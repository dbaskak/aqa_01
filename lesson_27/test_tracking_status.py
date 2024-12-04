from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class NovaPoshtaTracking:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://tracking.novaposhta.ua/#/uk"

    def open_tracking_page(self):
        # Opens the tracking page
        self.driver.get(self.url)

    def enter_tracking_number(self, tracking_number):
        # Enters the tracking number into the input field and submits
        # Wait for the page to load and find the input field
        input_field = self.driver.find_element(By.ID, "en")
        input_field.clear()
        input_field.send_keys(tracking_number)
        input_field.send_keys(Keys.ENTER)  # Submit the tracking number

    def get_status(self):
        # Extracts the status of the package from the tracking page
        # Wait for the status to appear on the page
        time.sleep(3)
        status_element = self.driver.find_element(By.CSS_SELECTOR, "div.header__status-text")
        return status_element.text


def test_tracking_status():
    # Test to verify the tracking status of a package
    tracking_number = "59001261579871"  # A valid tracking number
    expected_status = "Отримана"  # Expected status for this tracking number

    driver = webdriver.Chrome()  # Initialize WebDriver
    driver.maximize_window()

    try:
        # Initialize the tracking class
        tracker = NovaPoshtaTracking(driver)
        tracker.open_tracking_page()

        # Enter the tracking number and get the status
        tracker.enter_tracking_number(tracking_number)
        actual_status = tracker.get_status()

        # Verify the status
        assert actual_status == expected_status, f"Expected '{expected_status}', but got '{actual_status}'"
        print(f"Test passed! Status: {actual_status}")
    finally:
        driver.quit()  # Close the browser


if __name__ == "__main__":
    test_tracking_status()