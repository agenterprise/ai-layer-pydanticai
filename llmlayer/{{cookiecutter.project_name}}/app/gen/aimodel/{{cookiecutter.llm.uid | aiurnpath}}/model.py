from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict
from pydantic_ai.models.openai import OpenAIChatModel, AsyncOpenAI
from pydantic_ai.models import Model, Provider, ModelSettings
from pydantic_ai.providers.azure import AzureProvider
from pydantic.dataclasses import dataclass
from app.gen.config.llm_settings import LLMSetting
from app.gen.domainmodel.aimodel.model import AbstractLanguageModel

settings = LLMSetting()
class BaseLanguageModel(AbstractLanguageModel):
    model: Model = None
    settings: LLMSetting = settings

    {% for key, value in cookiecutter.llm.properties.items() %}
    {{ key | aiurnvar }}:str = "{{ value }}"
    {% endfor %}
    model_config = ConfigDict(arbitrary_types_allowed=True)

    async def get_model(self) -> Model:
         return OpenAIChatModel(
                self.settings.{{cookiecutter.llm.uid | aiurnvar}}_model_name,
                provider = await self.get_provider(),
                settings = await self.get_setting()
            )
    
    async def get_provider(self) -> Provider:
        {% if cookiecutter.llm.provider == "aiurn:provider:azure" %}
            return AzureProvider(
                azure_endpoint=settings.{{cookiecutter.llm.uid | aiurnvar}}_endpoint,
                api_version=settings.{{cookiecutter.llm.uid | aiurnvar}}_version,
                api_key=settings.{{cookiecutter.llm.uid | aiurnvar}}_api_key
                )
        {% endif %}
    
    async def get_setting(self) -> ModelSettings:
         return ModelSettings(temperature=0.7, max_tokens=1000)

{{cookiecutter.llm.uid | aiurnvar }} = OpenAIChatModel(
                settings.{{cookiecutter.llm.uid | aiurnvar}}_model_name,
                {% if cookiecutter.llm.provider == "aiurn:provider:azure" %}
                provider=AzureProvider(
                    azure_endpoint=settings.{{cookiecutter.llm.uid | aiurnvar}}_endpoint,
                    api_version=settings.{{cookiecutter.llm.uid | aiurnvar}}_version,
                    api_key=settings.{{cookiecutter.llm.uid | aiurnvar}}_api_key,

                )
                {% endif %}
            )

