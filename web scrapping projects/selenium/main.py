from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver_path="C:\development\chromedriver"
driver=webdriver.Chrome(chrome_driver_path)

assert "Python" in driver.title
driver.get("https://python.org")
#event_times=driver.find_elements_by_css_selector(".event-widget time")
event_names=driver.find_element(By.CSS_SELECTOR,"event_widget li a")
for date in event_names:
    print(date.text)
#event_names=driver.find_elements_by_css_selector("")

driver.quit()