import unittest
import re

class TestChartConfig(unittest.TestCase):

    def extract_function_body(self, content, function_name):
        start_pattern = f'function {function_name}'
        start_index = content.find(start_pattern)
        if start_index == -1:
            return None

        # Find the opening brace
        open_brace_index = content.find('{', start_index)
        if open_brace_index == -1:
            return None

        balance = 0
        for i in range(open_brace_index, len(content)):
            char = content[i]
            if char == '{':
                balance += 1
            elif char == '}':
                balance -= 1
                if balance == 0:
                    return content[open_brace_index + 1 : i]
        return None

    def test_haulage_chart_begins_at_zero(self):
        """
        Tests that the haulage chart's y-axis is configured to start at zero.
        """
        with open('index.html', 'r') as f:
            content = f.read()

        function_body = self.extract_function_body(content, 'createHaulageChart')
        self.assertIsNotNone(function_body, "Could not find the createHaulageChart function body")

        # Verify that the haulage chart's y-axis is configured to begin at zero
        self.assertIn('beginAtZero: true', function_body, "The haulage chart's y-axis does not begin at zero within the createHaulageChart function.")

class TestHubAccessibility(unittest.TestCase):
    def extract_function_body(self, content, function_name):
        start_pattern = f'function {function_name}'
        start_index = content.find(start_pattern)
        if start_index == -1:
            return None

        # Find the opening brace
        open_brace_index = content.find('{', start_index)
        if open_brace_index == -1:
            return None

        balance = 0
        for i in range(open_brace_index, len(content)):
            char = content[i]
            if char == '{':
                balance += 1
            elif char == '}':
                balance -= 1
                if balance == 0:
                    return content[open_brace_index + 1 : i]
        return None

    def test_hub_nodes_have_accessibility_attributes(self):
        """
        Tests that the Smart Hub nodes are generated with accessibility attributes.
        """
        with open('index.html', 'r') as f:
            content = f.read()

        function_body = self.extract_function_body(content, 'createHubDiagram')
        self.assertIsNotNone(function_body, "Could not find the createHubDiagram function body")

        # Verify attributes are set
        self.assertIn("node.setAttribute('tabindex', '0')", function_body, "Missing tabindex attribute")
        self.assertIn("node.setAttribute('role', 'img')", function_body, "Missing role attribute")
        self.assertIn("node.setAttribute('aria-label', pillar)", function_body, "Missing aria-label attribute")

    def test_hub_node_css_focus(self):
        """
        Tests that CSS includes focus styles for hub nodes.
        """
        with open('index.html', 'r') as f:
            content = f.read()

        # Check for focus selector on hub-node
        self.assertIn(".hub-node:hover, .hub-node:focus", content, "CSS missing focus selector for hub-node wrapper")

        # Check for focus selector on hub-text
        self.assertIn(".hub-node:hover .hub-text, .hub-node:focus .hub-text", content, "CSS missing focus selector for hub-text")

if __name__ == '__main__':
    unittest.main()
