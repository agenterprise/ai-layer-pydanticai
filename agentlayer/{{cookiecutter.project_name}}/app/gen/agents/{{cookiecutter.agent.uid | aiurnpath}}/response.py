     
from pydantic import BaseModel, Field

class {{cookiecutter.agent.uid | aiurnvar | capitalize }}AgentResponse(BaseModel):
    {% for key, value in cookiecutter.agent.outputproperties %}
    {{ key | aiurnvar }}: str = Field("",description="{{value['description']}}")
    {% endfor %}
   