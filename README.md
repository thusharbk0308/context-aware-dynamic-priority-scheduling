# CADPS - CPU Scheduling Simulator

## Overview

CADPS (CPU Scheduling Simulator with Dynamic Priority System) is a web-based application that simulates and compares different CPU scheduling algorithms. It provides a comprehensive analysis of process scheduling using multiple algorithms including FCFS, SJF, Priority Scheduling, Round Robin, and an advanced CADPS algorithm.

## Project Structure

```
CADPS/
├── app.py                          # Flask application entry point
├── test_simulations.py             # Unit tests for scheduling algorithms
├── README.md/                      # Documentation (this file)
├── report_support/
│   └── assumptions.txt             # Project assumptions and constraints
├── scheduler/                      # Core scheduling module
│   ├── __init__.py
│   ├── models.py                   # Process model definition
│   ├── cadps.py                    # CADPS algorithm implementation
│   ├── fcfs.py                     # First Come First Served algorithm
│   ├── sjf.py                      # Shortest Job First algorithm
│   ├── priority.py                 # Priority Scheduling algorithm
│   ├── round_robin.py              # Round Robin algorithm
│   ├── metrics.py                  # Metrics calculation utilities
│   └── __pycache__/
├── static/                         # Static web assets
│   ├── style.css                   # Web interface styling
│   └── charts.js                   # Chart visualization library
└── templates/                      # HTML templates
    └── index.html                  # Main web interface
```

## Features

### Supported Scheduling Algorithms

1. **FCFS (First Come First Served)**
   - Processes are executed in the order they arrive
   - Simple but can lead to long wait times

2. **SJF (Shortest Job First)**
   - Processes with shortest burst time are executed first
   - Minimizes average waiting time

3. **Priority Scheduling**
   - Processes are scheduled based on assigned priority
   - Higher priority processes execute first

4. **Round Robin**
   - Each process gets a fixed time quantum
   - Good for time-sharing systems

5. **CADPS (Custom Algorithm with Dynamic Priority System)**
   - Advanced algorithm considering multiple factors:
     - Base priority value
     - Waiting time score
     - Burst time estimation
     - I/O bound process detection
     - Foreground/background process classification
     - Energy consumption estimation

### Key Features

- **Web-Based Interface**: User-friendly Flask web application
- **Real-time Simulation**: Run simulations with custom process parameters
- **Comparative Analysis**: Compare performance across all algorithms simultaneously
- **Metrics Calculation**: Detailed metrics including:
  - Turnaround time
  - Waiting time
  - Response time
  - Completion time
  - Starvation detection
- **Process Classification**: Support for I/O bound and foreground/background processes
- **Energy Estimation**: CPU usage and energy consumption estimation

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Flask
- pip (Python package manager)

### Installation

1. Clone or extract the project to your local machine
2. Navigate to the project directory:
   ```bash
   cd CADPS
   ```
3. Install required dependencies:
   ```bash
   pip install flask
   ```

### Running the Application

1. Start the Flask development server:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```
3. Enter process parameters (arrival time, burst time, priority, I/O bound, foreground)
4. Click simulate to compare all algorithms

## Process Parameters

When creating a process for simulation, you need to provide:

- **Arrival Time**: Time when the process arrives in the ready queue
- **Burst Time**: CPU time required to complete the process
- **Priority**: Priority level (lower values = higher priority, typical range: 1-5)
- **I/O Bound**: Whether the process performs I/O operations
- **Foreground**: Whether the process runs in foreground or background

## Algorithm Comparison

The simulator calculates the following metrics for each algorithm:

| Metric | Description |
|--------|-------------|
| **Turnaround Time** | Completion time - Arrival time |
| **Waiting Time** | Time spent waiting in ready queue |
| **Response Time** | Time from arrival to first execution |
| **Completion Time** | Time when process finishes execution |
| **Starvation** | Whether process was starved (never executed) |

## CADPS Algorithm Details

The CADPS algorithm implements a dynamic priority system that considers:

```
Priority Value = (Base Priority × 2) + Waiting Score + Burst Score 
                 + IO Boost + Foreground Boost - Energy Penalty

Where:
- Waiting Score: min(waiting_time, 5) to prevent starvation
- Burst Score: min((1/remaining_burst) × 4, 2) - favors shorter jobs
- IO Boost: +3 for I/O bound processes
- Foreground Boost: +3 for foreground processes
- Energy Penalty: burst_time × 0.2
```

## Testing

Run the test suite to verify algorithm implementations:

```bash
python test_simulations.py
```

## File Descriptions

### Core Files

- **app.py**: Flask application with routing and form handling
- **models.py**: `Process` class defining process attributes and metrics
- **metrics.py**: Functions to calculate scheduling metrics
- **cadps.py**: CADPS algorithm implementation with dynamic priority calculation

### Algorithm Files

- **fcfs.py**: FCFS algorithm implementation
- **sjf.py**: SJF algorithm implementation
- **priority.py**: Priority scheduling implementation
- **round_robin.py**: Round Robin implementation

### Web Files

- **index.html**: Main web interface with process input form
- **style.css**: Styling for the web interface
- **charts.js**: Charting library for visualization

## Assumptions

See [report_support/assumptions.txt](report_support/assumptions.txt) for detailed project assumptions and constraints.

## Performance Characteristics

Different algorithms perform differently depending on the workload:

- **FCFS**: Good for batch processing, poor response time
- **SJF**: Optimal average waiting time, requires knowing burst time in advance
- **Priority**: Flexible but prone to starvation without aging
- **Round Robin**: Fair CPU allocation, good response time
- **CADPS**: Balanced approach considering multiple factors for mixed workloads

## Future Enhancements

- Multi-core processor simulation
- Preemption support for all algorithms
- Gantt chart visualization
- Custom time quantum for Round Robin
- Export results to CSV/JSON
- Advanced visualization and analytics

## License

This project is for educational purposes.

## Author

Created as a CPU Scheduling Simulation Project

## Support

For issues or questions, please refer to the code comments and test files for examples of how to use the simulator.
