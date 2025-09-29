import os

from jinja2.ext import Extension


class AIURNExtension(Extension):
    def __init__(self, environment):
        super(AIURNExtension,self).__init__(environment)
        environment.filters['aiurnpath'] = lambda v: os.path.join(*v.split(':')[2:])
        environment.filters['aiurnvar'] = lambda v: '_'.join(v.split(':')[2:]).replace('-', '_')
        environment.filters['aiurnimport'] = lambda v:'.'.join(v.split(':')[2:])

"""
@simple_filter
def aiurnpath(v):
    path = os.path.join(*v.split(':')[2:])
    return path

@simple_filter
def aiurnvar(v):
    return '_'.join(v.split(':')[2:]).replace('-', '_')
  
"""