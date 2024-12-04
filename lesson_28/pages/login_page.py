from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://guest:welcome2qauto@qauto2.forstudy.space/"  # Site login

    # Locators
    REGISTER_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-primary') and text()='Sign up']")  # "Sign Up" button

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        # Open start page
        self.driver.get(self.URL)

    def go_to_registration(self):
        # Registration page
        # Wait for button enabled
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.REGISTER_BUTTON)
        )
        self.driver.find_element(*self.REGISTER_BUTTON).click()