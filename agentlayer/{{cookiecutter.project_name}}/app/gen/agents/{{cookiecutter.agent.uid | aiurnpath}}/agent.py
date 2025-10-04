import logging
from pydantic_ai import Agent, FunctionToolset
from app.gen.domainmodel.agent import AbstractAgent
from app.gen.domainmodel.model import AbstractLanguageModel
from app.gen.domainmodel.tool import AbstractTool, ToolType, MCPNotAvailableException
from fastapi import  HTTPException
 


logger = logging.getLogger(__name__)

class BaseAgent(AbstractAgent):
    """Base class for agents."""
    systemprompt: str = {{ cookiecutter.agent.systemprompt }}
   
    """ LLM reference """
    llmref:str = "{{ cookiecutter.agent.llmref }}"
    llmmodel:AbstractLanguageModel = None

    """Tool references"""
    {% for ref in cookiecutter.agent.toolrefs %}
    {{ ref | aiurnvar }}: AbstractTool
    {% endfor %} 

    """ Agent properties """
    properties:dict = {
        {% for key, value in cookiecutter.agent.properties.items() %}"{{ key | aiurnvar }}" : {{ value }} , {% endfor %}
    }

    """ Internal pydantic agent instance """
    _agent:Agent = None

    async def _get_toolsets(self):
        """Get the toolset for the agent."""
        toolsets = []
        alltools = [{% for ref in cookiecutter.agent.toolrefs %}self.{{ ref | aiurnvar }},{% endfor %}]
        functiontools = [await tool.as_tool() for tool in alltools if tool.type!=ToolType.MCP]     
        functionaltoolset = FunctionToolset(tools=functiontools)
        toolsets.append(functionaltoolset)

        for tool in alltools:
            if tool.type==ToolType.MCP:
                try:
                    mcptool = await tool.as_tool()
                except MCPNotAvailableException:
                    logger.warning(f"MCP Tool {tool} / {tool.endpoint} is not running. Not recognized in toolset.")
                if mcptool.is_running:
                    toolsets.append(mcptool)
       

        return toolsets
    
    async def _get_agent(self, force_renew: bool = False):
        """Get the agent instance."""
        if force_renew:
            self._agent = None
            
        self._agent = self._agent or Agent(  
            model=await self.llmmodel.get_model(),
            instructions=self.systemprompt,  
            toolsets=await self._get_toolsets()
        )
        return self._agent
    
    async def ask(self, query: str):
        """Use the agent to answer a question."""
        try:
            agent = await self._get_agent()
            result = await agent.run(f"{query}")
            return result 
        except Exception as e:
            import uuid
            errorcode = uuid.uuid4().hex    
            logger.error(f"Error (ref: {errorcode} ) agent {self}: {e}")
            raise HTTPException(status_code=500, detail="Internal Agent Error (ref: {errorcode} )")