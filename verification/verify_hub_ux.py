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

        # Scroll to the Hub section
        hub_section = page.locator("#hub")
        hub_section.scroll_into_view_if_needed()

        # Wait for the diagram to be generated
        page.wait_for_selector(".hub-node")

        # Check if nodes have tabindex="0" and aria-label
        nodes = page.locator(".hub-node")
        count = nodes.count()
        print(f"Found {count} hub nodes")

        if count == 0:
            print("❌ No hub nodes found")
            exit(1)

        # Check the center node
        center_node = page.locator("#hub-center")
        if center_node.get_attribute("tabindex") != "0":
            print("❌ Center node missing tabindex='0'")
        else:
            print("✅ Center node has tabindex='0'")

        if not center_node.get_attribute("aria-label"):
            print("❌ Center node missing aria-label")
        else:
            print(f"✅ Center node has aria-label: {center_node.get_attribute('aria-label')}")

        # Check pillar nodes
        for i in range(count):
            node = nodes.nth(i)
            # Skip checking text content if it's purely checking attributes

            tabindex = node.get_attribute("tabindex")
            aria_label = node.get_attribute("aria-label")
            role = node.get_attribute("role")

            if tabindex == "0":
                print(f"✅ Node {i} has tabindex='0'")
            else:
                print(f"❌ Node {i} missing tabindex='0'")

            if aria_label:
                print(f"✅ Node {i} has aria-label: {aria_label}")
            else:
                print(f"❌ Node {i} missing aria-label")

            if role == "img":
                print(f"✅ Node {i} has role='img'")
            else:
                print(f"❌ Node {i} missing or incorrect role (expected 'img', got '{role}')")

        # Test Focus State
        # We try to focus the first generated pillar node (index 1 usually, index 0 is center)
        # Actually in DOM, center is #hub-center, others are appended.
        # nodes locator matches all .hub-node.
        # #hub-center is a .hub-node.

        if count > 1:
            pillar_node = nodes.nth(1)
            pillar_node.focus()

            # Check if it has the active styles
            hub_text = pillar_node.locator(".hub-text")

            expect(pillar_node).to_be_focused()
            print("✅ Node focusable")

            # Get background color
            bg_color = hub_text.evaluate("el => getComputedStyle(el).backgroundColor")
            print(f"Focused Background Color: {bg_color}")

            if "rgb(191, 255, 0)" in bg_color:
                print("✅ Focus style applied correctly")
            else:
                print(f"⚠️ Focus style might not be applied (got {bg_color}, expected rgb(191, 255, 0))")

            # Take Screenshot
            screenshot_path = os.path.join(base_dir, "verification/hub_focus_state.png")
            hub_section.screenshot(path=screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    verify_hub_ux()
