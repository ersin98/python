from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Test_Souce:
    def test_invalid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        usernameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(5)
        loginBtn=driver.find_element(By.ID,"login-button")
        sleep(5)
        loginBtn.click()
        sleep(1)
        errorMessage= driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult= errorMessage.text=="Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU: {testResult}")
testClass= Test_Souce()
testClass.test_invalid_login()
sleep(30)
