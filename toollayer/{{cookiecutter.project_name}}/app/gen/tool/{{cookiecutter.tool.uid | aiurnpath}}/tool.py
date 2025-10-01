from pydantic import BaseModel
from pydantic_ai import Tool, RunContext
from app.gen.domainmodel.tool import AbstractTool

class BaseTool(AbstractTool):

    description: str = {{ cookiecutter.tool.description }}
    properties:dict = {
        {% for key, value in cookiecutter.tool.properties.items() %}"{{ key | aiurnvar }}" : {{ value }} , {% endfor %}
    }
   
    async def prepare(self, query: str):
        return query 

    async def call(self, ctx:RunContext[str], query: str):
        return query 
    
    def as_tool(self):
        from pydantic_ai import Tool
        return Tool(self.call, name={{ cookiecutter.tool.name }}, description=self.description)
    

{{cookiecutter.tool.uid | aiurnvar}} = BaseTool()