import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class CrossBrowserConfiguration(unittest.TestCase):
    url = "https://www.testingtherapy.com/"
    driver = None

    @classmethod
    def setUpClass(cls):
        """Set up the browser based on the provided browser name."""
        browser_name = "firefox"  # Default browser

        # Get browser name from environment or argument
        browser_name = getattr(cls, 'browser', browser_name)

        try:
            if browser_name == "chrome":
                service = Service(ChromeDriverManager().install())
                cls.driver = webdriver.Chrome(service=service)
            elif browser_name == "firefox":
                service = FirefoxService(GeckoDriverManager().install())
                cls.driver = webdriver.Firefox(service=service)
            elif browser_name == "edge":
                service = EdgeService(EdgeChromiumDriverManager().install())
                cls.driver = webdriver.Edge(service=service)
            else:
                raise ValueError(f"Unsupported browser: {browser_name}")

            cls.driver.maximize_window()  # Maximize window for consistency
        except Exception as e:
            print(f"Error setting up the {browser_name} WebDriver: {e}")
            raise

    def test_open_url(self):
        """Open the URL in the selected browser."""
        self.driver.get(self.url)
        self.assertEqual(self.driver.current_url, self.url, "URL did not open correctly")

    @classmethod
    def tearDownClass(cls):
        """Close the browser after all tests."""
        if cls.driver:
            cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
