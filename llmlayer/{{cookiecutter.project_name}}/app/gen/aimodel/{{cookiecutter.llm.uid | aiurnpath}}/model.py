from pydantic import ConfigDict
from pydantic_ai.models.openai import OpenAIChatModel as SelectedModel
from pydantic_ai.models import Model, ModelSettings

from app.gen.config.settings import LLMSettings
from app.gen.domainmodel.model import AbstractLanguageModel

{%- if cookiecutter.llm.provider == "aiurn:model:provider:azure" %}
from pydantic_ai.providers.azure import AzureProvider as SelectedProvider
{%- else %}
from pydantic_ai.providers.openai import OpenAIProvider as SelectedProvider
{%- endif %}

class BaseLanguageModel(AbstractLanguageModel):
    """Base class for language models."""

    model: SelectedModel = None
    provider: SelectedProvider = None
    settings: LLMSettings = None

    """Language model configuration."""
    properties:dict = {
        {%- for key, value in cookiecutter.llm.properties.items() %}"{{ key | aiurnvar }}" : {{ value }} , {%- endfor %}
    }

    """ Allow arbitrary types for provider and model """
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    async def get_model(self) -> Model:
        """Get the language model instance."""
        self.model = self.model or  SelectedModel(
                self.settings.{{cookiecutter.llm.uid | aiurnvar}}_model_name,
                provider = await self.get_provider(),
                settings = await self.get_setting()
            )
        return self.model
    
    async def get_provider(self) -> SelectedProvider:
        """Get the provider instance."""
        self.provider = self.provider or SelectedProvider(
                    azure_endpoint=self.settings.{{cookiecutter.llm.uid | aiurnvar}}_endpoint,
                    api_version=self.settings.{{cookiecutter.llm.uid | aiurnvar}}_version,
                    api_key=self.settings.{{cookiecutter.llm.uid | aiurnvar}}_api_key
                    )
        return self.provider
           
    async def get_setting(self) -> ModelSettings:
        """Get the model settings."""
        return ModelSettings(self.properties)
  
