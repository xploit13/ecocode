# report_generator.py
# Extended implementation for generating energy analysis reports in EcoCode

import json
import os
from datetime import datetime


class ReportGenerator:

    def __init__(self, output_directory="reports"):
        """
        Initialize the ReportGenerator.

        Args:
            output_directory (str): Directory to save generated reports.
        """
        self.output_directory = output_directory

        # Ensure the output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

    def generate_text_report(self, data, filename="report.txt"):
        """
        Generate a text-based energy analysis report.

        Args:
            data (dict): Data to include in the report.
            filename (str): Name of the text report file.

        Returns:
            str: Path to the generated report.
        """
        file_path = os.path.join(self.output_directory, filename)
        with open(file_path, "w") as file:
            file.write(f"Energy Analysis Report - {datetime.now()}")
            file.write("=" * 50 + "")
            for key, value in data.items():
                file.write(f"{key}: {value}")
        print(f"Text report generated at: {file_path}")
        return file_path

    def generate_json_report(self, data, filename="report.json"):
        """
        Generate a JSON-based energy analysis report.

        Args:
            data (dict): Data to include in the report.
            filename (str): Name of the JSON report file.

        Returns:
            str: Path to the generated report.
        """
        file_path = os.path.join(self.output_directory, filename)
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
        print(f"JSON report generated at: {file_path}")
        return file_path

    def generate_html_report(self, data, filename="report.html"):
        """
        Generate an HTML-based energy analysis report.

        Args:
            data (dict): Data to include in the report.
            filename (str): Name of the HTML report file.

        Returns:
            str: Path to the generated report.
        """
        file_path = os.path.join(self.output_directory, filename)
        with open(file_path, "w") as file:
            file.write(
                f"<html><head><title>Energy Analysis Report</title></head><body>"
            )
            file.write(f"<h1>Energy Analysis Report - {datetime.now()}</h1>")
            file.write("<table border='1'>")
            file.write("<tr><th>Key</th><th>Value</th></tr>")
            for key, value in data.items():
                file.write(f"<tr><td>{key}</td><td>{value}</td></tr>")
            file.write("</table>")
            file.write("</body></html>")
        print(f"HTML report generated at: {file_path}")
        return file_path


# Example usage
if __name__ == "__main__":
    generator = ReportGenerator()
    sample_data = {
        "Total Energy Usage": "120 J",
        "Execution Time": "15 seconds",
        "Processes Analyzed": 3,
        "Average Energy Usage": "40 J"
    }

    generator.generate_text_report(sample_data)
    generator.generate_json_report(sample_data)
    generator.generate_html_report(sample_data)
