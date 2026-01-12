from playwright.sync_api import sync_playwright, expect
import os

def verify_footers():
    base_dir = os.getcwd()
    pages = ["index.html", "loadscan.html", "trimble.html", "cabin-eye.html", "vtol-drones.html", "sentrymine.html"]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        for html_file in pages:
            file_path = os.path.join(base_dir, html_file)
            if not os.path.exists(file_path):
                print(f"Warning: {html_file} not found")
                continue

            print(f"Checking {html_file}...")
            page.goto(f"file://{file_path}")

            # Scroll to the Footer
            footer = page.locator("footer")
            footer.scroll_into_view_if_needed()

            # Check for the link
            download_link = page.get_by_role("link", name="Download Assets")
            expect(download_link).to_be_visible()

            href = download_link.get_attribute("href")
            assert href == "assets/hub-screenshots.zip"
            print(f"Verified footer link in {html_file}")

        browser.close()

if __name__ == "__main__":
    verify_footers()
