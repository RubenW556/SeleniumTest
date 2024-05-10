# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



class TestCase():
    def setup_method(self, method):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(options)
        self.driver.implicitly_wait(5)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_case(self):
        self.run()
    # def test_case1(self):
    #     self.run()
    # def test_case2(self):
    #     self.run()
    # def test_case3(self):
    #     self.run()
    # def test_case4(self):
    #     self.run()
    def run(self):
        self.driver.get("https://baw21.novadoc.ecm:9443/navigator/login.jsp")
        self.driver.find_element(By.NAME, "j_username").send_keys("p8admin")
        self.driver.find_element(By.NAME, "j_password").send_keys("Password1")
        self.driver.find_element(By.NAME, "login").click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".icmRolePicker"))).click()
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Trainee')]").click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Add Case')]"))).click()
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Request Training')]").click()
        self.driver.find_element(By.ID, "pvr_widget_editors_TextBoxEditor_0").send_keys("hi")
        self.driver.find_element(By.ID, "pvr_widget_editors_TextBoxEditor_1").send_keys("hi")
        self.driver.find_element(By.ID, "pvr_widget_editors_TextBoxEditor_2").send_keys("hi")
        self.driver.find_elements(By.XPATH, "//*[contains(text(), 'Add')]").pop().click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".icmRolePicker").click()
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Trainer')]").click()
        self.driver.find_element(By.XPATH, "//*[@id='icm_widget_SelectorTabContainer_0_tablist']/div[4]/div/div[2]").click()
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'New Approval')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Approve')]").click()
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Plan Training')]").click()
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Complete')]").click()

