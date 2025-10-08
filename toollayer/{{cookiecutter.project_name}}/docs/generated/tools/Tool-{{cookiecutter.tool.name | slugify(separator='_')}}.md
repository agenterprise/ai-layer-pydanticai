# Tool {{ cookiecutter.tool['name'] }}
{{ cookiecutter.tool['description'] }}

### Type
```
{{ cookiecutter.tool.type }}
```

{%- if cookiecutter.tool.type == "aiurn:tooltype:mcp" %}
Implemenation:  (MCPServerStreamableHTTP)[https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.MCPServerStreamableHTTP]
Endpoint: {{cookiecutter.tool.endpoint}})
{%-endif%}
{%- if cookiecutter.tool.type == "aiurn:tooltype:code" %}
Implementation: 
 ```python
  ({{ cookiecutter.tool.endpoint }})
```
 {%- endif %} 

### Input
{%- if cookiecutter.tool.input %}
* Package: app.gen.entities.{{cookiecutter.tool.input | aiurnimport }}.entity 
* Class: {{cookiecutter.tool.input | aiurnvar | capitalize }}Entity
{%- else %}
* Package: app.gen.domainmodel.baseentity
* Class: BaseInputEntity
{%-endif%}
### Output
{%- if cookiecutter.tool.output %}
* Package: app.gen.entities.{{cookiecutter.tool.output | aiurnimport }}.entity  
* Class: {{cookiecutter.tool.output | aiurnvar | capitalize }}Entity
{%- else %}
* Package: app.gen.domainmodel.baseentity
* Class: BaseOutputEntity
{%-endif%}
### Custom Properties
{%- for key, value in cookiecutter.tool.properties.items() %}
- **{{ key | aiurnvar }}**: {{ value }}
{%- endfor %}


# Extend
Create a file "custom_tool.py" with a Subclass below /app/ext/tools/{{cookiecutter.tool.uid | aiurnpath}} so that model factory can find it.