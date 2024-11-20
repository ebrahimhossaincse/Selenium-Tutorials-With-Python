import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class HeadlessChromeBrowser(unittest.TestCase):
    url = "https://www.testingtherapy.com/"
    driver = None

    @classmethod
    def setUpClass(cls):
        """Set up the headless Chrome browser before tests."""
        # Set up Chrome options
        options = Options()
        options.add_argument("--headless=new")  # Enable headless mode
        options.add_argument("--disable-gpu")  # Disable GPU rendering
        options.add_argument("--window-size=1920,1080")  # Set fixed window size
        options.add_argument("--disable-extensions")  # Disable extensions

        # Set up ChromeDriver using WebDriverManager
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service, options=options)  # Assign to class attribute
        print("Headless Chrome Browser Started")

    def test_open_url(self):
        """Open the URL in the Chrome browser and verify the URL."""
        self.driver.get(self.url)
        self.assertEqual(self.driver.current_url, self.url, "URL did not open correctly")

    @classmethod
    def tearDownClass(cls):
        """Close the Chrome browser after all tests."""
        if cls.driver:
            cls.driver.quit()
            print("Headless Chrome Browser Closed")


if __name__ == "__main__":
    unittest.main()
