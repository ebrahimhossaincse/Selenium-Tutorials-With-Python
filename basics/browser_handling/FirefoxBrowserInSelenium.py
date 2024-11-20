import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class FirefoxBrowserInSelenium(unittest.TestCase):
    url = "https://www.testingtherapy.com/"
    driver = None

    @classmethod
    def setUpClass(cls):
        """Set up the Firefox browser before the tests."""
        try:
            service = Service(GeckoDriverManager().install())  # Set up GeckoDriver
            cls.driver = webdriver.Firefox(service=service)    # Initialize Firefox WebDriver
            cls.driver.maximize_window()                       # Maximize browser
        except Exception as e:
            print(f"Error setting up the Firefox WebDriver: {e}")
            raise

    def test_open_url(self):
        """Open the URL in the Firefox browser."""
        self.driver.get(self.url)
        self.assertEqual(self.driver.current_url, self.url, "URL did not open correctly")

    @classmethod
    def tearDownClass(cls):
        """Close the Firefox browser after all tests."""
        if cls.driver:
            cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
