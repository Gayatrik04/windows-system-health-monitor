# Windows System Health Monitor

A Python-based system monitoring utility that collects CPU, memory, and disk usage, records timestamped metrics in CSV format, identifies high resource usage using configurable thresholds, and summarizes system activity.

This project demonstrates Python programming, basic system telemetry collection, CSV file handling, exception handling, command-line arguments, and unit testing.

## Features

- Monitors CPU, memory, and disk usage.
- Records timestamped measurements in a CSV file.
- Flags resource usage at or above the configured 80% threshold.
- Calculates average and maximum usage.
- Supports configurable sampling intervals and monitoring duration.
- Handles invalid usage values and common runtime errors.
- Includes automated unit tests using Python's `unittest` framework.

## Technologies Used

- Python
- psutil
- CSV
- unittest
- Visual Studio Code

## Project Structure

```text
Windows-System-Health-Monitor/
├── monitor.py
├── requirements.txt
├── README.md
├── .gitignore
├── tests/
│   └── test_monitor.py
└── reports/
    └── system_metrics.csv  # Generated when the monitor runs
```

The `reports/` directory and CSV file are generated during execution and do not need to be committed to GitHub.

## Requirements

- Python 3.10 or later
- Windows 10 or Windows 11
- The `psutil` Python package

Other operating systems may also work, but this project is primarily documented for Windows.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Gayatrik04/windows-system-health-monitor.git
cd windows-system-health-monitor
```

Replace the repository URL if you choose a different repository name.

### 2. Create a virtual environment

```powershell
py -m venv .venv
```

### 3. Activate the environment

For PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If activation is blocked, use Command Prompt:

```bat
.venv\Scripts\activate.bat
```

### 4. Install dependencies

```powershell
py -m pip install -r requirements.txt
```

## Usage

### Run the monitor for 30 seconds

```powershell
py monitor.py --interval 2 --duration 30
```

This runs the monitor for 30 seconds with a 2-second sampling interval.

The output CSV file is saved to:

```text
reports/system_metrics.csv
```

### Run the monitor for 60 seconds

```powershell
py monitor.py --interval 2 --duration 60 --output reports/run2.csv
```

This saves the measurements to a separate CSV file.

## Sample Run Results

The following results were recorded during an actual 30-second run on one system.

| Metric | Average | Maximum |
|---|---:|---:|
| CPU usage | 8.0% | 20.9% |
| Memory usage | 41.0% | 41.2% |
| Disk usage | 30.8% | 30.8% |

- Monitoring duration: 30 seconds
- Sampling interval: 2 seconds
- Samples saved: 15
- CSV logging: Successful

These values are specific to that run. Results will vary depending on system activity and available resources.

## Sample CSV Output

The generated CSV contains timestamped resource measurements. An example row from a recorded run is:

```csv
timestamp,cpu_percent,memory_percent,disk_percent
2026-10-20T00:02:13+05:30,5.3,41.0,30.8
```

The timestamp and metric values above are an example from one recorded sample. New runs generate different values.

## Unit Testing

The project uses Python's built-in `unittest` framework.

Run the tests with:

```powershell
py -m unittest discover -s tests -v
```

### Test Results

All five tests passed during the recorded test run.

| Test case | Result |
|---|---|
| Invalid negative value | Passed |
| Invalid value above 100 | Passed |
| Maximum usage is high | Passed |
| Normal usage | Passed |
| Threshold usage is high | Passed |

```text
Ran 5 tests in 0.001s

OK
```

## What I Learned

- Collecting basic system resource metrics with Python.
- Recording timestamped measurements in CSV files.
- Using command-line arguments to configure program execution.
- Applying threshold-based checks to resource usage.
- Handling invalid inputs and runtime errors.
- Writing and running unit tests to verify program behavior.

## Limitations

- This is a basic user-space monitoring utility, not a Windows diagnostic or performance optimization tool.
- The 80% threshold is a configurable starting point, not a universal definition of poor performance.
- Disk usage reflects the configured disk path.
- The tool does not identify which individual process causes high resource usage.
- It does not analyze Event Tracing for Windows (ETW) traces, inspect Windows internals, or measure battery consumption.

## Future Improvements

- Add process-level CPU and memory monitoring.
- Export additional summary reports.
- Allow thresholds to be configured through command-line arguments.
- Add more unit tests for error conditions and command-line options.
- Add charts to visualize resource usage over time.

## Author

**Gayatri Sunil Kasbekar**

- GitHub: [Gayatrik04](https://github.com/Gayatrik04)

---

