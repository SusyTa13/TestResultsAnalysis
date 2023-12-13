import json
import csv
# import datetime from datetime


def process_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    total_tests = len(data)
    passed_tests = sum(1 for test in data if test['status'] == 'pass')
    failed_tests = total_tests - passed_tests
    execution_times = [test['execution_time'] for test in data]
    avg_execution_time = sum(execution_times) / total_tests
    min_execution_time = min(execution_times)
    max_execution_time = max(execution_times)

    metrics = {
        "Total Test Cases": total_tests,
        "Passed Test Cases": passed_tests,
        "Failed Test Cases": failed_tests,
        "Average Execution Time": avg_execution_time,
        "Min Execution Time": min_execution_time,
        "Max Execution Time": max_execution_time
    }

    export_to_csv(data, metrics)


def export_to_csv(data, metrics):
    csv_file = 'test_report.csv'

    with open(csv_file, 'w', newline='') as file:
        columns = ['Test Case', 'Status', 'Execution Time', 'Timestamp']
        writer = csv.DictWriter(file, fieldnames=columns + list(metrics.keys()))
        
        writer.writeheader()
        
        for d in data:
            writer.writerow({
                'Test Case': d['test_case'],
                'Status': d['status'],
                'Execution Time': d['execution_time'],
                'Timestamp': d['timestamp']
            })


if __name__ == "__main__":
    json_file = 'test_results.json'
    process_json(json_file)