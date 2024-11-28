from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# Create a WebDriver instance
driver = webdriver.Chrome()  # Make sure you have chromedriver installed
driver.get("http://localhost:8000/dz.html")  # Open the main page

try:
    # Working with the first frame (dz_frame1)
    frame1 = driver.find_element(By.CSS_SELECTOR, "iframe[src='dz_frame1.html']")
    driver.switch_to.frame(frame1)  # Switch to the first frame
    input1 = driver.find_element(By.ID, "input1")
    input1.send_keys("Frame1_Secret")  # Enter the secret text
    driver.find_element(By.XPATH, "//button[text()='Verify']").click()  # Click the "Verify" button

    # Verify the result for the first frame
    alert = Alert(driver)
    assert alert.text == "Verification successful!", f"Frame1 failed: {alert.text}"
    print("Frame1 verification successful!")
    alert.accept()  # Close the alert dialog

    # Return to the main context
    driver.switch_to.default_content()

    # Working with the second frame (dz_frame2)
    frame2 = driver.find_element(By.CSS_SELECTOR, "iframe[src='dz_frame2.html']")
    driver.switch_to.frame(frame2)  # Switch to the second frame
    input2 = driver.find_element(By.ID, "input2")
    input2.send_keys("Frame2_Secret")  # Enter the secret text
    driver.find_element(By.XPATH, "//button[text()='Verify']").click()  # Click the "Verify" button

    # Verify the result for the second frame
    alert = Alert(driver)
    assert alert.text == "Verification successful!", f"Frame2 failed: {alert.text}"
    print("Frame2 verification successful!")
    alert.accept()  # Close the alert dialog

    print("Both frames verified successfully!")

finally:
    # Close the browser
    time.sleep(2)  # Extra time to view the results
    driver.quit()