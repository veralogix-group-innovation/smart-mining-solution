import unittest
import re

class TestHubAccessibility(unittest.TestCase):

    def test_hub_nodes_accessibility(self):
        with open('index.html', 'r') as f:
            content = f.read()

        # Check for CSS changes
        # Looking for .hub-node:hover, .hub-node:focus-visible or similar structure
        self.assertTrue(re.search(r'\.hub-node:hover,\s*[\.\w:-]*\.hub-node:focus-visible', content),
                        "CSS should include .hub-node:focus-visible selector shared with hover")

        # Check for JS changes in createHubDiagram

        # Check center node attributes in the HTML string
        # We check that the JS code contains the updated HTML string with attributes
        # Since the static HTML doesn't have them, we must ensure we are matching the JS part.

        # We look for the substring in the JS code
        expected_js_snippet = 'id="hub-center" tabindex="0" role="img" aria-label="Smart Hub Central Node"'
        self.assertIn(expected_js_snippet, content, "JS should generate hub-center with accessibility attributes")

        # Check generated nodes
        # We expect code like:
        # node.setAttribute('tabindex', '0');
        # node.setAttribute('role', 'img');
        # node.setAttribute('aria-label', ...);

        self.assertIn("node.setAttribute('tabindex', '0')", content)
        self.assertIn("node.setAttribute('role', 'img')", content)
        # Using regex for aria-label to allow for variable/template string
        self.assertTrue(re.search(r"node\.setAttribute\('aria-label',\s*`\${pillar} Pillar`\)", content) or
                        re.search(r"node\.setAttribute\('aria-label',\s*['\"]\${pillar} Pillar['\"]", content) or
                        re.search(r"node\.setAttribute\('aria-label',\s*`\${pillar} Pillar`", content), # in case of loose match
                        "Should set aria-label on generated nodes")

if __name__ == '__main__':
    unittest.main()
