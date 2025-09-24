from pydantic import BaseModel
from pydantic_ai import Agent
from app.gen.agents.cook.agent import BaseAgent
class CustomAgent(BaseAgent):
   
    systemprompt: str = f"Hi Michael" 
    async def ask(self, query: str):
        # do my stuff here
        result = await super().ask(f"{query}")
        
        return result.output