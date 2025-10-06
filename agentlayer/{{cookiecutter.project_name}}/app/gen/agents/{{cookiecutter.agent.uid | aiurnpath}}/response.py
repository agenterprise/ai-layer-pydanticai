     
from pydantic import BaseModel, Field

class {{cookiecutter.agent.uid | aiurnvar | capitalize }}AgentResponse(BaseModel):
    {% if cookiecutter.agent.outputproperties|length == 0 %}
    result: str = Field("", description="The result of agen call")
    {% endif %}
    {% for key, value in cookiecutter.agent.outputproperties.items() %}
    {{ key | aiurnvar }}: str = Field("",description="{{value['description'] | replace('"','')}}")
    {% endfor %}
   