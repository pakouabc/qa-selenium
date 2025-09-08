from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
service = Service("./chromedriver")

driver = webdriver.Chrome(service=service)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title

driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text
time.sleep(11)
driver.quit()

