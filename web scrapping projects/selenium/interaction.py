from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver_path="C:\development\chromedriver"
driver=webdriver.Chrome(chrome_driver_path)

driver.get("https:en.wikipedia.org/wiki/Main_Page")

count=driver.find_element(By.ID,'articlecount')
print(count.text)