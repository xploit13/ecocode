# test_report_generator.py
# Unit tests for report_generator.py

import os
from ecocode.report_generator import generate_report

def test_generate_report():
    output_file = "test_report.txt"
    generate_report("test_script.py", output_file)
    assert os.path.exists(output_file)
    os.remove(output_file)
