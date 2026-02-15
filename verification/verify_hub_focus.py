from playwright.sync_api import sync_playwright, expect
import os

def verify_hub_focus():
    base_dir = os.getcwd()
    html_file = os.path.join(base_dir, "index.html")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        print(f"Opening {html_file}")
        page.goto(f"file://{html_file}")

        # Wait for the diagram to be generated
        page.wait_for_selector("#hub-diagram .hub-node", timeout=5000)

        # Scroll to the Hub diagram
        hub_section = page.locator("#hub")
        hub_section.scroll_into_view_if_needed()
        page.wait_for_timeout(500)

        nodes = page.locator(".hub-node")
        count = nodes.count()
        print(f"Found {count} hub nodes")

        if count == 0:
            print("Error: No hub nodes found.")
            exit(1)

        # Check attributes and focusability
        for i in range(count):
            node = nodes.nth(i)
            print(f"Checking node {i}...")

            # Check tabindex
            tabindex = node.get_attribute("tabindex")
            if tabindex != "0":
                print(f"Failure: Node {i} missing tabindex='0'. Found: {tabindex}")
            else:
                print(f"Success: Node {i} has tabindex='0'")

            # Check role
            role = node.get_attribute("role")
            if role != "img":
                 print(f"Failure: Node {i} missing role='img'. Found: {role}")
            else:
                print(f"Success: Node {i} has role='img'")

            # Check aria-label
            label = node.get_attribute("aria-label")
            if not label:
                 print(f"Failure: Node {i} missing aria-label.")
            else:
                 print(f"Success: Node {i} has aria-label='{label}'")

        # Attempt to tab through nodes
        # Focus the first focusable element before the nodes (e.g., ROI link in nav if visible, or skip link)
        # It's easier to just try to focus the node directly if it's focusable, or press Tab repeatedly.

        # Focus the second node (index 1) which is a pillar node (starts dark)
        target_node = nodes.nth(1)
        try:
            target_node.focus()
            expect(target_node).to_be_focused()
            print("Success: Second node (pillar) is focusable via .focus()")

            # Check for visual change (class or style)
            # Since we are using :focus pseudo-class, we check computed styles
            # Wait a bit for transition
            page.wait_for_timeout(300)

            # Check if z-index is 20 (as defined in :hover and planned for :focus)
            z_index = target_node.evaluate("element => window.getComputedStyle(element).zIndex")
            print(f"Focused node z-index: {z_index}")

            if z_index != "20":
                 print("Failure: Focused node does not have z-index 20 (style not applied).")
            else:
                 print("Success: Focused node has z-index 20.")

            # Take screenshot of the focused node
            screenshot_path = os.path.join(base_dir, "verification/hub_focused_pillar.png")
            # Screenshot the container to see the effect
            page.locator("#hub-diagram").screenshot(path=screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")

        except Exception as e:
            print(f"Failure: Could not focus pillar node. Error: {e}")

        browser.close()

if __name__ == "__main__":
    verify_hub_focus()
