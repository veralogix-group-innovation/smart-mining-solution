import os
import shutil
import zipfile
from playwright.sync_api import sync_playwright
import time
from pathlib import Path

def generate_screenshots():
    # Define mapping of pages to role/filename
    mapping = {
        "index.html": "executive/dashboard.png",
        "loadscan.html": "haulage/loadscan_report.png",
        "trimble.html": "survey/earthworks_precision.png",
        "cabin-eye.html": "safety/fatigue_monitoring.png",
        "vtol-drones.html": "security/aerial_surveillance.png",
        "sentrymine.html": "compliance/workforce_status.png"
    }

    base_dir = Path.cwd()
    screenshots_dir = base_dir / "screenshots"
    assets_dir = base_dir / "assets"
    zip_path = assets_dir / "hub-screenshots" # make_archive adds .zip

    # Clean up previous runs
    if screenshots_dir.exists():
        shutil.rmtree(screenshots_dir)
    screenshots_dir.mkdir()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        for html_file, output_path in mapping.items():
            file_path = base_dir / html_file
            if not file_path.exists():
                print(f"Warning: {html_file} not found.")
                continue

            full_output_path = screenshots_dir / output_path
            full_output_path.parent.mkdir(parents=True, exist_ok=True)

            print(f"Generating screenshot for {html_file} -> {output_path}")
            page.goto(f"file://{file_path}")

            # Wait for animations/charts
            page.wait_for_timeout(2000)

            page.screenshot(path=str(full_output_path), full_page=True)

        browser.close()

    # Zip the folder
    print(f"Zipping screenshots to {zip_path}.zip")
    shutil.make_archive(str(zip_path), 'zip', screenshots_dir)

    # Cleanup screenshots dir
    shutil.rmtree(screenshots_dir)
    print("Done.")

if __name__ == "__main__":
    generate_screenshots()
