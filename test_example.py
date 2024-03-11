from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from time import sleep

def test_hi():
    options = FirefoxOptions()
    options.add_argument("--headless")
    browser = webdriver.Firefox(options=options)
    browser.get('http://win-1ics5jffm16.dev.local:9080/navigator/')
    sleep(3)
    assert browser.title == "IBM Content Navigator"
    browser.quit()
