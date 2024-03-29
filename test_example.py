import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from time import sleep
browser = 0

@pytest.fixture(autouse=True)
def run_around_tests():
    global browser
    options = FirefoxOptions()
    options.add_argument("--headless")
    browser = webdriver.Firefox(options=options)
    browser.get('http://win-1ics5jffm16.dev.local:9080/navigator/')
    browser.implicitly_wait(2)

def test_hi():
    sleep(3)
    assert browser.title == "IBM Content Navigator"
    browser.quit()


def test_hi2():
    actual = browser.find_element(By.XPATH, "// *[ @ id = \"ecm_widget_layout_NavigatorMainLayout_0_LoginPane\"] / div[1] / table / tbody / tr / td[2] / div[1]").text
    expected = "Welcome to IBM Content Navigator"
    assert actual == expected
