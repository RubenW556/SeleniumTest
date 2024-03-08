from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver

options = FirefoxOptions()
options.add_argument("--headless")
browser = webdriver.Firefox(options=options)
browser.get('http://google.com/')

if(browser.title=="Google"):
    print ("yes!!!")
else:
    print ("no!!!")
browser.quit()