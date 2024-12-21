# energy_analysis_example.py
# Example script demonstrating the use of energy analysis features in EcoCode

from ecocode.energy_analyzer import EnergyAnalyzer

def example_function():
    # A sample function to analyze
    result = sum([i ** 2 for i in range(10000)])
    return result

if __name__ == "__main__":
    # Initialize the EnergyAnalyzer
    analyzer = EnergyAnalyzer()

    # Start monitoring energy usage
    analyzer.start()

    print("Running the example function...")
    example_function()

    # Stop monitoring energy usage
    analyzer.stop()

    # Generate a report
    report = analyzer.generate_report()

    print("Energy Analysis Report:")
    print(report)
