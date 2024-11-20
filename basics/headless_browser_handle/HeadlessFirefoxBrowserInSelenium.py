import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


class HeadlessFirefoxBrowser(unittest.TestCase):
    url = "https://www.testingtherapy.com/"
    driver = None

    @classmethod
    def setUpClass(cls):
        """Set up the headless Firefox browser before tests."""
        # Set up Firefox options
        options = Options()
        options.add_argument("--headless")  # Enable headless mode
        options.add_argument("--width=1920")  # Set fixed window width
        options.add_argument("--height=1080")  # Set fixed window height

        # Set up GeckoDriver using WebDriverManager
        service = Service(GeckoDriverManager().install())
        cls.driver = webdriver.Firefox(service=service, options=options)  # Assign to class attribute
        print("Headless Firefox Browser Started")

    def test_open_url(self):
        """Open the URL in the Firefox browser and verify the URL."""
        self.driver.get(self.url)
        self.assertEqual(self.driver.current_url, self.url, "URL did not open correctly")

    @classmethod
    def tearDownClass(cls):
        """Close the Firefox browser after all tests."""
        if cls.driver:
            cls.driver.quit()
            print("Headless Firefox Browser Closed")


if __name__ == "__main__":
    unittest.main()
