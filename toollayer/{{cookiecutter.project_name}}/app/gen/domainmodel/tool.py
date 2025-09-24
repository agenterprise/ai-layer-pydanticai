from pydantic import BaseModel

class AbstractTool(BaseModel):

    async def call(self, query: str):
        pass

    async def prepare(self, query: str):
        pass

    