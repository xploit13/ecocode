# test_plugin_manager.py
# Extended unit tests for plugin_manager.py

import pytest
from ecocode.plugin_manager import PluginManager


class MockPlugin:

    def __init__(self):
        self.name = "MockPlugin"

    def analyze(self, data):
        return {"mock_analysis": "analysis_result"}


class AnotherMockPlugin:

    def __init__(self):
        self.name = "AnotherMockPlugin"

    def analyze(self, data):
        return {"analysis": f"Processed {data}"}


@pytest.fixture
def plugin_manager():
    return PluginManager()


def test_register_plugin(plugin_manager):
    plugin = MockPlugin()
    plugin_manager.register_plugin(plugin)
    assert "MockPlugin" in plugin_manager.plugins, "Plugin should be registered successfully."


def test_run_plugin(plugin_manager):
    plugin = MockPlugin()
    plugin_manager.register_plugin(plugin)
    result = plugin_manager.run_plugin("MockPlugin", {"key": "value"})
    assert result[
        "mock_analysis"] == "analysis_result", "Plugin should return the correct analysis result."


def test_run_nonexistent_plugin(plugin_manager):
    result = plugin_manager.run_plugin("NonExistentPlugin", {"key": "value"})
    assert result is None, "Running a nonexistent plugin should return None."


def test_load_plugins_from_directory(tmpdir):
    # Create a mock plugin file in the plugins directory
    plugin_dir = tmpdir.mkdir("plugins")
    plugin_file = plugin_dir.join("example_plugin.py")
    plugin_file.write("""
class Plugin:
    def __init__(self):
        self.name = "ExamplePlugin"

    def analyze(self, data):
        return {"analysis": "Example plugin analysis"}
""")
    plugin_manager = PluginManager(plugin_directory=str(plugin_dir))
    assert "ExamplePlugin" in plugin_manager.plugins, "Plugin should be loaded from directory."


def test_list_plugins(plugin_manager):
    plugin1 = MockPlugin()
    plugin2 = AnotherMockPlugin()
    plugin_manager.register_plugin(plugin1)
    plugin_manager.register_plugin(plugin2)
    plugin_list = plugin_manager.list_plugins()
    assert "MockPlugin" in plugin_list, "Plugin list should include MockPlugin."
    assert "AnotherMockPlugin" in plugin_list, "Plugin list should include AnotherMockPlugin."


# Run tests using pytest
if __name__ == "__main__":
    pytest.main()
