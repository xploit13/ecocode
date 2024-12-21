# plugin_manager.py
# Extended implementation for managing plugins in EcoCode

import importlib
import os


class PluginManager:

    def __init__(self, plugin_directory="plugins"):
        """
        Initialize the PluginManager.

        Args:
            plugin_directory (str): Directory containing plugin files.
        """
        self.plugins = {}
        self.plugin_directory = plugin_directory

        # Load plugins from the specified directory
        if os.path.exists(plugin_directory):
            self.load_plugins(plugin_directory)

    def register_plugin(self, plugin):
        """
        Register a new plugin.

        Args:
            plugin: An instance of the plugin to register.
        """
        self.plugins[plugin.name] = plugin
        print(f"Plugin '{plugin.name}' registered successfully.")

    def run_plugin(self, plugin_name, data):
        """
        Execute a registered plugin with the provided data.

        Args:
            plugin_name (str): Name of the plugin to execute.
            data (dict): Input data for the plugin.

        Returns:
            dict: Output from the plugin's `analyze` method.
        """
        if plugin_name in self.plugins:
            return self.plugins[plugin_name].analyze(data)
        else:
            print(f"Plugin '{plugin_name}' not found.")
            return None

    def load_plugins(self, directory):
        """
        Load all plugins from the specified directory.

        Args:
            directory (str): Path to the plugins directory.
        """
        for filename in os.listdir(directory):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]
                self._load_plugin_module(directory, module_name)

    def _load_plugin_module(self, directory, module_name):
        """
        Dynamically load a plugin module.

        Args:
            directory (str): Directory containing the plugin module.
            module_name (str): Name of the module to load.
        """
        module_path = f"{directory.replace('/', '.')}.{module_name}"
        try:
            module = importlib.import_module(module_path)
            if hasattr(module, "Plugin"):
                plugin_instance = module.Plugin()
                self.register_plugin(plugin_instance)
            else:
                print(
                    f"Module '{module_name}' does not have a 'Plugin' class.")
        except Exception as e:
            print(f"Failed to load plugin '{module_name}': {e}")

    def list_plugins(self):
        """
        List all registered plugins.

        Returns:
            list: Names of all registered plugins.
        """
        return list(self.plugins.keys())


# Example usage
if __name__ == "__main__":
    manager = PluginManager(plugin_directory="plugins")

    # List all loaded plugins
    print("Available Plugins:", manager.list_plugins())

    # Run a specific plugin
    plugin_output = manager.run_plugin("ExamplePlugin", {"data": "test"})
    print("Plugin Output:", plugin_output)
