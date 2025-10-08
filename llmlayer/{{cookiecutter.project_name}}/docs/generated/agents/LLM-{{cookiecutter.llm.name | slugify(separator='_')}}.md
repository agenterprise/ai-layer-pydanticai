# LLM "{{ cookiecutter.llm['name'] }}""
Overview agent
### System Prompt
```
{{ cookiecutter.llm.uid }}
```
### Properties


# Extend
Create a file "custom_model.py" below /app/ext/aimodel/{{cookiecutter.llm.uid | aiurnvar}} so that model factory can find it.


