# test_eco_score.py
# Unit tests for eco_score.py

from ecocode.eco_score import calculate_score

def test_calculate_score():
    score = calculate_score("test_script.py")
    assert score == 85
