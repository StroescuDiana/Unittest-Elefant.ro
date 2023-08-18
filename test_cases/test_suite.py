import unittest

import HtmlTestRunner

from test_cases.test_1_2_3_4 import TestsFrom1To4
from test_cases.test_5_6 import TestsFrom5To6


class TestSuite(unittest.TestCase):

    def tests_suite(self):
        tests_suite = unittest.TestSuite()
        tests_suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestsFrom1To4),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestsFrom5To6)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="Elefant.ro tests",
            report_name="Test Results",
        )
        runner.run(tests_suite)