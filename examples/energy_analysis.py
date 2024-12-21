# energy_analysis_example.py
# Extended example script demonstrating advanced energy analysis features in EcoCode

import time
from ecocode.energy_analyzer import EnergyAnalyzer

def example_function_a():
    # A sample function to analyze
    result = sum([i ** 2 for i in range(10000)])
    return result

def example_function_b():
    # Another sample function to analyze
    result = 1
    for i in range(1, 1000):
        result *= i
    return result

if __name__ == "__main__":
    # Initialize the EnergyAnalyzer
    analyzer = EnergyAnalyzer()

    # Start monitoring energy usage
    analyzer.start()

    print("Running example_function_a...")
    start_time = time.time()
    example_function_a()
    analyzer.monitor_energy_usage("example_function_a")
    print(f"Execution Time for example_function_a: {time.time() - start_time:.2f} seconds")

    print("Running example_function_b...")
    start_time = time.time()
    example_function_b()
    analyzer.monitor_energy_usage("example_function_b")
    print(f"Execution Time for example_function_b: {time.time() - start_time:.2f} seconds")

    # Stop monitoring energy usage
    analyzer.stop()

    # Generate a detailed report
    report = analyzer.generate_report()

    print("Energy Analysis Report:")
    for key, value in report.items():
        if key == "details":
            print("Detailed Process Analysis:")
            for detail in value:
                print(detail)
        else:
            print(f"{key}: {value}")
