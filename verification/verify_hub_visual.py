import os
import asyncio
from playwright.async_api import async_playwright, expect

async def verify_hub_visual():
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

        # Locate the first hub node (should be WORKFORCE or similar)
        # Using get_by_label as we added aria-labels
        node = page.locator(".hub-node").first

        # Scroll to view
        await node.scroll_into_view_if_needed()

        # Focus the node
        await node.focus()

        # Wait a bit for transitions
        await page.wait_for_timeout(500)

        # Take screenshot of the hub diagram area
        hub_diagram = page.locator("#hub-diagram")
        screenshot_path = "verification/hub_focus_state.png"
        await hub_diagram.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify_hub_visual())
