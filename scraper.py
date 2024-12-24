import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class CricketDataScraper:
    def __init__(self, base_url, download_dir):
        self.base_url = base_url
        self.download_dir = download_dir
        self.driver = None

        # Set up Chrome options for Selenium
        self.chrome_options = Options()
        prefs = {"download.default_directory": self.download_dir, "profile.default_content_settings.popups": 0}
        self.chrome_options.add_experimental_option("prefs", prefs)

    def setup_driver(self):
        """Initialize the WebDriver."""
        service = Service()  # Provide the path to chromedriver if needed
        self.driver = webdriver.Chrome(service=service, options=self.chrome_options)

    def download_json_files(self):
        """Automate the download of JSON files for Test, ODI, and T20 matches."""
        try:
            # Navigate to the Cricsheet matches page
            self.driver.get(self.base_url)
            time.sleep(3)  # Allow time for the page to load

            # Define match types and their corresponding CSS selectors or XPath
            match_types = {
                "Test matches": '//a[contains(@href, "tests_json.zip")]',
                "One-day internationals": '//a[contains(@href, "odis_json.zip")]',
                "T20 internationals": '//a[contains(@href, "t20s_json.zip")]',
            }

            for match_type, xpath in match_types.items():
                print(f"Downloading {match_type}...")
                try:
                    # Locate and click the download link
                    link = self.driver.find_element(By.XPATH, xpath)
                    link.click()
                    time.sleep(5)  # Wait for the file to download
                except Exception as e:
                    print(f"Error downloading {match_type}: {e}")

            print("Download completed for all match types.")
        except Exception as e:
            print(f"An error occurred during scraping: {e}")

    def close_driver(self):
        """Close the Selenium WebDriver."""
        if self.driver:
            self.driver.quit()

    def run(self):
        """Execute the scraping process."""
        self.setup_driver()
        self.download_json_files()
        self.close_driver()


if __name__ == "__main__":
    # Define the URL and download directory
    BASE_URL = "https://cricsheet.org/matches/"
    DOWNLOAD_DIR = os.path.join(os.getcwd(), "downloads")  # Set to a preferred download directory

    # Ensure the download directory exists
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)

    # Run the scraper
    scraper = CricketDataScraper(BASE_URL, DOWNLOAD_DIR)
    scraper.run()
