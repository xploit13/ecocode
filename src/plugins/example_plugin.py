# example_plugin.py
# Example plugin demonstrating extensibility in EcoCode

class ExamplePlugin:
    def __init__(self):
        self.name = "ExamplePlugin"

    def analyze(self, data):
        print("Analyzing data in ExamplePlugin...")
        return {"analysis": "This is an example plugin analysis."}
