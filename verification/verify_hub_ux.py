from playwright.sync_api import sync_playwright, expect
import os

def verify_hub_ux():
    base_dir = os.getcwd()
    html_file = os.path.join(base_dir, "index.html")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        print(f"Opening {html_file}")
        page.goto(f"file://{html_file}")

        # Wait for JS to run and create diagram
        page.wait_for_selector("#hub-diagram .hub-node", state="visible")

        # Scroll to Hub
        hub_section = page.locator("#hub")
        hub_section.scroll_into_view_if_needed()
        page.wait_for_timeout(500)

        # Check Center Hub
        center_hub = page.locator("#hub-center")
        expect(center_hub).to_be_visible()
        expect(center_hub).to_have_attribute("tabindex", "0")
        expect(center_hub).to_have_attribute("role", "img")
        expect(center_hub).to_have_attribute("aria-label", "Smart Hub Core")

        # Check focus on center hub
        center_hub.focus()
        expect(center_hub).to_be_focused()

        # Check Pillar Nodes
        pillars = ["WORKFORCE", "SAFETY", "EARTHWORKS", "AERIAL", "HAULAGE", "REPORTING"]

        for pillar in pillars:
            # We can find them by aria-label now!
            print(f"Checking pillar: {pillar}")
            node = page.locator(f".hub-node[aria-label='{pillar} Pillar']")
            expect(node).to_be_visible()
            expect(node).to_have_attribute("tabindex", "0")
            expect(node).to_have_attribute("role", "img")

            # Test Focus
            node.focus()
            expect(node).to_be_focused()

            # Take a screenshot of the hub section with the first node focused
            if pillar == pillars[0]:
                 screenshot_path = os.path.join(base_dir, "verification/hub_focus_state.png")
                 page.locator("#hub").screenshot(path=screenshot_path)
                 print(f"Screenshot saved to {screenshot_path}")

        print("All hub nodes verified successfully.")
        browser.close()

if __name__ == "__main__":
    verify_hub_ux()
