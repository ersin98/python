from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.com.tr/?hl=tr")
sleep(1)#daha yüklenmeden elemanın bulunmaya çalışması sıkıntı
input = driver.find_element(By.NAME,"q")
print(f"Input: {input}")
input.send_keys("kodlama io")#selamun aleyküm
searchButton= driver.find_element(By.NAME,"btnK")
sleep(2)
searchButton.click()
#input()
sleep(5)
firstResult=driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a/h3")#/html/body/div[7]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/a/h3
sleep(3)
firstResult.click()
sleep(5)
#clickSA= driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/p[1]/span/a/span")#/html/body/div[1]/div/div[3]/main/div[2]/div[3]/div[1]/p[1]/span/a/span
#clickSA.click()
listOfCourses=driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"şuanda {len(listOfCourses)} adet kurs var")


sleep(40)
#full xpath
#/html/body/div[7]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/a/h3
#xpath
#//*[@id="rso"]/div[1]/div/div/div/div[1]/div/a/h3

