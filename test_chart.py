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
        start_pattern = r'function createHaulageChart\(.*?\)\s*\{'
        match = re.search(start_pattern, content)
        self.assertIsNotNone(match, "Could not find the start of createHaulageChart function")

        start_index = match.end() - 1 # Points to the opening '{'

        # Extract the full function body by balancing braces
        open_braces = 0
        end_index = -1

        for i, char in enumerate(content[start_index:], start=start_index):
            if char == '{':
                open_braces += 1
            elif char == '}':
                open_braces -= 1

            if open_braces == 0:
                end_index = i
                break

        self.assertNotEqual(end_index, -1, "Could not find the closing brace for createHaulageChart function")

        # content inside the braces
        function_body = content[start_index+1:end_index]

        self.assertIn('beginAtZero: true', function_body, "The haulage chart's y-axis does not begin at zero within the createHaulageChart function.")

if __name__ == '__main__':
    unittest.main()
