"""Collect basic Windows system-health metrics and write a CSV report."""
import argparse
import csv
import logging
import time
from datetime import datetime
from pathlib import Path

import psutil

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def classify_usage(value, warning_threshold=80.0):
    """Return a simple status label for a percentage metric."""
    if not isinstance(value, (int, float)) or not 0 <= value <= 100:
        raise ValueError("Usage must be a number between 0 and 100.")
    return "HIGH" if value >= warning_threshold else "NORMAL"


def collect_metrics():
    """Collect one sample of CPU, memory, and disk usage."""
    disk_path = Path.cwd().anchor or "/"
    disk = psutil.disk_usage(disk_path)
    memory = psutil.virtual_memory()
    return {
        "timestamp": datetime.now().astimezone().isoformat(timespec="seconds"),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": float(memory.percent),
        "disk_percent": float(disk.percent),
    }


def write_sample(writer, sample):
    """Write a single sample to an open CSV writer."""
    writer.writerow(sample)


def run_monitor(interval, duration, output_file):
    if interval < 1:
        raise ValueError("Interval must be at least 1 second.")
    if duration < 1:
        raise ValueError("Duration must be at least 1 second.")

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fields = ["timestamp", "cpu_percent", "memory_percent", "disk_percent"]
    samples = []

    logging.info("Monitoring for %s seconds; output: %s", duration, output_path)
    end_time = time.monotonic() + duration

    try:
        with output_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            while time.monotonic() < end_time:
                sample = collect_metrics()
                write_sample(writer, sample)
                handle.flush()
                samples.append(sample)

                for metric in ("cpu_percent", "memory_percent", "disk_percent"):
                    value = float(sample[metric])
                    status = classify_usage(value)
                    if status == "HIGH":
                        logging.warning("%s usage is high: %.1f%%", metric, value)

                time.sleep(max(0, min(interval - 1, end_time - time.monotonic())))
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
    except (OSError, psutil.Error) as exc:
        logging.error("Could not complete monitoring: %s", exc)
        raise

    if samples:
        print("\nSummary")
        for metric in ("cpu_percent", "memory_percent", "disk_percent"):
            values = [float(row[metric]) for row in samples]
            print(f"{metric}: average={sum(values)/len(values):.1f}%  max={max(values):.1f}%")
        print(f"Samples saved: {len(samples)}")
        print(f"CSV report: {output_path.resolve()}")
    else:
        print("No samples collected.")


def main():
    parser = argparse.ArgumentParser(description="Monitor CPU, memory, and disk usage.")
    parser.add_argument("--interval", type=int, default=2, help="Seconds between samples (minimum 1).")
    parser.add_argument("--duration", type=int, default=30, help="Total monitoring duration in seconds.")
    parser.add_argument("--output", default="reports/system_metrics.csv", help="CSV output path.")
    args = parser.parse_args()
    run_monitor(args.interval, args.duration, args.output)


if __name__ == "__main__":
    main()
