from typing import List
from pydantic import BaseModel
from pydantic_ai import Agent, Tool
from app.gen.domainmodel.agent import AbstractAgent
from app.gen.domainmodel.modelregistry import BaseModelregistry
from app.gen.domainmodel.toolregistry import BaseToolregistry


class BaseAgent(AbstractAgent):
    toolregistry: BaseToolregistry
    modelregistry: BaseModelregistry
    systemprompt: str = "{{ cookiecutter.agent.systemprompt }}"
    {% for key, value in cookiecutter.agent.properties.items() %}
    {{ key | aiurnvar }}:str = "{{ value }}"
    {% endfor %}
    llmref:str = "{{ cookiecutter.agent.llmref }}"
    toolrefs:List = [{% for ref in cookiecutter.agent.toolrefs %}"{{ ref }}", {% endfor %} ]

    async def ask(self, query: str):
        basetools = [self.toolregistry[ref] for ref in self.toolrefs]
        tools = [t.as_tool() for t in basetools]
        agent = Agent(  
            model=self.modelregistry.registry[self.llmref],
            instructions=self.systemprompt,  
            tools=tools
        )
        result = await agent.run(f"{query}")
        return result 