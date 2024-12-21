# energy_analyzer.py
# Extended implementation for analyzing energy usage in EcoCode

import random
import time


class EnergyAnalyzer:

    def __init__(self):
        self.energy_data = []
        self.is_active = False

    def start(self):
        """
        Start the energy analysis process.
        """
        self.is_active = True
        self.energy_data = []
        print("Energy analysis started.")

    def stop(self):
        """
        Stop the energy analysis process.
        """
        self.is_active = False
        print("Energy analysis stopped.")

    def monitor_energy_usage(self, process_name):
        """
        Simulate monitoring energy usage for a process.

        Args:
            process_name (str): Name of the process to monitor.
        """
        if not self.is_active:
            raise RuntimeError(
                "Energy analysis must be started before monitoring.")

        simulated_usage = random.uniform(
            10.0, 100.0)  # Simulate energy usage in joules
        timestamp = time.time()
        self.energy_data.append({
            "process": process_name,
            "energy_usage": simulated_usage,
            "timestamp": timestamp
        })
        print(
            f"Recorded energy usage for {process_name}: {simulated_usage:.2f} J"
        )

    def generate_report(self):
        """
        Generate a detailed energy analysis report.

        Returns:
            dict: A summary of energy usage data.
        """
        if not self.energy_data:
            return {"message": "No energy data recorded."}

        total_energy = sum(entry["energy_usage"] for entry in self.energy_data)
        average_energy = total_energy / len(self.energy_data)
        report = {
            "total_energy_usage": f"{total_energy:.2f} J",
            "average_energy_usage": f"{average_energy:.2f} J",
            "process_count": len(self.energy_data),
            "details": self.energy_data
        }
        return report


# Example usage
if __name__ == "__main__":
    analyzer = EnergyAnalyzer()
    analyzer.start()

    analyzer.monitor_energy_usage("Process A")
    time.sleep(1)
    analyzer.monitor_energy_usage("Process B")
    time.sleep(1)
    analyzer.monitor_energy_usage("Process C")

    analyzer.stop()
    report = analyzer.generate_report()
    print("Energy Analysis Report:", report)
