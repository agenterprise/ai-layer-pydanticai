from pydantic import BaseModel

class AbstractAgent(BaseModel):
    """Abstract base class for agents."""
    async def ask(self, query: str):
        pass