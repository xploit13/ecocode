# plugin_example.py
# Extended example script showing advanced plugin creation and usage in EcoCode

from ecocode.plugin_manager import PluginManager

# Define a custom plugin with advanced functionality
class AdvancedPlugin:
    def __init__(self):
        self.name = "AdvancedPlugin"

    def analyze(self, data):
        # Example analysis logic
        result = {"analysis": f"Processed data: {data}"}
        if "key_metric" in data:
            result["key_metric"] = data["key_metric"] * 2
        else:
            result["key_metric"] = "No key_metric provided"
        return result

if __name__ == "__main__":
    # Initialize the PluginManager
    plugin_manager = PluginManager()

    # Create an instance of the custom plugin
    advanced_plugin = AdvancedPlugin()

    # Register the plugin
    plugin_manager.register_plugin(advanced_plugin)

    # Use the plugin to analyze data
    sample_data = {"key_metric": 42, "other_info": "Sample data"}
    print("Running the AdvancedPlugin...")
    result = plugin_manager.run_plugin("AdvancedPlugin", sample_data)

    # Display the plugin's analysis result
    print("Plugin Analysis Results:")
    for key, value in result.items():
        print(f"{key}: {value}")
