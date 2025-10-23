import unittest
import re

class TestChartConfig(unittest.TestCase):

    def test_haulage_chart_begins_at_zero(self):
        """
        Tests that the haulage chart's y-axis is configured to start at zero.
        """
        with open('index.html', 'r') as f:
            content = f.read()

        # Isolate the javascript for the createHaulageChart function
        match = re.search(r'function createHaulageChart\(.*?\)\s*\{(.+?)\s*\}\s*\n', content, re.DOTALL)
        self.assertIsNotNone(match, "Could not find the createHaulageChart function")

        function_body = match.group(1)

        # This will fail because the current config is "beginAtZero: false"
        self.assertIn('beginAtZero: true', function_body, "The haulage chart's y-axis does not begin at zero within the createHaulageChart function.")

if __name__ == '__main__':
    unittest.main()
