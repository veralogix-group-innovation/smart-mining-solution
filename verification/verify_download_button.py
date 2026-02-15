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

        # Scroll to the Footer
        footer = page.locator("footer")
        footer.scroll_into_view_if_needed()
        page.wait_for_timeout(500)

        # Check for the link
        download_link = page.get_by_role("link", name="Download Assets")
        expect(download_link).to_be_visible()

        href = download_link.get_attribute("href")
        print(f"Link href: {href}")
        assert href == "assets/hub-screenshots.zip"

        # Take screenshot of the footer
        screenshot_path = os.path.join(base_dir, "verification/footer_verification.png")
        footer.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    verify_download_button()
