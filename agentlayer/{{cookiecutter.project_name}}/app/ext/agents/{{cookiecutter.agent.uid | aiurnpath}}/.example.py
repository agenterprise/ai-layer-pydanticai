from pydantic import BaseModel
from pydantic_ai import Agent
from app.gen.agents.{{cookiecutter.agent.uid | aiurnimport}}.tool.agent import BaseAgent
class CustomAgent(BaseAgent):
   """Example of a custom agent extension."""
    systemprompt: str = f"Hi Michael" 
    async def ask(self, query: str):
        # do my stuff here
        result = await super().ask(self, f"{query}")
        
        return result.output