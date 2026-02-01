from playwright.sync_api import sync_playwright, expect
import os
import re

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
        page.wait_for_timeout(500) # Wait for animation/layout

        # Locate the hub nodes
        nodes = page.locator(".hub-node")

        # Wait for nodes to be generated
        page.wait_for_selector(".hub-node")

        count = nodes.count()
        print(f"Found {count} hub nodes")

        outer_node = nodes.nth(1)

        print("Checking attributes...")
        try:
            expect(outer_node).to_have_attribute("tabindex", "0")
            print("✅ tabindex='0' present")
        except Exception as e:
            print(f"❌ tabindex missing or incorrect: {e}")

        try:
            expect(outer_node).to_have_attribute("role", "img")
            print("✅ role='img' present")
        except Exception as e:
            print(f"❌ role missing or incorrect: {e}")

        try:
            # check if it has "Pillar" in it
            expect(outer_node).to_have_attribute("aria-label", re.compile(r".+ Pillar"))
            print("✅ aria-label present")
        except Exception as e:
            print(f"❌ aria-label missing: {e}")

        # Verify Focus Behavior
        print("Testing keyboard focus...")
        try:
            outer_node.focus()
            expect(outer_node).to_be_focused()
            print("✅ Element can be focused via API")

        except Exception as e:
            print(f"❌ Failed to focus element: {e}")

        # Take screenshot of focused state
        screenshot_path = os.path.join(base_dir, "verification/hub_focus_check.png")
        if count > 0:
            try:
                outer_node.focus()
                page.wait_for_timeout(200) # Wait for transition
                page.screenshot(path=screenshot_path)
                print(f"Screenshot saved to {screenshot_path}")
            except:
                print("Could not take screenshot of focused node")

        browser.close()

if __name__ == "__main__":
    verify_hub_ux()
