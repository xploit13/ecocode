# test_plugin_manager.py
# Unit tests for plugin_manager.py

from ecocode.plugin_manager import PluginManager

class MockPlugin:
    def __init__(self):
        self.name = "MockPlugin"

    def analyze(self, data):
        return {"mock": "analysis"}

def test_register_and_run_plugin():
    manager = PluginManager()
    plugin = MockPlugin()
    manager.register_plugin(plugin)
    result = manager.run_plugin("MockPlugin", {})
    assert result == {"mock": "analysis"}
