# test_eco_score.py
# Extended unit tests for eco_score.py

import pytest
import os
from ecocode.eco_score import EcoScoreCalculator


@pytest.fixture
def calculator():
    return EcoScoreCalculator()


def test_calculate_score_valid_file(calculator, tmpdir):
    test_file = tmpdir.join("test_script.py")
    test_file.write("print('Hello, world!')")
    score = calculator.calculate_score(str(test_file))
    assert 0 <= score <= 100, "Eco-score should be within valid range."


def test_calculate_score_nonexistent_file(calculator):
    with pytest.raises(FileNotFoundError):
        calculator.calculate_score("nonexistent_file.py")


def test_evaluate_efficiency_valid_file(calculator, tmpdir):
    test_file = tmpdir.join("test_script.py")
    test_file.write("print('Hello, world!')\nprint('Another line')\n")
    efficiency_report = calculator.evaluate_efficiency(str(test_file))

    assert "file_size" in efficiency_report, "Efficiency report should include file size."
    assert "lines_of_code" in efficiency_report, "Efficiency report should include lines of code."
    assert "eco_score" in efficiency_report, "Efficiency report should include eco-score."
    assert efficiency_report[
        "lines_of_code"] == 2, "Line count should match the file content."


def test_generate_recommendation_large_file(calculator, tmpdir):
    test_file = tmpdir.join("large_script.py")
    test_file.write("\n".join(["print('Line')"] * 600))  # 600 lines
    efficiency_report = calculator.evaluate_efficiency(str(test_file))
    assert "recommendation" in efficiency_report, "Efficiency report should include recommendations."
    assert "refactoring" in efficiency_report["recommendation"].lower(
    ), "Recommendation should suggest refactoring for large files."


def test_generate_recommendation_small_file(calculator, tmpdir):
    test_file = tmpdir.join("small_script.py")
    test_file.write("print('Hello, world!')")
    efficiency_report = calculator.evaluate_efficiency(str(test_file))
    assert "recommendation" in efficiency_report, "Efficiency report should include recommendations."
    assert "efficient" in efficiency_report["recommendation"].lower(
    ), "Recommendation should confirm code is efficient for small files."


# Run tests using pytest
if __name__ == "__main__":
    pytest.main()
