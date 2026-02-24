from playwright.sync_api import sync_playwright, expect
import os

def verify_hub_accessibility_visual():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # Load the local index.html file
        page.goto(f"file://{os.path.abspath('index.html')}")

        # Wait for the hub diagram to be generated
        page.wait_for_selector("#hub-diagram .hub-node", state="attached")

        # Locate the first hub node (not the center one, one of the pillars)
        # The center one is also a hub-node but has ID hub-center.
        # The generated ones don't have IDs.

        # Let's focus on the "SAFETY" pillar node.
        safety_node = page.get_by_label("SAFETY Pillar")

        # Focus it
        safety_node.focus()

        # Expect it to be focused
        expect(safety_node).to_be_focused()

        # Take a screenshot of the hub diagram area
        hub_diagram = page.locator("#hub-diagram")
        hub_diagram.screenshot(path="verification/hub_focus_state.png")

        print("Screenshot saved to verification/hub_focus_state.png")

        browser.close()

if __name__ == "__main__":
    verify_hub_accessibility_visual()
