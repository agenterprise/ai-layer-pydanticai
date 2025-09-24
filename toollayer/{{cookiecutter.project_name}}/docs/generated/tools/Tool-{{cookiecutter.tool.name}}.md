# Tool "{{ cookiecutter.tool['name'] }}""
Overview agent
### Type
```
{{ cookiecutter.tool.type }}
```
### Properties
{% for key, value in cookiecutter.tool.properties.items() %}
- **{{ key | aiurnvar }}**: {{ value }}
{% endfor %}


# Extend
Create a file "custom_tool.py" with a Subclass below /app/ext/tools/{{cookiecutter.tool.uid | aiurnpath}} so that model factory can find it.