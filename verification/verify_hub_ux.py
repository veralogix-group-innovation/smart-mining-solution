from playwright.sync_api import sync_playwright, expect
import os

def verify_hub_ux():
    base_dir = os.getcwd()
    file_path = os.path.join(base_dir, "index.html")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        print(f"Checking {file_path}...")
        page.goto(f"file://{file_path}")

        # Wait for the diagram to be generated
        page.wait_for_selector("#hub-diagram .hub-node", state="visible")

        nodes = page.locator(".hub-node")
        count = nodes.count()
        print(f"Found {count} hub nodes.")

        # Expect 7 nodes (center + 6 pillars)
        if count != 7:
            print(f"ERROR: Expected 7 nodes, found {count}")
            browser.close()
            exit(1)

        # Check Center Node (first one in DOM usually, or by ID)
        center_node = page.locator("#hub-center")
        expect(center_node).to_be_visible()

        # Check Pillars
        for i in range(count):
            node = nodes.nth(i)
            # visual scroll to it
            node.scroll_into_view_if_needed()

            # Check Attributes
            tabindex = node.get_attribute("tabindex")
            role = node.get_attribute("role")
            aria_label = node.get_attribute("aria-label")

            print(f"Node {i}: tabindex={tabindex}, role={role}, label={aria_label}")

            if tabindex != "0":
                print(f"ERROR: Node {i} missing tabindex='0'")

            if role != "img":
                 print(f"ERROR: Node {i} missing role='img'")

            if not aria_label:
                 print(f"ERROR: Node {i} missing aria-label")

            # Check Focus
            node.focus()
            expect(node).to_be_focused()
            print(f"Node {i} focuses correctly.")

        browser.close()
        print("Hub UX Verification Complete.")

if __name__ == "__main__":
    verify_hub_ux()
