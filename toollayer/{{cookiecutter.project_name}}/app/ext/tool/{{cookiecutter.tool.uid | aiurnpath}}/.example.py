from pydantic import BaseModel
from app.gen.tool.{{cookiecutter.tool.uid | aiurnimport}}.tool import BaseTool
class CustomTool(BaseTool):
   
    async def call(self, query: str):
        result = await super().call(self,query)
        return f"Not implemented yet, but may be useful: {result}"