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
            file.write(f"Energy Analysis Report - {datetime.now()}\n")
            file.write("=" * 50 + "\n")
            for key, value in data.items():
                file.write(f"{key}: {value}\n")
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
            file.write(f"<html><head><title>Energy Analysis Report</title></head><body>\n")
            file.write(f"<h1>Energy Analysis Report - {datetime.now()}</h1>\n")
            file.write("<table border='1'>\n")
            file.write("<tr><th>Key</th><th>Value</th></tr>\n")
            for key, value in data.items():
                file.write(f"<tr><td>{key}</td><td>{value}</td></tr>\n")
            file.write("</table>\n")
            file.write("</body></html>\n")
        print(f"HTML report generated at: {file_path}")
        return file_path
