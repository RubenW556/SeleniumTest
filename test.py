from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from time import sleep
import unittest


class hit(unittest.TestCase):

    def test_hi(self):
        options = FirefoxOptions()
        options.add_argument("--headless")
        browser = webdriver.Firefox(options=options)
        browser.get('http://win-1ics5jffm16.dev.local:9080/navigator/')
        sleep(5)
        self.assertEqual(browser.title, "IBM Content Navigator")
        browser.quit()
