from pydantic import BaseModel
from pydantic_ai import Agent
from app.gen.agents.cook.tool import BaseTool
class CustomTool(BaseTool):
   
    async def call(self, query: str):
        # do my stuff here
        result = await super().ask(f"{query}")
        
        return result.output