from playwright.sync_api import sync_playwright, expect
import os

def verify_hub_ux():
    base_dir = os.getcwd()
    file_path = os.path.join(base_dir, "index.html")

    if not os.path.exists(file_path):
        print("Error: index.html not found")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        print(f"Loading {file_path}...")
        page.goto(f"file://{file_path}")

        # Wait for the diagram to be generated
        page.wait_for_selector("#hub-diagram .hub-node")

        # Get all hub nodes
        nodes = page.locator(".hub-node")
        count = nodes.count()
        print(f"Found {count} hub nodes.")

        # Expect 7 nodes (1 center + 6 pillars)
        if count != 7:
            print(f"FAILURE: Expected 7 nodes, found {count}")
            # We don't exit here to see other failures if any, but in a real test we might.

        # Check accessibility attributes
        for i in range(count):
            node = nodes.nth(i)

            # Check tabindex
            tabindex = node.get_attribute("tabindex")
            if tabindex != "0":
                print(f"Node {i} missing tabindex='0' (found: {tabindex})")

            # Check role
            role = node.get_attribute("role")
            if role != "img":
                 print(f"Node {i} missing role='img' (found: {role})")

            # Check aria-label
            aria_label = node.get_attribute("aria-label")
            if not aria_label:
                print(f"Node {i} missing aria-label")
            else:
                print(f"Node {i} aria-label: {aria_label}")

        # Check Keyboard Navigation
        print("Testing keyboard navigation...")
        # Focus the first element on the page (Skip link)
        page.keyboard.press("Tab")

        # Tab through until we hit the hub nodes.
        # This is tricky because there are many links before.
        # Alternatively, we can focus the section before it and then tab.

        # Let's try to focus the element before the hub section to simulate natural flow,
        # or just verify they CAN be focused.

        # Focusing the first node explicitly to see if it receives focus
        nodes.first.focus()
        expect(nodes.first).to_be_focused()
        print("First node is focusable.")

        # Now Tab to the next one
        page.keyboard.press("Tab")
        expect(nodes.nth(1)).to_be_focused()
        print("Tabbed to second node successfully.")

        browser.close()

if __name__ == "__main__":
    verify_hub_ux()
