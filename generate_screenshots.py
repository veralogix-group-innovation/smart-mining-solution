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

    print(f"Working directory: {base_dir}")
    print("Checking for HTML files...")
    found_files = []
    for f in mapping.keys():
        if (base_dir / f).exists():
            found_files.append(f)
        else:
            print(f"WARNING: {f} not found!")

    print(f"Found {len(found_files)}/{len(mapping)} files to process.")

    # Clean up previous runs
    if screenshots_dir.exists():
        shutil.rmtree(screenshots_dir)
    screenshots_dir.mkdir()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use a larger viewport to ensure everything is visible
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        for html_file, output_path in mapping.items():
            file_path = base_dir / html_file
            if not file_path.exists():
                print(f"Skipping {html_file} - File does not exist")
                continue

            full_output_path = screenshots_dir / output_path
            full_output_path.parent.mkdir(parents=True, exist_ok=True)

            print(f"Processing {html_file} -> {output_path}...")

            try:
                # Use file:// protocol with absolute path
                page.goto(f"file://{file_path.absolute()}", wait_until="load", timeout=60000)

                # Wait for animations/charts (increased timeout)
                page.wait_for_timeout(5000)

                # Ensure body is visible
                page.wait_for_selector("body", state="visible", timeout=10000)

                page.screenshot(path=str(full_output_path), full_page=True)

                if full_output_path.exists():
                    print(f"SUCCESS: Generated {full_output_path.name} ({full_output_path.stat().st_size} bytes)")
                else:
                    print(f"ERROR: Screenshot file was not created for {html_file}")

            except Exception as e:
                print(f"ERROR processing {html_file}: {e}")

        browser.close()

    # List generated files
    print("\nGenerated screenshots:")
    generated_count = 0
    for root, dirs, files in os.walk(screenshots_dir):
        for file in files:
            print(f" - {os.path.join(root, file)}")
            generated_count += 1

    if generated_count == 0:
        print("ERROR: No screenshots were generated. Aborting zip creation.")
        exit(1)

    # Zip the folder
    print(f"\nZipping {generated_count} files to {zip_path}.zip...")
    shutil.make_archive(str(zip_path), 'zip', screenshots_dir)

    if (zip_path.with_suffix('.zip')).exists():
        print(f"SUCCESS: Zip file created at {zip_path}.zip")
    else:
        print("ERROR: Zip file creation failed.")

    # Cleanup screenshots dir
    shutil.rmtree(screenshots_dir)
    print("Cleanup complete.")

if __name__ == "__main__":
    generate_screenshots()
