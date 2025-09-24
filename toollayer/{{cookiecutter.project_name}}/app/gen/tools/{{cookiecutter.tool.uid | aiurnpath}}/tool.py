from pydantic import BaseModel
from pydantic_ai import Agent
from app.gen.domainmodel.tool import AbstractTool

class BaseTool(AbstractTool):

    systemprompt: str = "{{ cookiecutter.tool.description }}"
    {% for key, value in cookiecutter.tool.properties.items() %}
    {{ key | aiurnvar }}:str = "{{ value }}"
    {% endfor %}

    async def prepare(self, query: str):
        return query 

    async def call(self, query: str):
        return query 