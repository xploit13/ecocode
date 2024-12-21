# profile_example.py
# Extended example script for advanced dynamic profiling in EcoCode

from ecocode.dynamic_profiler import DynamicProfiler

# Define a sample function to profile
def compute_sum():
    total = sum(range(10000))
    return total

# Define another sample function to profile
def compute_factorial():
    result = 1
    for i in range(1, 1000):
        result *= i
    return result

if __name__ == "__main__":
    # Initialize the DynamicProfiler
    profiler = DynamicProfiler()

    # Start profiling
    profiler.start()

    @profiler.profile_function
    def profiled_sum():
        return compute_sum()

    @profiler.profile_function
    def profiled_factorial():
        return compute_factorial()

    print("Running profiled_sum...")
    profiled_sum()

    print("Running profiled_factorial...")
    profiled_factorial()

    # Stop profiling
    profiler.stop()

    # Display the profiling results
    results = profiler.get_results()

    print("Dynamic Profiling Results:")
    for function_name, stats in results.items():
        print(f"Function: {function_name}")
        print(f"Execution Time: {stats['execution_time']:.4f} seconds")
        print(f"Memory Used: {stats['memory_used']} bytes")
        print(f"Execution Count: {stats['execution_count']}")
        print("-" * 40)
