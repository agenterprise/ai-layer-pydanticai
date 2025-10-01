from pydantic import BaseModel

class AbstractTool(BaseModel):
    """Abstract base class for tools."""
    async def call(self, query: str):
        pass

    async def prepare(self, query: str):
        pass
    

    