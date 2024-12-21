# test_dynamic_profiler.py
# Unit tests for dynamic_profiler.py

from ecocode.dynamic_profiler import DynamicProfiler

def test_profiler_start_stop():
    profiler = DynamicProfiler()
    profiler.start()
    assert profiler.get_results() == {}
    profiler.stop()
