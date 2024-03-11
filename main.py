from unittest import TestLoader, TestSuite
import HtmlTestRunner
import datetime

from test import hit

if __name__ == "__main__":
    file_name = datetime.datetime.now().strftime("%Y_%m_%d_%H%M_report.html")
    output = open(file_name, "wb")
    loader = TestLoader()
    suite = TestSuite([
                       loader.loadTestsFromTestCase(hit),
                      ])
    runner = HtmlTestRunner.HTMLTestRunner(output='example_suite')
    runner.run(suite)
