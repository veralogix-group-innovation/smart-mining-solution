from playwright.sync_api import sync_playwright, expect
import os

def verify_hub_ux():
    base_dir = os.getcwd()
    html_file = "index.html"
    file_path = os.path.join(base_dir, html_file)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        print(f"Checking {html_file} for Smart Hub UX...")
        page.goto(f"file://{file_path}")

        # Scroll to the Hub section to ensure it's visible (though not strictly necessary for DOM presence check)
        hub_section = page.locator("#hub")
        hub_section.scroll_into_view_if_needed()

        # Wait for the hub nodes to be generated
        # There should be 7 nodes: 1 center + 6 pillars
        nodes = page.locator(".hub-node")
        expect(nodes).to_have_count(7, timeout=5000)

        print("Hub nodes found.")

        # Check accessibility attributes for the center node
        center_node = page.locator("#hub-center")
        expect(center_node).to_have_attribute("role", "img")
        expect(center_node).to_have_attribute("tabindex", "0")
        expect(center_node).to_have_attribute("aria-label", "Smart Hub Center")

        print("Center node accessibility verified.")

        # Check accessibility attributes for the pillar nodes
        # We'll check the first one as a sample, or iterate
        count = nodes.count()
        for i in range(count):
            node = nodes.nth(i)
            # Center node is one of them, we already checked specific attributes for it,
            # but let's check general structure for all
            if node.get_attribute("id") == "hub-center":
                continue

            expect(node).to_have_attribute("role", "img")
            expect(node).to_have_attribute("tabindex", "0")
            # Aria label should be present
            aria_label = node.get_attribute("aria-label")
            assert aria_label and "Smart Hub Pillar:" in aria_label, f"Node {i} missing correct aria-label: {aria_label}"

        print("Pillar nodes accessibility verified.")

        # Take a screenshot for visual verification
        page.screenshot(path="verification/hub_ux.png")
        print("Screenshot saved to verification/hub_ux.png")

        browser.close()

if __name__ == "__main__":
    try:
        verify_hub_ux()
        print("SUCCESS: Smart Hub UX verification passed.")
    except Exception as e:
        print(f"FAILURE: {e}")
        exit(1)
