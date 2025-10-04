import logging
from pydantic_ai import Tool, RunContext
from app.gen.domainmodel.tool import AbstractTool, ToolType, MCPNotAvailableException
logger = logging.getLogger(__name__)


class BaseTool(AbstractTool):
    """Base class for tools. Can be extended for custom behavior at extension layer (see app/ext/tool)."""
    description: str = {{ cookiecutter.tool.description }}
    
    """ Tool properties """
    properties:dict = {
        {% for key, value in cookiecutter.tool.properties.items() %}"{{ key | aiurnvar }}" : {{ value }} , {% endfor %}
    }
    type: ToolType = ToolType("{{ cookiecutter.tool.type }}")
    async def prepare(self, query: str):
        """Prepare the tool call."""
        pass

    async def call(self, ctx:RunContext[str],  {% for key in cookiecutter.tool.inputproperties %}{{ key | aiurnvar }}:str , {% endfor %}ç):
        """Call the tool."""
        {% if cookiecutter.tool.type == "aiurn:tooltype:code" %}
        function = eval({{ cookiecutter.tool.endpoint }})
        return function({% for key in cookiecutter.tool.inputproperties %}{{ key | aiurnvar }}, {% endfor %})
        {% endif %}   
        pass
    
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
            logger.error("Error initializing MCP Server at {{cookiecutter.tool.endpoint}}")
            raise MCPNotAvailableException("Error initializing MCP Server at {{cookiecutter.tool.endpoint}}")
        {% elif cookiecutter.tool.type == "aiurn:tooltype:code" %}     
        #return Tool(self.call, name={{ cookiecutter.tool.name }}, description=self.description)
        return  Tool.from_schema(
            function=self.call,
            name={{ cookiecutter.tool.name }},
            description=self.description,
            json_schema={
                'additionalProperties': False,
                'properties': {
                    {% for key, value in cookiecutter.tool.inputproperties.items() %}
                    '{{ key | aiurnvar }}': {'description': '{{ value['description'] | replace('"','')}}', 'type': 'integer'},
                    {% endfor %}
                },
                'required': [{% for key, value in cookiecutter.tool.inputproperties.items() %}'{{ key | aiurnvar }}',{% endfor %}],
                'type': 'object',
            },
            takes_ctx=False,
)
        {% else %}
        raise NotImplementedError("Tool type {{ cookiecutter.tool.type }} not implemented.")
        {% endif %}
    