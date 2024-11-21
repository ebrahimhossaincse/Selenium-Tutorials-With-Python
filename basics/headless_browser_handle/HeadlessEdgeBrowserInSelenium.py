import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class HeadlessEdgeBrowser(unittest.TestCase):
    url = "https://www.testingtherapy.com/"
    driver = None

    @classmethod
    def setUpClass(cls):
        """Set up the headless Edge browser before tests."""
        # Set up Edge options
        options = Options()
        options.add_argument("--headless")  # Enable headless mode
        options.add_argument("--window-size=1920,1080")  # Set fixed window size

        # Set up EdgeDriver using WebDriverManager
        service = Service(EdgeChromiumDriverManager().install())
        cls.driver = webdriver.Edge(service=service, options=options)  # Assign to class attribute
        print("Headless Edge Browser Started")

    def test_open_url(self):
        """Open the URL in the Edge browser and verify the URL."""
        self.driver.get(self.url)
        self.assertEqual(self.driver.current_url, self.url, "URL did not open correctly")

    @classmethod
    def tearDownClass(cls):
        """Close the Edge browser after all tests."""
        if cls.driver:
            cls.driver.quit()
            print("Headless Edge Browser Closed")


if __name__ == "__main__":
    unittest.main()
