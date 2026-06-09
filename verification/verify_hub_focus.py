import os
from playwright.sync_api import sync_playwright, expect

def verify_hub_focus():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load local file
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/index.html")

        # Wait for hub diagram to generate
        # The center node is static in JS but injected via innerHTML
        page.wait_for_selector("#hub-center", state="visible")

        # Find a generated node, e.g., WORKFORCE
        # The text is inside .hub-text
        node = page.locator(".hub-node").filter(has_text="WORKFORCE").first

        # Scroll into view
        node.scroll_into_view_if_needed()

        # Focus the node using keyboard tab is often better for focus-visible
        # But node.focus() should trigger :focus.
        # Our CSS uses .hub-node:focus-visible.
        # Playwright's .focus() triggers focus-visible in recent versions?
        # Let's try pressing Tab until we reach it or just focus it.
        # If we use .focus(), it might trigger :focus but not necessarily :focus-visible depending on browser heuristic.
        # However, we mapped :hover, :focus-visible so it should be fine if we can trigger it.
        # Let's try to force focus-visible by using keyboard.

        # Click on body to reset focus
        page.click("body")

        # Tab to the skip link
        page.keyboard.press("Tab")
        # Tab to Search input
        page.keyboard.press("Tab")
        # Tab to Search button
        page.keyboard.press("Tab")

        # This might take too many tabs.
        # Let's just focus the node and see.
        node.focus()

        # Check if it has focus
        expect(node).to_be_focused()

        # Take screenshot of the diagram
        screenshot_path = "verification/hub_focus.png"
        # Wait a bit for transition
        page.wait_for_timeout(500)

        page.locator("#hub-diagram").screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    verify_hub_focus()
