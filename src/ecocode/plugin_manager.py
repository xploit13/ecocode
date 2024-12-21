# plugin_manager.py
# Manages plugins in EcoCode

class PluginManager:
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, plugin):
        self.plugins[plugin.name] = plugin
        print(f"Plugin {plugin.name} registered.")

    def run_plugin(self, plugin_name, data):
        if plugin_name in self.plugins:
            return self.plugins[plugin_name].analyze(data)
        else:
            print(f"Plugin {plugin_name} not found.")
            return None
