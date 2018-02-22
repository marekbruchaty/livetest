# encoding: utf-8
# module _ruamel_yaml
# from /usr/local/lib/python3.6/site-packages/_ruamel_yaml.cpython-36m-darwin.so
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import ruamel.yaml.error as __ruamel_yaml_error
import ruamel.yaml.events as __ruamel_yaml_events
import ruamel.yaml.nodes as __ruamel_yaml_nodes
import ruamel.yaml.tokens as __ruamel_yaml_tokens


class DocumentStartEvent(__ruamel_yaml_events.Event):
    # no doc
    def __init__(self, start_mark=None, end_mark=None, explicit=None, version=None, tags=None, comment=None): # reliably restored by inspect
        # no doc
        pass

    explicit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __slots__ = (
        'explicit',
        'version',
        'tags',
    )


