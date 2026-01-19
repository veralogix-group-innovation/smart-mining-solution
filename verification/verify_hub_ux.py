from playwright.sync_api import sync_playwright, expect
import os
import sys
import re

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the page
        url = f"file://{os.getcwd()}/index.html"
        print(f"Loading {url}")
        page.goto(url)

        # Wait for the diagram to be generated
        try:
            page.wait_for_selector("#hub-center", state="visible", timeout=5000)
            page.wait_for_selector(".hub-node", state="visible", timeout=5000)
        except Exception as e:
            print("Timed out waiting for Hub Diagram elements.")
            sys.exit(1)

        # Get all hub nodes
        nodes = page.locator(".hub-node")
        count = nodes.count()
        print(f"Found {count} hub nodes.")

        if count < 2:
            print("Error: Expected at least center + 1 pillar node.")
            sys.exit(1)

        # 1. Check Center Node
        center = page.locator("#hub-center")
        print("Verifying Center Node attributes...")

        try:
            expect(center).to_have_attribute("tabindex", "0")
            expect(center).to_have_attribute("role", "img")
            expect(center).to_have_attribute("aria-label", "Smart Hub Center")
            print("✅ Center node attributes correct.")
        except AssertionError as e:
            print(f"❌ Center node attributes missing: {e}")
            # Don't exit yet, check pillars

        # 2. Check Pillar Node (e.g., the first one after center)
        # Note: .hub-node includes center.
        pillar = nodes.nth(1)
        print("Verifying Pillar Node attributes...")

        try:
            expect(pillar).to_have_attribute("tabindex", "0")
            expect(pillar).to_have_attribute("role", "img")
            # We don't check exact label content as it varies, just presence
            expect(pillar).to_have_attribute("aria-label", re.compile(r".+"))
            print("✅ Pillar node attributes correct.")
        except AssertionError as e:
            print(f"❌ Pillar node attributes missing: {e}")

        # 3. Check Focus Behavior
        print("Verifying Focus Behavior...")
        try:
            pillar.focus()
            expect(pillar).to_be_focused()
            print("✅ Pillar node is focusable.")

            # Check computed style for transform
            # The hover effect applies: transform: scale(1.1) translateX(-45%) translateY(-45%)
            # We check if the transform matrix changes from default.
            # Default (set by JS) is translate(-50%, -50%).
            # Note: computed style might return matrix(...)

            # Let's just check if the class or style is applied via CSS check?
            # CSS :focus-visible rules can't be easily checked via computed style in some browsers if not natively supported by playwright logic?
            # Actually computed style is the best way.

            # Let's check z-index which changes to 20 on hover/focus
            z_index = pillar.evaluate("element => window.getComputedStyle(element).zIndex")
            if z_index == "20":
                print("✅ Pillar node has correct z-index on focus (visual feedback active).")
            else:
                print(f"❌ Pillar node z-index is {z_index}, expected 20.")

            # Take screenshot for visual verification
            # Ensure it is in view
            pillar.scroll_into_view_if_needed()
            # Capture the diagram area
            page.locator("#hub-diagram").screenshot(path="verification/hub_focused.png")
            print("📸 Screenshot saved to verification/hub_focused.png")

        except Exception as e:
             print(f"❌ Focus test failed: {e}")

        browser.close()

if __name__ == "__main__":
    run()
