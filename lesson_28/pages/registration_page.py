from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class RegistrationPage:
    # Locators
    FIRST_NAME_INPUT = (By.ID, "signupName")
    LAST_NAME_INPUT = (By.ID, "signupLastName")
    EMAIL_INPUT = (By.ID, "signupEmail")
    PASSWORD_INPUT = (By.ID, "signupPassword")
    CONFIRM_PASSWORD_INPUT = (By.ID, "signupRepeatPassword")
    REGISTER_BUTTON = (By.XPATH, "//div[@class='modal-footer']//button[contains(@class, 'btn-primary') and text("
                                 ")='Register']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'alert') and contains(@class, 'alert-danger') and text()='User "
                               "already exists']")

    def __init__(self, driver):
        self.driver = driver

    def register_user(self, first_name, last_name, email, password):
        # Fill in fregistration form and press "Register" button
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT).send_keys(password)

        # print(self.driver.page_source)

        # Wait for modal window
        modal = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, "modal-content"))
        )
        assert modal.is_displayed(), "Modal dialog not visible"

        # Wait for "Registry" button enabled
        register_button = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.REGISTER_BUTTON)
        )
        register_button.click()

        # Check for error message
        try:
            error_message = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.ERROR_MESSAGE)
            )
            return error_message.text
        except TimeoutException:
            return None