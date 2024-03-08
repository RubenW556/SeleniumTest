from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver

options = FirefoxOptions()
options.add_argument("--headless")
browser = webdriver.Firefox(options=options)
browser.get('http://win-1ics5jffm16.dev.local:9080/navigator/')

if(browser.title=="No target servlet"):
    print ("yes!!!")
else:
    print ("no!!!")
browser.quit()