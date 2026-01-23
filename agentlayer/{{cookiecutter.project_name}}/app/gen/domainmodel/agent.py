from pydantic import BaseModel, Field


class AbstractAgent(BaseModel):
    agentid: str = Field(..., description="Unique identifier for the agent.")
    systemprompt: str = Field(..., description="System prompt for the agent.")
    namespace: str = Field(None, description="Optional namespace for the agent.")
    
    """Abstract base class for agents."""
    async def ask(self, query: str):
        pass
    async def ask_a2a(self, query: str):
        pass
    

