from wheelcms_axle.registries.configuration import configuration_registry
from wheelcms_axle.configuration import BaseConfigurationHandler

class ConfigurationHandler(BaseConfigurationHandler):
    id = "debug"
    label = "Debug"
    model = None
    form = None

    def view(self, handler, instance):
        return handler.template("wheelcms_debug/configure_debug.html")


configuration_registry.register(ConfigurationHandler)

