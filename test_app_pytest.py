import pytest
import webbrowser
import logging
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Configuration
APP_URL = "http://localhost:8080"
TIMEOUT = 10
REPORT_FILE = "report.html"
SCREENSHOT_DIR = "screenshots"

# Ensure screenshot folder exists
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture(scope="module")
def driver():
    """Set up Chrome WebDriver and teardown."""
    logging.info("Launching Chrome browser...")
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(service=Service(), options=options)
    driver.implicitly_wait(TIMEOUT)
    yield driver
    logging.info("Closing browser...")
    driver.quit()

def take_screenshot(driver, name):
    """Save screenshot on failure."""
    path = os.path.join(SCREENSHOT_DIR, f"{name}.png")
    driver.save_screenshot(path)
    logging.info(f"Screenshot saved: {path}")

def test_page_title(driver):
    """Ensure page has a title."""
    try:
        driver.get(APP_URL)
        title = driver.title
        assert title.strip(), "Page title should not be empty"
    except Exception as e:
        take_screenshot(driver, "page_title_failed")
        raise e

def test_heading_exists(driver):
    """Check for <h1> heading."""
    try:
        driver.get(APP_URL)
        heading = WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        assert heading.text.strip(), "Heading should not be empty"
    except Exception as e:
        take_screenshot(driver, "heading_failed")
        raise e

def test_navigation_bar(driver):
    """Check for <nav> element."""
    try:
        driver.get(APP_URL)
        nav = driver.find_element(By.TAG_NAME, "nav")
        assert nav.is_displayed(), "Navbar should be visible"
    except Exception as e:
        take_screenshot(driver, "navbar_failed")
        raise e

def test_button_click(driver):
    """Click first button if present."""
    try:
        driver.get(APP_URL)
        button = driver.find_element(By.TAG_NAME, "button")
        assert button.is_displayed(), "Button should be visible"
        button.click()
        time.sleep(1)
    except NoSuchElementException:
        pytest.skip("No button found.")
    except Exception as e:
        take_screenshot(driver, "button_click_failed")
        raise e

def test_login_form(driver):
    """Check login form input fields and button."""
    try:
        driver.get(APP_URL)
        email = driver.find_element(By.NAME, "email")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.XPATH, "//button[@type='submit']")

        assert email.is_displayed(), "Email field not visible"
        assert password.is_displayed(), "Password field not visible"
        assert submit.is_displayed(), "Submit button not visible"

        # Enter dummy data
        email.send_keys("test@example.com")
        password.send_keys("password123")
        submit.click()
        time.sleep(1)
    except NoSuchElementException:
        pytest.skip("Login form not found.")
    except Exception as e:
        take_screenshot(driver, "login_form_failed")
        raise e

def test_open_report_after_run():
    """Open HTML report after run (optional)."""
    if os.path.exists(REPORT_FILE):
        logging.info(f"Opening report: {REPORT_FILE}")
        webbrowser.open(REPORT_FILE)
