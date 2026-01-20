from playwright.sync_api import sync_playwright

def verify_hub_accessibility():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # Load the local index.html file
        import os
        page.goto(f"file://{os.path.abspath('index.html')}")

        # Wait for the hub diagram to be generated
        page.wait_for_selector("#hub-diagram .hub-node", state="attached")

        # Check if hub nodes are focusable
        hub_nodes = page.locator("#hub-diagram .hub-node")
        count = hub_nodes.count()
        print(f"Found {count} hub nodes.")

        focusable_count = 0
        for i in range(count):
            node = hub_nodes.nth(i)
            # Check tabindex
            tabindex = node.get_attribute("tabindex")
            if tabindex is not None and int(tabindex) >= 0:
                focusable_count += 1
            else:
                # check if inner div is focusable
                inner = node.locator(".hub-text")
                if inner.count() > 0:
                    tabindex_inner = inner.get_attribute("tabindex")
                    if tabindex_inner is not None and int(tabindex_inner) >= 0:
                         focusable_count += 1

        print(f"Focusable hub nodes: {focusable_count}")

        browser.close()

if __name__ == "__main__":
    verify_hub_accessibility()
