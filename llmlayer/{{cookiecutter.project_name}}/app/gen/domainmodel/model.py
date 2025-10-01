from pydantic import BaseModel

class AbstractLanguageModel(BaseModel):
        
    async def get_provider(self):
        pass

    async def get_model(self):
        pass