from app.gen.config.settings_llm import LLMSettings

class BaseLLMEnvironmentContext():

    def LLMSettingsBean(self):
        return LLMSettings()
    
     """ Language Models""" 
    {%- for key, llm in cookiecutter.llms.items() %}
    def {{llm.uid | aiurnvar | capitalize }}LLMBean(self):
        from app.gen.aimodel.{{llm.uid | aiurnimport}}.model import BaseLanguageModel as {{llm.uid | aiurnvar | capitalize}}
        return {{llm.uid | aiurnvar | capitalize}}(settings=self.LLMSettingsBean())
    {%- endfor %}

