from playwright.sync_api import sync_playwright
import os
import sys

def verify_hub_ux():
    cwd = os.getcwd()
    file_path = f"file://{cwd}/index.html"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(file_path)

        # Wait for the Hub to be generated
        page.wait_for_selector("#hub-center")
        page.wait_for_selector(".hub-node")

        print("Checking Smart Hub Center accessibility...")
        center = page.locator("#hub-center")

        # Check attributes
        tabindex = center.get_attribute("tabindex")
        role = center.get_attribute("role")
        aria_label = center.get_attribute("aria-label")

        if tabindex != "0":
            print("FAIL: #hub-center missing tabindex='0'")
            sys.exit(1)
        if role != "img":
            print("FAIL: #hub-center missing role='img'")
            sys.exit(1)
        if not aria_label:
            print("FAIL: #hub-center missing aria-label")
            sys.exit(1)

        print("PASS: Smart Hub Center attributes correct.")

        print("Checking Smart Hub Nodes accessibility...")
        nodes = page.locator(".hub-node")
        count = nodes.count()

        # We know there should be nodes (the center is one .hub-node, but the generated ones are also .hub-node)
        # Wait, looking at index.html:
        # center: class="... hub-node ..."
        # generated: class="hub-node absolute"
        # So all of them are .hub-node.

        # We need to distinguish generated nodes from center if we want specific checks,
        # but the plan says verify both have attributes.

        for i in range(count):
            node = nodes.nth(i)
            # Skip if it's the center and we already checked it?
            # Actually, let's just check all of them.

            t_index = node.get_attribute("tabindex")
            r_role = node.get_attribute("role")
            a_label = node.get_attribute("aria-label")

            if t_index != "0":
                print(f"FAIL: Node {i} missing tabindex='0'")
                sys.exit(1)
            if r_role != "img":
                print(f"FAIL: Node {i} missing role='img'")
                sys.exit(1)
            if not a_label:
                print(f"FAIL: Node {i} missing aria-label")
                sys.exit(1)

        print("PASS: All hub nodes have correct attributes.")

        # Check focus behavior
        print("Checking focus behavior...")
        # Focus the first node (likely the center or first generated one)
        first_node = nodes.first
        first_node.focus()

        # Check if it is focused
        is_focused = first_node.evaluate("element => document.activeElement === element")
        if not is_focused:
             print("FAIL: Element did not receive focus.")
             sys.exit(1)

        # Check for visual changes (CSS)
        # We expect color change on .hub-text child when .hub-node is focused
        # But wait, the center node HAS no .hub-text child. It has text directly.
        # The generated nodes have .hub-text child.

        # Let's find a generated node (one with .hub-text)
        generated_node = page.locator(".hub-node:has(.hub-text)").first
        generated_node.focus()

        hub_text = generated_node.locator(".hub-text")

        # Get background color
        bg_color = hub_text.evaluate("element => getComputedStyle(element).backgroundColor")

        # Expected: #BFFF00 -> rgb(191, 255, 0)
        # The default is #222222 -> rgb(34, 34, 34)

        print(f"Focused Node Background Color: {bg_color}")

        if "rgb(191, 255, 0)" not in bg_color:
             print("FAIL: Focus state does not match hover state (background color not correct).")
             sys.exit(1)

        print("PASS: Focus state visual feedback confirmed.")

        # Take a screenshot for visual verification
        screenshot_path = os.path.join(cwd, "verification", "hub_focus.png")
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    verify_hub_ux()
