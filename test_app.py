import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

APP_URL = "http://localhost:8080"  # Replace with your app URL if different
TIMEOUT = 10


class TestReactApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.info("Setting up browser driver...")
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        cls.driver = webdriver.Chrome(options=options)
        cls.wait = WebDriverWait(cls.driver, TIMEOUT)
        logging.info("WebDriver is ready.")

    def setUp(self):
        logging.info(f"Opening app at: {APP_URL}")
        self.driver.get(APP_URL)

    def test_page_title(self):
        logging.info("Testing page title...")
        title = self.driver.title
        logging.info(f"Title: {title}")
        self.assertNotEqual(title, "", "Title should not be empty")

    def test_heading_exists(self):
        logging.info("Checking for <h1> heading...")
        try:
            heading = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
            logging.info(f"Heading found: {heading.text}")
            self.assertTrue(len(heading.text) > 0)
        except TimeoutException:
            self.fail("Heading <h1> not found")

    def test_navigation_bar(self):
        logging.info("Verifying navbar presence...")
        try:
            nav = self.driver.find_element(By.TAG_NAME, "nav")
            self.assertTrue(nav.is_displayed())
        except NoSuchElementException:
            self.fail("Navigation bar not found")

    def test_button_click(self):
        logging.info("Looking for a button...")
        try:
            button = self.driver.find_element(By.XPATH, "//button")
            logging.info(f"Button text: {button.text}")
            self.assertTrue(button.is_displayed())
            button.click()
            logging.info("Button clicked successfully.")
        except NoSuchElementException:
            self.fail("No button found to click.")

    def test_form_submission(self):
        logging.info("Testing form input and submission...")
        try:
            name_input = self.driver.find_element(By.NAME, "name")
            email_input = self.driver.find_element(By.NAME, "email")
            submit_button = self.driver.find_element(By.XPATH, "//form//button")

            name_input.send_keys("Test User")
            email_input.send_keys("test@example.com")
            submit_button.click()

            # Optional: Check for success message
            success_message = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "success"))
            )
            self.assertIn("Thank you", success_message.text)
        except NoSuchElementException:
            logging.warning("Form or fields not found. Skipping form test.")
        except TimeoutException:
            self.fail("Form submission feedback not found in time.")

    def test_login_flow(self):
        logging.info("Checking login form flow...")
        try:
            username = self.driver.find_element(By.NAME, "username")
            password = self.driver.find_element(By.NAME, "password")
            login_btn = self.driver.find_element(By.XPATH, "//button[contains(text(),'Login')]")

            username.send_keys("admin")
            password.send_keys("password123")
            login_btn.click()

            dashboard = self.wait.until(
                EC.presence_of_element_located((By.ID, "dashboard"))
            )
            self.assertTrue(dashboard.is_displayed(), "Login dashboard not shown")
        except NoSuchElementException:
            logging.warning("Login elements not found. Skipping login test.")
        except TimeoutException:
            self.fail("Login response timed out")

    def test_custom_component(self):
        logging.info("Looking for a custom chart or component...")
        try:
            chart = self.driver.find_element(By.CLASS_NAME, "recharts-wrapper")
            self.assertTrue(chart.is_displayed())
            logging.info("Chart component is visible.")
        except NoSuchElementException:
            logging.warning("Custom component not found. Skipping this check.")

    def tearDown(self):
        time.sleep(1)  # Optional delay between tests

    @classmethod
    def tearDownClass(cls):
        logging.info("Closing browser...")
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
