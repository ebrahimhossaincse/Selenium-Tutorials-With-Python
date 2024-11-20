import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ChromeBrowserInSelenium(unittest.TestCase):
    url = "https://www.testingtherapy.com/"
    driver = None

    @classmethod
    def setUpClass(cls):
        """Set up the Chrome browser before the tests."""
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()  # Maximize the browser window

    def test_open_url(self):
        """Open the URL in the Chrome browser."""
        self.driver.get(self.url)
        self.assertEqual(self.driver.current_url, self.url, "URL did not open correctly")

    @classmethod
    def tearDownClass(cls):
        """Close the Chrome browser after all tests."""
        if cls.driver:
            cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
