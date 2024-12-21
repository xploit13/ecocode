# plugin_example.py
# Example script showing how to create and use a plugin in EcoCode

from ecocode.plugin_manager import PluginManager

# Define a custom plugin
class CustomPlugin:
    def __init__(self, name):
        self.name = name

    def analyze(self, data):
        # Example analysis logic
        print(f"Plugin '{self.name}' is analyzing the data...")
        return {"message": f"Analysis complete by {self.name}"}

if __name__ == "__main__":
    # Initialize the PluginManager
    plugin_manager = PluginManager()

    # Create an instance of the custom plugin
    custom_plugin = CustomPlugin(name="ExamplePlugin")

    # Register the plugin
    plugin_manager.register_plugin(custom_plugin)

    # Use the plugin to analyze data
    print("Running the custom plugin...")
    result = plugin_manager.run_plugin("ExamplePlugin", data={"sample": "data"})

    print("Plugin Result:")
    print(result)
