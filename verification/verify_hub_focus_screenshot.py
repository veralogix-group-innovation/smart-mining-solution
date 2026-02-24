from playwright.sync_api import sync_playwright
import os
import sys

def verify_hub_visual():
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch()
            page = browser.new_page()
            # Set viewport to ensure hub is visible
            page.set_viewport_size({"width": 1280, "height": 800})

            # Load the local index.html file
            file_path = os.path.abspath('index.html')
            page.goto(f"file://{file_path}")

            # Scroll to hub diagram
            hub = page.locator("#hub-diagram")
            hub.scroll_into_view_if_needed()

            # Wait for nodes
            page.wait_for_selector(".hub-node", timeout=5000)

            # Focus on the first pillar node
            # We use keyboard navigation to ensure :focus-visible triggers

            # Focus on the element before, or just focus the center and tab
            center_node = page.locator("#hub-center")
            center_node.focus()
            page.wait_for_timeout(200)

            # Press tab to move to first pillar (Workforce)
            page.keyboard.press("Tab")

            # Check what is focused
            focused_label = page.evaluate("document.activeElement.getAttribute('aria-label')")
            print(f"Focused element: {focused_label}")

            # Check computed style
            bg_color = page.evaluate("""() => {
                const node = document.activeElement;
                const text = node.querySelector('.hub-text');
                return window.getComputedStyle(text).backgroundColor;
            }""")
            print(f"Background color: {bg_color}")

            # Wait a bit for transition
            page.wait_for_timeout(2000)

            # Take screenshot of the hub area
            screenshot_path = "verification/hub_focus_state.png"
            page.screenshot(path=screenshot_path, clip={
                "x": 0,
                "y": 0,
                "width": 1280,
                "height": 1500 # Capture enough vertical space
            }, full_page=True) # or just use full_page=True

            # Better: screenshot just the hub section
            hub_section = page.locator("#hub")
            hub_section.screenshot(path=screenshot_path)

            print(f"Screenshot saved to {screenshot_path}")
            browser.close()

        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)

if __name__ == "__main__":
    verify_hub_visual()
