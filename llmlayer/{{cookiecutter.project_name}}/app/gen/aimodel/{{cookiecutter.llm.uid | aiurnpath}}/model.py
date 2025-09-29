from typing import Dict, Optional

from pydantic import ConfigDict
from pydantic_ai.models.openai import OpenAIChatModel, AsyncOpenAI
from pydantic_ai.models import Model
from pydantic_ai.providers.azure import AzureProvider
from pydantic.dataclasses import dataclass
from app.gen.config.llm_settings import LLMSetting

settings = LLMSetting()
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

