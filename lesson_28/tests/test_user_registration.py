import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "first_name, last_name, email, password, expected_error",
    [
        ("TestAA", "UserAA", "test.user11@example.com", "TestPassword123", None),  # New user
        ("Test", "User", "existing.user@example.com", "TestPassword123", "User already exists"),  # User exists Error
        # ("", "User", "test.user2@example.com", "TestPassword123", "Name is required"),  # No name
        # ("Test", "", "test.user3@example.com", "TestPassword123", "Last name is required"),  # No last name
        # ("Test", "User", "invalid-email", "TestPassword123", "Invalid email format"),  # Email is incorrect
        # ("Test", "User", "test.user4@example.com", "", "Password is required"),  # Empty password
    ],
)
def test_user_registration(driver, login_page, registration_page, first_name, last_name, email, password, expected_error):
    """Test user registration with multiple parameter sets."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.go_to_registration()

    # Register User
    error_message = registration_page.register_user(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
    )

    # Check up
    if expected_error:
        assert error_message == expected_error, f"Unexpected error: {error_message}"
        print(f"Error verified: {error_message}")
    else:
        success_message = WebDriverWait(registration_page.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//*[text()='Garage']"))
        )
        assert success_message.is_displayed(), "Registration failed, success message not found"
        print("Registration successful!")