from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from time import sleep

options = FirefoxOptions()
options.add_argument("--headless")
browser = webdriver.Firefox(options=options)
browser.get('http://win-1ics5jffm16.dev.local:9080/navigator/')
sleep(5)
if(browser.title=="IBM Content Navigator"):
    print ("yes!!!")
else:
    print ("no!!!")
browser.quit()