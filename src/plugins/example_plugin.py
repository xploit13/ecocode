# example_plugin.py
# Extended example plugin demonstrating advanced extensibility in EcoCode


class ExamplePlugin:

    def __init__(self):
        self.name = "ExamplePlugin"
        self.version = "1.0.0"
        self.author = "EcoCode Team"

    def analyze(self, data):
        """
        Analyze the input data and provide results.

        Args:
            data (dict): Input data for analysis.

        Returns:
            dict: Analysis results.
        """
        print(f"Running {self.name} (v{self.version}) by {self.author}")
        analysis_results = {
            "input_data": data,
            "analysis": "Example analysis result",
            "recommendations": self.generate_recommendations(data)
        }
        return analysis_results

    def generate_recommendations(self, data):
        """
        Generate optimization recommendations based on the analysis.

        Args:
            data (dict): Input data for generating recommendations.

        Returns:
            list: A list of recommendations.
        """
        recommendations = []
        if isinstance(data, dict) and "energy_usage" in data:
            energy_usage = data["energy_usage"]
            if energy_usage > 100:
                recommendations.append(
                    "Consider optimizing high energy-consuming operations.")
            else:
                recommendations.append(
                    "Energy usage is within acceptable limits.")
        else:
            recommendations.append("Insufficient data for recommendations.")
        return recommendations


# Example usage
if __name__ == "__main__":
    plugin = ExamplePlugin()
    sample_data = {"energy_usage": 120, "process": "Sample Process"}
    result = plugin.analyze(sample_data)
    print("Plugin Analysis Results:", result)
