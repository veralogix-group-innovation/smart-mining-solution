from playwright.sync_api import sync_playwright, expect
import os

def verify_download_button():
    base_dir = os.getcwd()
    html_file = os.path.join(base_dir, "index.html")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        print(f"Opening {html_file}")
        page.goto(f"file://{html_file}")

        # Scroll to the Hub section
        page.locator("#hub").scroll_into_view_if_needed()
        page.wait_for_timeout(500) # Wait for animation

        # Check for the button
        download_btn = page.get_by_role("link", name="DOWNLOAD ALL SCREENSHOTS")
        expect(download_btn).to_be_visible()

        href = download_btn.get_attribute("href")
        print(f"Button href: {href}")
        assert href == "assets/hub-screenshots.zip"

        # Take screenshot of the section
        screenshot_path = os.path.join(base_dir, "verification/download_button_verification.png")
        # Removing manual clip, relying on element screenshot

        # Better screenshot method
        hub_section = page.locator("#hub")
        hub_section.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    verify_download_button()
