from pyproject_parser import PyProject


masterpyproject = PyProject().load("pyproject.toml")
layerpyproject = PyProject().load(".layerconfig/{{cookiecutter.layername}}/pyproject.toml")

masterpyproject.dependency_groups.update(layerpyproject.dependency_groups)
masterpyproject.dump("pyproject.toml")
