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

        # Scroll to the Hub section
        hub_section = page.locator("#hub")
        hub_section.scroll_into_view_if_needed()
        page.wait_for_timeout(1000) # Wait for animation/render

        # Locate the Hub Center
        hub_center = page.locator("#hub-center")
        expect(hub_center).to_be_visible()

        # Verify Attributes
        print("Verifying Hub Center attributes...")
        expect(hub_center).to_have_attribute("tabindex", "0")
        expect(hub_center).to_have_attribute("role", "img")
        expect(hub_center).to_have_attribute("aria-label", "Smart Hub Center")

        # Verify Focusability
        print("Verifying Hub Center focus...")
        hub_center.focus()
        expect(hub_center).to_be_focused()

        # Take screenshot of focused center
        screenshot_path_center = os.path.join(base_dir, "verification/hub_center_focus.png")
        # Screenshotting the specific element might clip the scale effect if it overflows,
        # so we might want to screenshot the container or add padding.
        # But simple screenshot is fine for now.
        hub_center.screenshot(path=screenshot_path_center)
        print(f"Screenshot saved to {screenshot_path_center}")

        # Verify Pillars
        # Pillars are generated dynamically, let's find one
        pillar_name = "WORKFORCE"
        pillar_node = page.locator(f".hub-node[aria-label='Smart Hub Pillar: {pillar_name}']")

        print(f"Verifying {pillar_name} pillar...")
        expect(pillar_node).to_be_visible()
        expect(pillar_node).to_have_attribute("tabindex", "0")
        expect(pillar_node).to_have_attribute("role", "img")

        # Focus on the pillar
        pillar_node.focus()
        expect(pillar_node).to_be_focused()

        # Wait for transition
        page.wait_for_timeout(500)

        # Take screenshot of focused pillar
        screenshot_path_pillar = os.path.join(base_dir, "verification/hub_pillar_focus.png")
        pillar_node.screenshot(path=screenshot_path_pillar)
        print(f"Screenshot saved to {screenshot_path_pillar}")

        print("Smart Hub UX Verification Passed!")
        browser.close()

if __name__ == "__main__":
    verify_hub_ux()
