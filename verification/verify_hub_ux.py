from playwright.sync_api import sync_playwright, expect
import os
import time

def verify_hub_ux():
    base_dir = os.getcwd()
    html_file = os.path.join(base_dir, "index.html")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        print(f"Opening {html_file}")
        page.goto(f"file://{html_file}")

        # Wait for hub diagram to generate
        page.wait_for_selector("#hub-center")
        page.wait_for_selector(".hub-node")

        # Scroll to section
        page.locator("#hub").scroll_into_view_if_needed()
        time.sleep(0.5)

        # Get all nodes
        nodes = page.locator(".hub-node").all()
        print(f"Found {len(nodes)} hub nodes")

        if len(nodes) == 0:
            raise Exception("No hub nodes found")

        # Verify accessibility attributes
        for i, node in enumerate(nodes):
            print(f"Checking node {i}")

            # Check tabindex
            tabindex = node.get_attribute("tabindex")
            print(f"  tabindex: {tabindex}")
            if tabindex != "0":
                print("  FAIL: tabindex is missing or incorrect")

            # Check role
            role = node.get_attribute("role")
            print(f"  role: {role}")
            if role != "img":
                 print("  FAIL: role is missing or incorrect")

            # Check aria-label
            aria_label = node.get_attribute("aria-label")
            print(f"  aria-label: {aria_label}")
            if not aria_label:
                 print("  FAIL: aria-label is missing")

        # Check interaction (focus state)
        # We pick the first pillar node (not center) to test hover/focus style
        # The center node is usually first or last depending on DOM order.
        # pillars are appended to container. Center is re-inserted.
        # Let's just try to focus the second node (index 1) which should be a pillar
        target_node = nodes[1]
        target_node.focus()

        # Check if it is focused
        is_focused = target_node.evaluate("el => document.activeElement === el")
        print(f"Node 1 is focused: {is_focused}")

        # Take screenshot of the hub
        screenshot_path = os.path.join(base_dir, "verification/hub_verification.png")
        page.locator("#hub-diagram").screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        # Assertions
        for node in nodes:
            expect(node).to_have_attribute("tabindex", "0")
            expect(node).to_have_attribute("role", "img")
            expect(node).to_have_attribute("aria-label", re.compile(r".+"))

        browser.close()

if __name__ == "__main__":
    import re
    verify_hub_ux()
