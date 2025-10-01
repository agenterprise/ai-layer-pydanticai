from pydantic_ai import Tool, RunContext
from app.gen.domainmodel.tool import AbstractTool

class BaseTool(AbstractTool):
    """Base class for tools. Can be extended for custom behavior at extension layer (see app/ext/tool)."""
    description: str = {{ cookiecutter.tool.description }}

    """ Tool properties """
    properties:dict = {
        {% for key, value in cookiecutter.tool.properties.items() %}"{{ key | aiurnvar }}" : {{ value }} , {% endfor %}
    }
   
    async def prepare(self, query: str):
        """Prepare the tool call."""
        return query 

    async def call(self, ctx:RunContext[str], query: str):
        """Call the tool."""
        return query 
    
    def as_tool(self):
        """Convert to a pydantic-ai Tool."""
        return Tool(self.call, name={{ cookiecutter.tool.name }}, description=self.description)
    