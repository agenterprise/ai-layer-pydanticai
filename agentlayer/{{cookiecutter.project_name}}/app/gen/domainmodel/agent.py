from pydantic import BaseModel

class AbstractAgent(BaseModel):

    async def ask(self, query: str):
        pass