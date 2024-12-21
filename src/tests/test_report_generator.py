# test_report_generator.py
# Extended unit tests for report_generator.py

import os
import pytest
from ecocode.report_generator import ReportGenerator


@pytest.fixture
def report_generator():
    return ReportGenerator(output_directory="test_reports")


def test_generate_text_report(report_generator, tmpdir):
    sample_data = {
        "Total Energy Usage": "120 J",
        "Execution Time": "15 seconds"
    }
    report_path = report_generator.generate_text_report(
        sample_data, filename="text_report.txt")
    assert os.path.exists(report_path), "Text report file should be created."
    with open(report_path, "r") as file:
        content = file.read()
        assert "Total Energy Usage: 120 J" in content, "Report should include correct energy usage."
        assert "Execution Time: 15 seconds" in content, "Report should include correct execution time."


def test_generate_json_report(report_generator, tmpdir):
    sample_data = {
        "Total Energy Usage": "120 J",
        "Execution Time": "15 seconds"
    }
    report_path = report_generator.generate_json_report(
        sample_data, filename="json_report.json")
    assert os.path.exists(report_path), "JSON report file should be created."
    with open(report_path, "r") as file:
        content = file.read()
        assert '"Total Energy Usage": "120 J"' in content, "Report should include correct energy usage."
        assert '"Execution Time": "15 seconds"' in content, "Report should include correct execution time."


def test_generate_html_report(report_generator, tmpdir):
    sample_data = {
        "Total Energy Usage": "120 J",
        "Execution Time": "15 seconds"
    }
    report_path = report_generator.generate_html_report(
        sample_data, filename="html_report.html")
    assert os.path.exists(report_path), "HTML report file should be created."
    with open(report_path, "r") as file:
        content = file.read()
        assert "<td>Total Energy Usage</td>" in content, "Report should include correct energy usage."
        assert "<td>Execution Time</td>" in content, "Report should include correct execution time."


def test_invalid_output_directory(tmpdir):
    invalid_dir = "/invalid/path/to/reports"
    with pytest.raises(OSError):
        ReportGenerator(output_directory=invalid_dir)


def test_empty_data_handling(report_generator):
    report_path = report_generator.generate_text_report(
        {}, filename="empty_report.txt")
    assert os.path.exists(
        report_path), "Report file should be created even for empty data."
    with open(report_path, "r") as file:
        content = file.read()
        assert "Energy Analysis Report" in content, "Report should still include a title."


# Cleanup the test_reports directory after tests
def teardown_function():
    report_dir = "test_reports"
    if os.path.exists(report_dir):
        for file in os.listdir(report_dir):
            os.remove(os.path.join(report_dir, file))
        os.rmdir(report_dir)


# Run tests using pytest
if __name__ == "__main__":
    pytest.main()
