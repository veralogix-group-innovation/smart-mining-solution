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

        # Wait for hub to generate
        page.wait_for_selector("#hub-diagram")
        page.wait_for_timeout(1000)

        nodes = page.locator(".hub-node")
        count = nodes.count()
        print(f"Found {count} hub nodes")

        if count == 0:
            print("Error: No hub nodes found")
            exit(1)

        center_node = nodes.nth(0)
        first_pillar = nodes.nth(1)

        print("Checking Center Node...")
        try:
            expect(center_node).to_have_attribute("tabindex", "0")
            print("PASS: Center node has tabindex=0")
        except AssertionError:
            print("FAIL: Center node missing tabindex=0")

        print("Checking First Pillar Node...")
        try:
            expect(first_pillar).to_have_attribute("tabindex", "0")
            print("PASS: First pillar node has tabindex=0")
        except AssertionError:
            print("FAIL: First pillar node missing tabindex=0")

        try:
            expect(first_pillar).to_have_attribute("role", "img")
            print("PASS: First pillar node has role=img")
        except AssertionError:
            print("FAIL: First pillar node missing role=img")

        # Check aria-label presence
        val = first_pillar.get_attribute("aria-label")
        if val:
            print(f"PASS: First pillar node has aria-label='{val}'")
        else:
            print("FAIL: First pillar node missing aria-label")

        # Test Focusability
        print("Testing Focusability...")
        try:
            first_pillar.focus()
            expect(first_pillar).to_be_focused()
            print("PASS: First pillar is focusable")
        except Exception as e:
            print(f"FAIL: First pillar is not focusable: {e}")

        browser.close()

if __name__ == "__main__":
    verify_hub_ux()
