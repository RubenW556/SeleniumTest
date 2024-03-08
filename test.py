from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver

options = FirefoxOptions()
options.add_argument("--headless")
browser = webdriver.Firefox(options=options)
browser.get('http://192.168.247.167:9443/')

if(browser.title=="No target servlet"):
    print ("yes!!!")
else:
    print ("no!!!")
browser.quit()