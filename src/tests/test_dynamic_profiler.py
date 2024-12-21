# test_dynamic_profiler.py
# Extended unit tests for dynamic_profiler.py

import pytest
from ecocode.dynamic_profiler import DynamicProfiler

def test_profiler_initialization():
    profiler = DynamicProfiler()
    assert profiler.get_results() == {}, "Profiler should initialize with empty results."

def test_profiler_start_stop():
    profiler = DynamicProfiler()
    profiler.start()
    assert profiler.active, "Profiler should be active after start."
    profiler.stop()
    assert not profiler.active, "Profiler should not be active after stop."

def test_function_profiling():
    profiler = DynamicProfiler()
    profiler.start()

    @profiler.profile_function
    def sample_function():
        return sum(range(100))

    result = sample_function()
    assert result == 4950, "Sample function did not return the expected result."

    profiler.stop()
    results = profiler.get_results()
    assert "sample_function" in results, "Profiler should record the sample function."
    assert results["sample_function"]["execution_time"] > 0, "Execution time should be recorded."

def test_multiple_function_calls():
    profiler = DynamicProfiler()
    profiler.start()

    @profiler.profile_function
    def sample_function():
        return sum(range(50))

    for _ in range(3):
        sample_function()

    profiler.stop()
    results = profiler.get_results()
    assert results["sample_function"]["execution_count"] == 3, "Execution count should track multiple calls."

def test_clear_results():
    profiler = DynamicProfiler()
    profiler.start()

    @profiler.profile_function
    def sample_function():
        return sum(range(50))

    sample_function()
    profiler.stop()

    profiler.clear_results()
    assert profiler.get_results() == {}, "Results should be cleared after calling clear_results."
