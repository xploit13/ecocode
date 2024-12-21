# profile_example.py
# Example script for profiling software dynamically using EcoCode

from ecocode.dynamic_profiler import DynamicProfiler

# Define a sample function to profile
def sample_function():
    total = 0
    for i in range(10000):
        total += i ** 2
    return total

if __name__ == "__main__":
    # Initialize the DynamicProfiler
    profiler = DynamicProfiler()

    # Start profiling
    profiler.start()

    print("Executing the sample function...")
    sample_function()

    # Stop profiling
    profiler.stop()

    # Display the profiling results
    results = profiler.get_results()

    print("Profiling Results:")
    for function_name, stats in results.items():
        print(f"Function: {function_name}")
        print(f"Execution Time: {stats['execution_time']} ms")
        print(f"Energy Consumption: {stats['energy_consumption']} J")
