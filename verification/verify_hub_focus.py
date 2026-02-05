import os
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local index.html file
        file_path = os.path.abspath("index.html")
        page.goto(f"file://{file_path}")

        # Wait for the hub diagram to be generated
        try:
            page.wait_for_selector(".hub-node", timeout=5000)
        except Exception as e:
            print("Error: Hub nodes not found within timeout.")
            exit(1)

        # Get all hub nodes
        nodes = page.locator(".hub-node").all()
        print(f"Found {len(nodes)} hub nodes.")

        if len(nodes) == 0:
            print("Error: No hub nodes found.")
            exit(1)

        # Verify accessibility attributes
        all_passed = True
        for i, node in enumerate(nodes):
            tabindex = node.get_attribute("tabindex")
            role = node.get_attribute("role")
            aria_label = node.get_attribute("aria-label")

            print(f"Node {i}: tabindex={tabindex}, role={role}, aria-label={aria_label}")

            if tabindex != "0":
                print(f"  FAILED: Node {i} missing tabindex='0'")
                all_passed = False
            if role != "img":
                print(f"  FAILED: Node {i} missing role='img'")
                all_passed = False
            if not aria_label:
                print(f"  FAILED: Node {i} missing aria-label")
                all_passed = False

        if not all_passed:
            print("Accessibility attribute verification failed.")
            # We don't exit here yet to check focus logic if possible, but without tabindex focus won't work.

        # Test keyboard navigation
        print("Testing keyboard navigation...")
        # Reset focus to body
        page.evaluate("document.body.focus()")

        # Press Tab repeatedly until we find a hub node
        found_focus = False
        focused_node_index = -1

        # We need to tab enough times to get past header links.
        # Skip link is first. Then header nav links.
        # This might be many tabs.
        # Alternative: Focus the element before the hub section if we knew what it was.
        # Or force focus on a node and check if it sticks (requires tabindex).

        # Let's try to focus the first node programmatically to check if it's focusable at all.
        try:
            nodes[0].focus()
            is_focused = page.evaluate("document.activeElement === document.querySelector('.hub-node')")
            if is_focused:
                 print("  Direct focus() worked (unexpected if tabindex is missing).")
            else:
                 print("  Direct focus() failed (expected if tabindex is missing).")
        except Exception as e:
            print(f"  Direct focus() threw exception: {e}")

        # Now try tabbing
        # We'll just try to Tab a few times and see if active element becomes a hub node.
        # Since there are many links, this might be flaky if we just count tabs.
        # But if we cycle through everything?

        # Let's just check if attributes are correct for now as the primary verification.
        if not all_passed:
            exit(1)

        # Take a screenshot of the focused node (if we managed to focus one, or just the hub area)
        # Try to focus a node to show the effect
        try:
            nodes[0].focus()
            page.wait_for_timeout(500) # Wait for transition
            page.screenshot(path="verification/hub_focused.png")
            print("Screenshot saved to verification/hub_focused.png")
        except Exception as e:
            print(f"Could not focus or screenshot: {e}")

        browser.close()

if __name__ == "__main__":
    run()
