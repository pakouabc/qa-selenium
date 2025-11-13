from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service()

driver = webdriver.Chrome(service=service)
driver.get("https://luisfraustoaf0724.pythonanywhere.com/auth/register")
driver.maximize_window()

time.sleep(2)
for cuenta in range(200,210):
	elem = driver.find_element(By.ID, "email")
	elem.clear()
	elem.send_keys(f"pako+{cuenta}@uabc.edu.mx")

	elem = driver.find_element(By.ID, "phone")
	elem.clear()
	elem.send_keys("6461234567")

	elem = driver.find_element(By.ID, "street")
	elem.clear()
	elem.send_keys(f"wallaby sidney {cuenta}")

	elem = driver.find_element(By.ID, "city")
	elem.clear()
	elem.send_keys(f"sim {cuenta}")

	elem = driver.find_element(By.ID, "state")
	elem.clear()
	elem.send_keys("solido")

	elem = driver.find_element(By.ID, "interior_number")
	elem.clear()
	elem.send_keys(cuenta)

	elem = driver.find_element(By.ID, "postal_code")
	elem.clear()
	elem.send_keys(f"22{cuenta}")

	elem = driver.find_element(By.ID, "last_name")
	elem.clear()
	elem.send_keys("EresElMejor")

	elem = driver.find_element(By.ID, "first_name")
	elem.clear()
	elem.send_keys(f"pako {cuenta}")
	elem = driver.find_element(By.ID, "age")
	elem.clear()
	elem.send_keys(f"{cuenta}")

	elem = driver.find_element(By.ID, "password")
	elem.clear()
	elem.send_keys("pako1984")

	elem = driver.find_element(By.ID, "confirm_password")
	elem.clear()
	elem.send_keys("pako1984")

	elem.send_keys(Keys.RETURN)
	time.sleep(2)
	driver.get("https://luisfraustoaf0724.pythonanywhere.com/auth/logout")
	time.sleep(2)
	driver.get("https://luisfraustoaf0724.pythonanywhere.com/auth/register")
	time.sleep(2)

driver.close()
