from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date
#from selenium.common.exceptions import NoSuchElementException

class Test_SaucedemoDefs():
    def __init__(self,driver):
        self.driver= driver
    def nullNamePassword(self):
        state=False
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(10)
        search_box = self.driver.find_element(By.ID,"user-name")
        search_box.clear()
        search_box = self.driver.find_element(By.ID,"password")
        search_box.clear()
        self.driver.find_element(By.ID,"login-button").click()# ayrı bir değişkene atmak yerine üstünde işlem yaptım
        self.driver.implicitly_wait(60)
        errorMessageContainer= self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        if("Epic sadface: Username is required"== errorMessageContainer.text):
            state=True
        print(f"nullNamePassword:{state}")
    def nullPassword(self):
        state=False
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(10)
        search_box = self.driver.find_element(By.ID,"user-name")
        search_box.send_keys("1")
        search_box = self.driver.find_element(By.ID,"password")
        search_box.clear()
        self.driver.find_element(By.ID,"login-button").click()
        self.driver.implicitly_wait(60)
        errorMessageContainer= self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        if("Epic sadface: Password is required"== errorMessageContainer.text):
            state=True
        print(f"nullPassword:{state}")
    def lockedOutUser(self):
        state=False
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(10)
        search_box = self.driver.find_element(By.ID,"user-name")
        search_box.send_keys("locked_out_user")
        search_box = self.driver.find_element(By.ID,"password")
        search_box.send_keys("secret_sauce")
        self.driver.find_element(By.ID,"login-button").click()
        self.driver.implicitly_wait(60)
        errorMessageContainer= self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        if("Epic sadface: Sorry, this user has been locked out."== errorMessageContainer.text):
            state=True
        print(f"lockedOutUser: {state}")
    def nullIcon(self):
        state1=False
        state2=True
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(10)
        search_box = self.driver.find_element(By.ID,"user-name")
        search_box.clear()
        search_box = self.driver.find_element(By.ID,"password")
        search_box.clear()
        self.driver.find_element(By.ID,"login-button").click()
        self.driver.implicitly_wait(60)
        icon1 = self.driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(1) > svg")
        state1= str(icon1.size)=="{'height': 18, 'width': 18}"
        icon2 = self.driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(2) > svg")
        state1=str(icon2.size)=="{'height': 18, 'width': 18}"
        self.driver.find_element(By.CLASS_NAME,"error-button").click()
        self.driver.implicitly_wait(10)
        try:
            icon1 = self.driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(1) > svg")
            if(str(icon1.size)=="{'height': 18, 'width': 18}"):
                state2= False
        except Exception:
            pass
        try:
            icon2 = self.driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(2) > svg")
            if(str(icon2.size)=="{'height': 18, 'width': 18}"):
                state2= False
        except Exception:
            pass
        print(f"nullIconState1:{state1}, nullIconState2:{state2}")
    def standardUser(self):
        state=False
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(10)
        search_box = self.driver.find_element(By.ID,"user-name")
        search_box.send_keys("standard_user")
        search_box = driver.find_element(By.ID,"password")
        search_box.send_keys("secret_sauce")
        self.driver.find_element(By.ID,"login-button").click()
        self.driver.implicitly_wait(60)
        if(self.driver.current_url=="https://www.saucedemo.com/inventory.html"):
            state=True
        print(f"standardUser: {state}")
    def numerOfItems(self):
        state=False
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(10)
        search_box = self.driver.find_element(By.ID,"user-name")
        search_box.send_keys("standard_user")
        search_box = self.driver.find_element(By.ID,"password")
        search_box.send_keys("secret_sauce")
        self.driver.find_element(By.ID,"login-button").click()
        self.driver.implicitly_wait(60)
        products= list(self.driver.find_elements(By.CLASS_NAME,"inventory_item"))
        if(len(products)==6):
            state=True
        print(f"numerOfItems: {state}")


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
saucedemoDefs= Test_SaucedemoDefs(driver)
saucedemoDefs.nullNamePassword()
saucedemoDefs.nullPassword()
saucedemoDefs.lockedOutUser()
saucedemoDefs.nullIcon()
saucedemoDefs.standardUser()
saucedemoDefs.numerOfItems()