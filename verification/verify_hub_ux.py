import os
from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local index.html file
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/index.html")

        # Wait for the hub diagram to be generated
        page.wait_for_selector("#hub-diagram .hub-node")

        # Check if hub nodes are focusable
        # We'll try to press Tab and see if we land on them.
        # First, focus on the body or an element before the hub
        page.focus("body")

        # Get all hub nodes
        hub_nodes = page.locator(".hub-node")
        count = hub_nodes.count()
        print(f"Found {count} hub nodes.")

        focusable_count = 0
        for i in range(count):
            node = hub_nodes.nth(i)
            # Check tabindex attribute
            tabindex = node.get_attribute("tabindex")
            if tabindex is not None and int(tabindex) >= 0:
                focusable_count += 1

        print(f"Focusable hub nodes: {focusable_count}/{count}")

        if focusable_count < count:
            print("❌ Not all hub nodes are focusable.")
        else:
            print("✅ All hub nodes are focusable.")

        # Check for inline style conflict on hover (optional verification)
        # We can verify if transform changes on hover, but checking the code is easier.

        browser.close()

if __name__ == "__main__":
    run()
