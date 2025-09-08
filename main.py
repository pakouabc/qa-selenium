from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)  # así es en v4
driver.get("https://www.google.com")
print(driver.title)
time.sleep(3)
driver.quit()

