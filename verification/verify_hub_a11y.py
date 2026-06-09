import os
import sys
import asyncio
from playwright.async_api import async_playwright

async def verify_hub_a11y():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Load local index.html
        cwd = os.getcwd()
        url = f"file://{cwd}/index.html"
        print(f"Loading {url}")
        await page.goto(url)

        # Wait for hub nodes to be generated
        await page.wait_for_selector(".hub-node")

        # Get all hub nodes
        hub_nodes = await page.query_selector_all(".hub-node")
        print(f"Found {len(hub_nodes)} hub nodes")

        issues = []

        for i, node in enumerate(hub_nodes):
            # Check attributes
            tabindex = await node.get_attribute("tabindex")
            role = await node.get_attribute("role")
            aria_label = await node.get_attribute("aria-label")
            text = await node.inner_text()

            print(f"Node {i} ({text}): tabindex={tabindex}, role={role}, aria-label={aria_label}")

            if tabindex != "0":
                issues.append(f"Node {i} missing tabindex='0'")
            if role != "img":
                issues.append(f"Node {i} missing role='img'")
            if not aria_label:
                issues.append(f"Node {i} missing aria-label")

        # Check focusability
        if len(hub_nodes) > 0:
            try:
                await hub_nodes[0].focus()
                is_focused = await page.evaluate("document.activeElement === document.querySelector('.hub-node')")
                if not is_focused:
                    issues.append("Node 0 could not be focused via JS focus()")
            except Exception as e:
                issues.append(f"Error focusing node: {e}")

        await browser.close()

        if issues:
            print("\n❌ Verification Failed:")
            for issue in issues:
                print(f"  - {issue}")
            sys.exit(1)
        else:
            print("\n✅ Verification Passed: All hub nodes are accessible.")
            sys.exit(0)

if __name__ == "__main__":
    asyncio.run(verify_hub_a11y())
