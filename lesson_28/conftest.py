import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage

@pytest.fixture(scope="function")
def driver():
    # WebDriver initialize
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    # LoginPage initialize
    return LoginPage(driver)

@pytest.fixture
def registration_page(driver):
   # RegistrationPage initialize
    return RegistrationPage(driver)