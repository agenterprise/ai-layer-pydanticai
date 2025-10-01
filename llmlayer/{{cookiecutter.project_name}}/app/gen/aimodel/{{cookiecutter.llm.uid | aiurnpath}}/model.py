from pydantic import ConfigDict
from pydantic_ai.models.openai import OpenAIChatModel as SelectedModel
from pydantic_ai.models import Model, ModelSettings

from app.gen.config.settings import LLMSettings
from app.gen.domainmodel.model import AbstractLanguageModel

{% if cookiecutter.llm.provider == "aiurn:model:provider:azure" %}
from pydantic_ai.providers.azure import AzureProvider as SelectedProvider
{% else %}
from pydantic_ai.providers.openai import OpenAIProvider as SelectedProvider
{% endif %}

class BaseLanguageModel(AbstractLanguageModel):
    model: SelectedModel = None
    settings: LLMSettings = None
    properties:dict = {
        {% for key, value in cookiecutter.llm.properties.items() %}"{{ key | aiurnvar }}" : {{ value }} , {% endfor %}
    }
    model_config = ConfigDict(arbitrary_types_allowed=True)

    async def get_model(self) -> Model:
         return SelectedModel(
                self.settings.{{cookiecutter.llm.uid | aiurnvar}}_model_name,
                provider = await self.get_provider(),
                settings = await self.get_setting()
            )
    
    async def get_provider(self) -> SelectedProvider:
       
            return SelectedProvider(
                azure_endpoint=self.settings.{{cookiecutter.llm.uid | aiurnvar}}_endpoint,
                api_version=self.settings.{{cookiecutter.llm.uid | aiurnvar}}_version,
                api_key=self.settings.{{cookiecutter.llm.uid | aiurnvar}}_api_key
                )
           
    async def get_setting(self) -> ModelSettings:
         
         return ModelSettings(self.properties)
  
