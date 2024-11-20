import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class EdgeBrowserInSelenium(unittest.TestCase):
    url = "https://www.testingtherapy.com/"
    driver = None

    @classmethod
    def setUpClass(cls):
        """Set up the Edge browser before the tests."""
        try:
            print("Setting up Edge WebDriver...")
            service = Service(EdgeChromiumDriverManager().install())  # Set up Edge WebDriver
            cls.driver = webdriver.Edge(service=service)  # Initialize Edge WebDriver
            cls.driver.maximize_window()  # Maximize browser window
            print("Edge WebDriver setup successful")
        except Exception as e:
            print(f"Error setting up the Edge WebDriver: {e}")
            raise

    def test_open_url(self):
        """Open the URL in the Edge browser."""
        try:
            self.driver.get(self.url)
            self.assertEqual(self.driver.current_url, self.url, "URL did not open correctly")
        except Exception as e:
            print(f"Error during URL test: {e}")
            raise

    @classmethod
    def tearDownClass(cls):
        """Close the Edge browser after all tests."""
        if cls.driver:
            cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
