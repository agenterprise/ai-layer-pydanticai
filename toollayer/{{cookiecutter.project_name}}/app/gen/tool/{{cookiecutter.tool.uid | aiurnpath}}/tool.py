import logging
from pydantic_ai import Tool, RunContext
from app.gen.domainmodel.tool import AbstractTool, ToolType, MCPNotAvailableException
from app.gen.domainmodel.baseentity import BaseInputEntity, BaseOutputEntity

logger = logging.getLogger(__name__)
{% if cookiecutter.tool.input %}
from app.gen.entities.{{cookiecutter.tool.input | aiurnimport }}.entity import {{cookiecutter.tool.input | aiurnvar | capitalize }}Entity as ToolInputType
{% else %}
type ToolInputType=BaseInputEntity
{%endif%}

{% if cookiecutter.tool.output %}
from app.gen.entities.{{cookiecutter.tool.output | aiurnimport }}.entity import {{cookiecutter.tool.output | aiurnvar | capitalize }}Entity as ToolOutputType
{% else %}
type ToolOutputType=BaseOutputEntity
{%endif%}

class BaseTool(AbstractTool):
    """Base class for tools. Can be extended for custom behavior at extension layer (see app/ext/tool)."""
    description: str = {{ cookiecutter.tool.description }}
    
    """ Tool properties """
    properties:dict = {
        {% for key, value in cookiecutter.tool.properties.items() %}"{{ key | aiurnvar }}" : {{ value }} , {% endfor %}
    }
    type: ToolType = ToolType("{{ cookiecutter.tool.type }}")
    
    async def call(self, ctx:RunContext[str], input:ToolInputType):
        """Call the tool."""
        {% if cookiecutter.tool.type == "aiurn:tooltype:code" %}
        function = eval({{ cookiecutter.tool.endpoint }})
        return function(input)
        {%else%}
        pass
        {% endif %}   
    
    
    async def as_tool(self):

        """Convert to a pydantic-ai Tool."""
        {% if cookiecutter.tool.type == "aiurn:tooltype:mcp" %}
        try:
            from pydantic_ai.mcp import MCPServerStreamableHTTP
            mcpServer =  MCPServerStreamableHTTP({{cookiecutter.tool.endpoint}})
            await mcpServer.__aenter__()
            mcpServer.log_handler = logger.parent.handlers[0]
            mcpServer.log_level=logger.parent.level
            return mcpServer
        except Exception as e:
            endpoint = {{cookiecutter.tool.endpoint}}
            error = f"Error initializing MCP Server at {endpoint}."
            logger.error(error)
            logger.error(e)
            raise MCPNotAvailableException(error)
        {% elif cookiecutter.tool.type == "aiurn:tooltype:code" %}     
        return Tool(self.call, name={{ cookiecutter.tool.name }}, description=self.description)
        {% else %}
        raise NotImplementedError("Tool type {{ cookiecutter.tool.type }} not implemented.")
        {% endif %}
    