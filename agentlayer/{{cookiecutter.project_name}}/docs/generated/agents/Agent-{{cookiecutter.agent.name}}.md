# Agent "{{ cookiecutter.agent['name'] }}""
Overview agent
### System Prompt
```
{{ cookiecutter.agent.systemprompt }}
```
### Properties
{% for key, value in cookiecutter.agent.properties.items() %}
- **{{ key | aiurnvar }}**: {{ value }}
{% endfor %}


# Extend
Create a file "custom_agent.py" with a Subclass below /app/ext/agents/{{cookiecutter.agent.uid | aiurnpath}} so that model factory can find it.