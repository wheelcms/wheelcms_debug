from wheelcms_axle.registries.configuration import configuration_registry
from wheelcms_axle.configuration import BaseConfigurationHandler

from wheelcms_axle.content import type_registry

from wheelcms_axle.registries import core

class BaseContext(object):
    def __getattr__(self, attribute):
        return getattr(self.wrapped, attribute)

class SpokeContext(BaseContext):
    def __init__(self, s):
        self.wrapped = s

    def icon(self):
        return self.wrapped.full_type_icon_path()

    def children(self):
        if self.wrapped.children is None:
            return "Any"
        if not self.wrapped.children: # empty sequence
            return "None"

        return ", ".join(s.title for s in self.wrapped.children)

    def explicit_children(self):
        if self.wrapped.explicit_children is None:
            return "Any"
        if not self.wrapped.explicit_children: # empty sequence
            return "None"

        return ", ".join(s.title for s in self.wrapped.explicit_children)

    def primary(self):
        if self.wrapped.primary is None:
            return "None"
        return self.wrapped.primary.title

    def workflow(self):
        return core.workflow[self.wrapped].__name__

class ConfigurationHandler(BaseConfigurationHandler):
    id = "debug"
    label = "Debug"
    model = None
    form = None

    def view(self, handler, instance):
        ctx = {}
        ctx['spokes'] = [SpokeContext(s) for s in type_registry.values()]

        # import pdb; pdb.set_trace()
        
        return handler.template("wheelcms_debug/configure_debug.html", **ctx)


configuration_registry.register(ConfigurationHandler)

