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
        # Using a more robust regex that counts braces would be ideal, but for this specific file,
        # we can look for the start of the function and the start of the next function/block or just verify content within the file.
        # Given the simplicity, we will check if 'beginAtZero: true' exists in the file, which is a reasonable proxy for this specific check
        # provided we are confident it's in the right place (which manual inspection confirmed).
        # A more specific check can search for the "createHaulageChart" string and then "beginAtZero: true" after it.

        start_index = content.find('function createHaulageChart')
        self.assertNotEqual(start_index, -1, "Could not find the createHaulageChart function")

        # Approximate end of function by finding the start of the next function or script block end
        # In index.html, the next function is createSafetyChart
        end_index = content.find('function createSafetyChart', start_index)
        if end_index == -1:
             end_index = content.find('</script>', start_index)

        function_body = content[start_index:end_index]

        # This will fail because the current config is "beginAtZero: false"
        self.assertIn('beginAtZero: true', function_body, "The haulage chart's y-axis does not begin at zero within the createHaulageChart function.")

if __name__ == '__main__':
    unittest.main()
