from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

print("Cookies Clicker uygulamasına hoş geldiniz.")
print("Bağlantıyı başlatmak için enter tuşuna basın.")
input()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://orteil.dashnet.org/cookieclicker/")
sleep(3)
langSelect = driver.find_element(By.ID,"langSelect-EN")
langSelect.click()
sleep(15)
print("Kapatmak için tıklama sayısına 0 yazın. Kapatmadan önce kayıt aldığınızdan emin olun.")
print("Tıklanma ensanısnda işlem yapamazsınız.")
while True:
    i=0
    counttttt= int(input("tıklanıcak adeti girin:"))
    if(counttttt == 0 ):
        break
    while i < counttttt:
        bigCookie = driver.find_element(By.ID,"bigCookie")
        bigCookie.click()
        i+=1
