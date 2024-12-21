# dynamic_profiler.py
# Implements dynamic function profiling for EcoCode

import time

class DynamicProfiler:
    def __init__(self):
        self.results = {}

    def start_profiling(self, func_name):
        self.results[func_name] = {"start_time": time.time(), "energy_usage": 0}

    def stop_profiling(self, func_name):
        end_time = time.time()
        self.results[func_name]["execution_time"] = end_time - self.results[func_name]["start_time"]

    def get_results(self):
        return self.results
