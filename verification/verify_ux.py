
from playwright.sync_api import sync_playwright
import os

def verify_accessibility():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Open the index.html file
        cwd = os.getcwd()
        page.goto(f'file://{cwd}/index.html')

        # Verify focus visible style on the search button or any primary button
        # We need to focus on a button to see the style.
        # Let's focus on the search button.
        search_button = page.get_by_label('Search site').nth(1) # The first one is the input label? No, input has label. Button has label.
        # The input has aria-label='Search site'
        # The button has aria-label='Search site'
        # Let's target them specifically.

        search_input = page.locator('input[aria-label="Search site"]')
        search_btn = page.locator('button[aria-label="Search site"]')

        search_input.click() # Focus input
        page.keyboard.press('Tab') # Focus button

        # Take a screenshot of the search area
        page.screenshot(path='verification/search_focus.png')

        # Verify Chart Buttons
        # Scroll to #solutions
        # page.locator('#loadOptimalBtn').scroll_into_view_if_needed()

        # Check initial state
        optimal = page.locator('#loadOptimalBtn')
        under = page.locator('#loadUnderBtn')

        print(f'Optimal Pressed: {optimal.get_attribute("aria-pressed")}')
        print(f'Under Pressed: {under.get_attribute("aria-pressed")}')

        # Click Underloaded
        under.click()

        # Check new state
        print(f'Optimal Pressed After Click: {optimal.get_attribute("aria-pressed")}')
        print(f'Under Pressed After Click: {under.get_attribute("aria-pressed")}')

        # Take a screenshot of the chart buttons
        page.screenshot(path='verification/chart_buttons.png')

        browser.close()

if __name__ == '__main__':
    verify_accessibility()
