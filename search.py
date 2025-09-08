from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.by import By

keyboard = Controller()
from selenium.webdriver.chrome.service import Service
service = Service("./chromedriver")

driver = webdriver.Chrome(service=service)
driver.get("https://www.elvigia.net/")
#assert "Tramites Ensenada" in driver.title
time.sleep(3)
# elem = driver.find_element(by=By.ID, value="searchBox")
# #driver.find_element_by_id("searchBox")
# elem.clear()
# elem.send_keys("multa")
# elem.send_keys(Keys.RETURN)
# time.sleep(10)
sample_chars = 'trmk90iuloes45cand'
sample_list_chars = ["comida","cine","tacos","uabc","Test","Medida","prueba","lorem","asd"]
#driver.get("http://bugzilla.ensenada.gob.mx/~tramites/login")
for i in range(1):
	lenght = random.randint(3,10)
	search = "".join((random.choice(sample_chars)) for x in range(lenght))
	print(f"Intent : {i} Search: {search}")
	elem = driver.find_element(by=By.NAME, value="buscar")
	elem.clear()
	elem.send_keys(search)
	elem.send_keys(Keys.RETURN)
	time.sleep(.1)
for i in range(2000):
	search = random.choice(sample_list_chars)
	print(f"Intent : {i} Search: {search}")
	elem = driver.find_element(by=By.NAME, value="buscar")
	elem.clear()
	elem.send_keys(search)
	elem.send_keys(Keys.RETURN)
	time.sleep(.2)

input("Press Enter to continue...")
#assert "No results found." not in driver.page_source" 
driver.close()
