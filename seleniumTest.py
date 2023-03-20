from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

#get(): Belirli bir URL'ye gitmek için kullanılır.
driver.get("https://www.example.com")

#send_keys: Bir web sayfasındaki bir metin kutusuna metin girmek için kullanılır.
search_box = driver.find_element_by_name("q")
search_box.send_keys("Selenium")
#Bu kodda, send_keys() yöntemi, "q" adlı metin kutusuna "Selenium" metnini girer.


#click() : Bir web sayfasındaki bir düğmeye tıklamak için kullanılır.
search_button = driver.find_element_by_name("btnK")
search_button.click()


#clear() : Bir metin kutusundaki metni temizlemek için kullanılır.
search_box = driver.find_element_by_name("q")
search_box.send_keys("Selenium öğreniyorum")
search_box.clear()

