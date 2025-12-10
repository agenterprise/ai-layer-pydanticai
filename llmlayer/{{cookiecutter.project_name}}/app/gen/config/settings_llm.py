from pydantic import Field
from pydantic_settings import BaseSettings

class LLMSettings(BaseSettings):
    {%- for key, llm in cookiecutter.llms.items() %}
    {{llm.uid | aiurnvar}}_api_key:str = "your api key"
    {{llm.uid | aiurnvar}}_model_name:str = Field({{llm.model}}, description="Model name or identifier")
    {{llm.uid | aiurnvar}}_endpoint:str = Field({{llm.endpoint}}, description="API endpoint for the LLM")
    {{llm.uid | aiurnvar}}_version:str = Field({{llm.version}}, description="Version of the LLM API")
    {%- endfor %}
