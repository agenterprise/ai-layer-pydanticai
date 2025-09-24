from pydantic import BaseModel
from pydantic_ai import Agent
from app.model.models import Modelregistry
from app.gen.aimodel.{{cookiecutter.llm.uid | aiurnvar}} import {{cookiecutter.llm.uid | aiurnvar }} 

{{cookiecutter.llm.uid | aiurnvar }}.temperature = 0.7