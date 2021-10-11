import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.alamy.es/log-in/?returnurl=https%3A%2F%2Fwww.alamy.es%2F")
time.sleep(5)

email = driver.find_element_by_id("txtBoxEmail")
email.send_keys("pruebacriptoy@outlook.com")
password = driver.find_element_by_id("txtBoxContraseña")
password.send_keys("criptografia100")

for i in range(1,101):
    time.sleep(5)
    print("Intento " + str(i))
    click = driver.find_element_by_id("btnIniciarsesión").click()