from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver_path="C:\development\chromedriver"
driver=webdriver.Chrome(chrome_driver_path)


driver.get("https://www.python.org")
elem = driver.find_element(By.ID, "event_widget")
for date in elem:
    print(date.text)