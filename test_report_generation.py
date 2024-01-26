import unittest
import pandas as pd
import os
from data_processing import read_csv_data
from html_generation import dataframe_to_html_table
from chart_generation import create_comparison_bar_chart, create_line_chart
from report import generate_report


class TestReportGenerator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base_path = os.path.dirname(os.path.abspath(__file__))

    def test_read_csv_data_valid_header(self):
        df = read_csv_data(self.base_path, '00', 'header_table', 'data.csv')
        self.assertIsInstance(df, pd.DataFrame)

    def test_read_csv_data_valid_overview(self):
        df = read_csv_data(self.base_path, '00', 'overview_table', 'data.csv')
        self.assertIsInstance(df, pd.DataFrame)

    def test_read_csv_data_invalid(self):
        df = read_csv_data(self.base_path, '00', 'header_table', 'nonexistent.csv')
        self.assertIsNone(df)

    def test_dataframe_to_html_table(self):
        df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        html_table = dataframe_to_html_table(df)
        self.assertIn('<table', html_table)

    def test_none_dataframe_to_html(self):
        html_table = dataframe_to_html_table(None)
        self.assertEqual(html_table, "<p>No data available</p>")

    def test_create_comparison_bar_chart(self):
        df = pd.DataFrame({'x': [1, 2], 'y': [3, 4], 'series': ['A', 'B']})
        chart_html = create_comparison_bar_chart(df, 'x', 'y', 'series', 'Title', 'Y Title')
        self.assertIn('plotly', chart_html)

    def test_create_line_chart(self):
        df = pd.DataFrame({'x': [1, 2], 'y': [3, 4], 'series': ['A', 'B']})
        chart_html = create_line_chart(df, 'x', 'y', 'series', 'Title')
        self.assertIn('plotly', chart_html)

class TestIntegration(unittest.TestCase):
    def test_report_generation(self):
        html_report = generate_report()

        # Basic HTML structure checks
        self.assertIn('<html>', html_report)
        self.assertIn('</html>', html_report)
        self.assertIn('<head>', html_report)
        self.assertIn('</head>', html_report)
        self.assertIn('<body>', html_report)
        self.assertIn('</body>', html_report)

        # Title in the head section
        self.assertIn('<title>Department Data Report</title>', html_report)

        # Check for navigation links
        self.assertIn('<nav class=\'nav-tabs\'>', html_report)

        # Check for section titles
        self.assertIn('Entire Organization', html_report)
        self.assertIn('Sales', html_report)
        self.assertIn('Marketing', html_report)
        self.assertIn('Customer Service', html_report)

        # Check for the presence of specific sections
        self.assertIn('<div class=\'section\' id=\'section1\'>', html_report)  # Entire Organization
        self.assertIn('<div class=\'section\' id=\'section2\'>', html_report)  # Sales
        self.assertIn('<div class=\'section\' id=\'section3\'>', html_report)  # Marketing
        self.assertIn('<div class=\'section\' id=\'section4\'>', html_report)  # Customer Service

        # Check for tables and charts
        self.assertIn('<table', html_report)  # Check for tables
        self.assertIn('plotly', html_report)  # Check for Plotly charts

if __name__ == '__main__':
    unittest.main()

