import logging
from typing import List
from pydantic import BaseModel
from pydantic_ai import Agent, Tool
from app.gen.domainmodel.agent import AbstractAgent
from app.gen.domainmodel.modelregistry import BaseModelregistry
from app.gen.domainmodel.toolregistry import BaseToolregistry
from app.gen.domainmodel.model import AbstractLanguageModel


logger = logging.getLogger(__name__)

class BaseAgent(AbstractAgent):
    toolregistry: BaseToolregistry
    systemprompt: str = {{ cookiecutter.agent.systemprompt }}
    properties:dict = {
        {% for key, value in cookiecutter.agent.properties.items() %}"{{ key | aiurnvar }}" : {{ value }} , {% endfor %}
    }
  
    llmref:str = "{{ cookiecutter.agent.llmref }}"
    toolrefs:List = [{% for ref in cookiecutter.agent.toolrefs %}"{{ ref }}", {% endfor %} ]
    llmmodel:AbstractLanguageModel = None
    
    _agent:Agent = None

    async def get_tools(self):

        for ref in self.toolrefs:
            if ref not in self.toolregistry.registry:
                logger.error(f"Tool {ref} not found in toolregistry")
                raise ValueError(f"Tool {ref} not found in toolregistry")
        
        basetools = [self.toolregistry.registry[ref] for ref in self.toolrefs]
        tools = [t.as_tool() for t in basetools]
        return tools
    
    async def _get_agent(self):
        self._agent = self._agent or Agent(  
            model=await self.llmmodel.get_model(),
            instructions=self.systemprompt,  
            tools=await self.get_tools()
        )
        return self._agent
    
    async def ask(self, query: str):
        """Use the agent to answer a question."""
        agent = await self._get_agent()
        result = await agent.run(f"{query}")
        return result 