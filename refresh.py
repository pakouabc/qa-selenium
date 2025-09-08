from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
service = Service("./chromedriver")

driver = webdriver.Chrome(service=service)

driver.get("https://www.uabc.mx/")
time.sleep(2)
for i in range(100):
    print(f'Rdeeffresh {i}')
    driver.refresh()
    time.sleep(1)
driver.close()
