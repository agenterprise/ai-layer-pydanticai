from pydantic import BaseModel

class AbstractModel(BaseModel):
        
        async def get_provider(self):
            pass

        async def get_model(self):
            pass