from playwright.sync_api import sync_playwright, expect
import os
import time

def verify_hub():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use a larger viewport to ensure elements fit
        context = browser.new_context(viewport={"width": 1280, "height": 1024})
        page = context.new_page()

        cwd = os.getcwd()
        page.goto(f"file://{cwd}/index.html")
        page.wait_for_selector(".hub-node")

        # Scroll to the hub section
        hub_section = page.locator("#hub-diagram")
        hub_section.scroll_into_view_if_needed()

        # Give a moment for animations/scrolling to settle
        time.sleep(0.5)

        # Focus on the first node (center)
        nodes = page.query_selector_all(".hub-node")
        if not nodes:
            print("No hub nodes found!")
            return

        center_node = nodes[0]
        print("Focusing center node...")
        center_node.focus()

        # Tab to the next one to show movement
        print("Pressing Tab to move focus...")
        page.keyboard.press("Tab")
        time.sleep(0.2) # Allow transition

        # Take a screenshot
        screenshot_path = "verification/hub_focus.png"
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    verify_hub()
