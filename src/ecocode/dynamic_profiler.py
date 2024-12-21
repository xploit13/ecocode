# dynamic_profiler.py
# Extended implementation for dynamic function profiling in EcoCode

import time
import functools
import tracemalloc

class DynamicProfiler:
    def __init__(self):
        self.results = {}
        self.active = False

    def start(self):
        """
        Start the profiler.
        """
        self.active = True
        tracemalloc.start()
        print("Profiler started.")

    def stop(self):
        """
        Stop the profiler.
        """
        self.active = False
        tracemalloc.stop()
        print("Profiler stopped.")

    def profile_function(self, func):
        """
        Decorator to profile a specific function.

        Args:
            func (callable): The function to profile.

        Returns:
            callable: The wrapped function with profiling enabled.
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not self.active:
                raise RuntimeError("Profiler must be started before profiling functions.")
            
            func_name = func.__name__
            self.results[func_name] = {
                "start_time": time.time(),
                "memory_start": tracemalloc.get_traced_memory()[0],
                "execution_count": self.results.get(func_name, {}).get("execution_count", 0) + 1
            }

            result = func(*args, **kwargs)

            memory_end = tracemalloc.get_traced_memory()[0]
            end_time = time.time()

            self.results[func_name].update({
                "end_time": end_time,
                "execution_time": end_time - self.results[func_name]["start_time"],
                "memory_end": memory_end,
                "memory_used": memory_end - self.results[func_name]["memory_start"]
            })

            return result

        return wrapper

    def get_results(self):
        """
        Retrieve profiling results.
        """
        return self.results

    def clear_results(self):
        """
        Clear all recorded profiling results.
        """
        self.results = {}
