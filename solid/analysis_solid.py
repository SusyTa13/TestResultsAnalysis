from file_logger import FileLogger
from test_reporter import TestReporter


def main():
    json_file = 'test_results.json'
    logger = FileLogger('error_log.txt')
    reporter = TestReporter(json_file, logger=logger)
    reporter.load_data()
    metrics = reporter.process_metrics()
    reporter.export_to_csv(metrics)


if __name__ == "__main__":
    main()
