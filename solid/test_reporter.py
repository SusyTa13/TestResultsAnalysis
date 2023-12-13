import json
import csv
from typing import Dict
from iLogger import ILogger


class TestReporter:
    def __init__(self, json_file: str, csv_file: str = 'test_report.csv', logger: ILogger = None):
        self.json_file = json_file
        self.csv_file = csv_file
        self.data = None
        self.logger = logger if logger else ILogger()

    def load_data(self):
        try:
            with open(self.json_file, 'r') as file:
                self.data = json.load(file)
        except Exception as e:
            self.logger.error(f"Error loading data from 'JSON' file: {e}")

    def process_metrics(self) -> Dict[str, float]:
        try:
            total_tests = len(self.data)
            passed_tests = sum(1 for test in self.data if test['status'] == 'pass')
            failed_tests = sum(1 for test in self.data if test['status'] == 'fail')
            execution_times = [test['execution_time'] for test in self.data]
            avg_execution_time = sum(execution_times) / total_tests
            min_execution_time = min(execution_times)
            max_execution_time = max(execution_times)

            return {
                "Total Test Cases": total_tests,
                "Passed Test Cases": passed_tests,
                "Failed Test Cases": failed_tests,
                "Average Execution Time": avg_execution_time,
                "Min Execution Time": min_execution_time,
                "Max Execution Time": max_execution_time
            }
        except Exception as e:
            self.logger.error(f"Error processing metrics: {e}")

    def export_to_csv(self, metrics: Dict[str, float]):
        try:
            with open(self.csv_file, 'w', newline='') as file:
                fieldnames = ['Test Case', 'Status', 'Execution Time', 'Timestamp'] + list(metrics.keys())
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                writer.writeheader()

                for test in self.data:
                    writer.writerow({
                        'Test Case': test['test_case'],
                        'Status': test['status'],
                        'Execution Time': test['execution_time'],
                        'Timestamp': test['timestamp']
                    })
        except Exception as e:
            self.logger.error(f"Error exporting to CSV: {e}")