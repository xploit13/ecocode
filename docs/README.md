# EcoCode

EcoCode is an open-source tool for profiling, analyzing, and optimizing the energy impact of software. It empowers developers to create sustainable and efficient code by providing insights into energy consumption, performance bottlenecks, and eco-friendly practices.

## Features

- **Dynamic Function Profiling**: Analyze function-level energy usage in real-time.
- **Eco-Score Calculation**: Evaluate the energy efficiency of your code.
- **Detailed Reports**: Generate comprehensive energy impact reports.
- **Extensible Plugins**: Extend functionality with custom plugins.
- **Real-time Monitoring Dashboard**: Monitor processes and energy usage in an interactive UI.

## Installation

### Prerequisites

- Python 3.8 or higher
- Node.js (for the frontend)
- Git

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/xploit13/ecocode.git
   cd ecocode
   ```

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the frontend:

   ```bash
   cd frontend
   npm install
   npm start
   ```

4. Start the backend:

   ```bash
   cd ../src
   python setup.py install
   python -m ecocode
   ```

5. Access the dashboard at [http://localhost:3000](http://localhost:3000).

## Usage

### Profiling a Script

Run the profiler on your Python script:

```bash
python -m ecocode.dynamic_profiler your_script.py
```

### Generating an Eco-Score

Evaluate the energy efficiency of your code:

```python
from ecocode.eco_score import calculate_score

score = calculate_score("path/to/your_script.py")
print(f"Eco-Score: {score}")
```

### Creating a Report

Generate a detailed energy impact report:

```python
from ecocode.report_generator import generate_report

generate_report("path/to/your_script.py", output_file="report.pdf")
```

## Contributing

We welcome contributions! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

## License

EcoCode is released under the [MIT License](LICENSE).

## Community

- **GitHub**: [https://github.com/xploit13/ecocode](https://github.com/xploit13/ecocode)
- **Contact**: [support@ecocode.org](mailto:support@ecocode.org)

Thank you for supporting sustainable software development with EcoCode!
