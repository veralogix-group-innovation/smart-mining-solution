from playwright.sync_api import sync_playwright
import os
import sys

def test_hub_ux():
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch()
            page = browser.new_page()
            # Load the local index.html file
            file_path = os.path.abspath('index.html')
            page.goto(f"file://{file_path}")

            print(f"Loading {file_path}")

            # Check if Hub Diagram exists
            hub = page.locator("#hub-diagram")
            if not hub.count():
                print("Hub diagram not found!")
                sys.exit(1)

            # Check if nodes are generated
            # We might need to wait a bit as it's JS generated, but it's on DOMContentLoaded
            try:
                page.wait_for_selector(".hub-node", timeout=5000)
            except:
                print("Timed out waiting for .hub-node elements")
                sys.exit(1)

            nodes = page.locator(".hub-node")
            count = nodes.count()
            print(f"Found {count} hub nodes.")

            # Should be at least 6 pillars + 1 center node = 7
            if count < 7:
                 print(f"Not enough nodes found. Expected at least 7, found {count}.")
                 sys.exit(1)

            # Check attributes
            all_passed = True
            for i in range(count):
                node = nodes.nth(i)
                role = node.get_attribute("role")
                tabindex = node.get_attribute("tabindex")
                label = node.get_attribute("aria-label")

                print(f"Node {i}: role='{role}', tabindex='{tabindex}', label='{label}'")

                if role != "img":
                    print(f"  FAIL: Node {i} role is '{role}', expected 'img'")
                    all_passed = False
                if tabindex != "0":
                    print(f"  FAIL: Node {i} tabindex is '{tabindex}', expected '0'")
                    all_passed = False
                if not label:
                    print(f"  FAIL: Node {i} has no aria-label")
                    all_passed = False

                # Check focus
                node.focus()
                # Check if focused using JS evaluation
                is_focused = page.evaluate("(element) => document.activeElement === element", node.element_handle())
                if not is_focused:
                     print(f"  FAIL: Node {i} could not be focused")
                     all_passed = False
                else:
                    # Optional: Check if focus styles are applied (e.g. background color change)
                    # This is tricky without computed styles, but we assume CSS works if focus works
                    pass

            if all_passed:
                print("SUCCESS: Hub nodes are accessible.")
            else:
                print("FAILURE: Some checks failed.")
                sys.exit(1)

            browser.close()
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)

if __name__ == "__main__":
    test_hub_ux()
