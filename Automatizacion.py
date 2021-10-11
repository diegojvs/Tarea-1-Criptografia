import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':
    nombre = "Criptografia"
    apellido = "Seguridad"
    correo = "015@yopmail.com"
    contraseña = "Algunacontraseña5"
    nacimiento = "01-01-2000"

    while True:
        sitio = int(input("¿Qué sitio desea auditar?  \n Seleccione una opción indicando su numero \n 1. Everlast \n 2. Alamy \n 3. Salir \n"))
        if sitio == 1:
            while True:
                opcion1 = int(input("¿Que desea hacer? \n Seleccione una opción indicando su numero \n 1. Crear una cuenta \n 2. Iniciar sesión \n 3. Reestablecer contraseña \n 4. Modificar contraseña \n 5. Salir \n"))
                if opcion1 ==  1:
                    driver = webdriver.Chrome()
                    driver.get("https://www.everlast.cl/customer/account/create/")
                    time.sleep(5)
                    name1 = driver.find_element_by_id("firstname")
                    name1.send_keys(nombre)
                    lastname = driver.find_element_by_id("lastname")
                    lastname.send_keys(apellido)
                    email = driver.find_element_by_id("email_address")
                    email.send_keys(correo)
                    password = driver.find_element_by_id("password")
                    password.send_keys(contraseña)
                    password1 = driver.find_element_by_id("password-confirmation")
                    password1.send_keys(contraseña)
                    date = driver.find_element_by_id("dob")
                    date.send_keys(nacimiento)
                    click = driver.find_element_by_xpath('//*[@id="form-validate"]/div/div[1]/button').click()
                elif opcion1 == 2:
                    driver = webdriver.Chrome()
                    driver.get("https://www.everlast.cl/customer/account/login/")
                    time.sleep(5)
                    ataque = int(input("¿Desea hacer un ataque por fuerza bruta? \n Seleccione una opción indicando su numero \n 1. Si \n 2. No \n"))
                    if ataque == 1:
                        intentos = int(input("Ingrese el numero de intentos que desea hacer \n"))
                        for i in range(0,intentos):
                            time.sleep(1)
                            errorpass = "ClaveErronea" + str(i)
                            email = driver.find_element_by_id("email")
                            email.clear()
                            email.send_keys("0@yopmail.com")
                            password = driver.find_element_by_id("pass")
                            password.clear()
                            password.send_keys(errorpass)
                            click = driver.find_element_by_id("send2").click()
                    elif ataque == 2:
                        time.sleep(1)
                        email = driver.find_element_by_id("email")
                        email.clear()
                        email.send_keys("0@yopmail.com")
                        password = driver.find_element_by_id("pass")
                        password.clear()
                        password.send_keys(contraseña)
                        click = driver.find_element_by_id("send2").click()
                    else:
                        print("Opción erronea")
                elif opcion1 == 3:
                    driver = webdriver.Chrome()
                    driver.get("https://www.everlast.cl/customer/account/forgotpassword/")
                    time.sleep(5)
                    email = driver.find_element_by_id("email_address")
                    email.send_keys(correo)
                    clickr = driver.find_element_by_xpath('//*[@id="form-validate"]/div/div[1]/button').click()
                elif opcion1 == 4:
                    driver = webdriver.Chrome()
                    driver.get("https://www.everlast.cl/customer/account/login/")
                    time.sleep(5)
                    email = driver.find_element_by_id("email")
                    email.clear()
                    email.send_keys("0@yopmail.com")
                    password = driver.find_element_by_id("pass")
                    password.clear()
                    password.send_keys(contraseña)
                    click = driver.find_element_by_id("send2").click()
                    time.sleep(5)
                    click = driver.find_element_by_xpath('//*[@id="block-collapsible-nav"]/ul/li[2]/a').click()
                    time.sleep(5)
                    click = driver.find_element_by_id("change-password").click()
                    time.sleep(3)
                    oldpass = driver.find_element_by_id("current-password")
                    oldpass.send_keys(contraseña)
                    newpass = driver.find_element_by_id("password")
                    newpass.send_keys("Nuevacontraseña1")
                    newpassconfirm = driver.find_element_by_id("password-confirmation")
                    newpassconfirm.send_keys("Nuevacontraseña1")
                    click = driver.find_element_by_xpath('//*[@id="form-validate"]/div/div[1]/button').click()
                elif opcion1 == 5:
                    break
                else: 
                    print("No existe esa opción")
        elif sitio == 2:
            while True:
                opcion1 = int(input("¿Que desea hacer? \n Seleccione una opción indicando su numero \n 1. Crear una cuenta \n 2. Iniciar sesión \n 3. Reestablecer contraseña \n 4. Modificar contraseña \n 5. Salir \n"))
                if opcion1 ==  1:
                    driver = webdriver.Chrome()
                    driver.get("https://www.alamy.es/create-customer-account/?returnurl=https%3A%2F%2Fwww.alamy.es%2F")
                    time.sleep(5)
                    email = driver.find_element_by_id("txtBoxEmail")
                    email.send_keys(correo)
                    password = driver.find_element_by_id("txtBoxContraseña")
                    password.send_keys(contraseña)
                    click = driver.find_element_by_id("btnCreesucuentaahora").click()
                    time.sleep(5)
                    click = driver.find_element_by_id("retLinkIdNoThanks").click()
                elif opcion1 == 2:
                    driver = webdriver.Chrome()
                    driver.get("https://www.alamy.es/log-in/?returnurl=https%3A%2F%2Fwww.alamy.es%2F")
                    time.sleep(5)
                    ataque = int(input("¿Desea hacer un ataque por fuerza bruta? \n Seleccione una opción indicando su numero \n 1. Si \n 2. No \n"))
                    if ataque == 1:
                        intentos = int(input("Ingrese el numero de intentos que desea hacer \n"))
                        errorpass = "ClaveErronea"
                        email = driver.find_element_by_id("txtBoxEmail")
                        email.send_keys("0@yopmail.com")
                        password = driver.find_element_by_id("txtBoxContraseña")
                        password.send_keys(errorpass)
                        for i in range(0,intentos):
                            time.sleep(1)
                            click = driver.find_element_by_xpath('//*[@id="btnIniciarsesión"]').click()
                    elif ataque == 2:
                        time.sleep(1)
                        email = driver.find_element_by_id("txtBoxEmail")
                        email.send_keys("0@yopmail.com")
                        password = driver.find_element_by_id("txtBoxContraseña")
                        password.send_keys(contraseña)
                        click = driver.find_element_by_xpath('//*[@id="btnIniciarsesión"]').click()
                    else:
                        print("Opción erronea")
                elif opcion1 == 3:
                    driver = webdriver.Chrome()
                    driver.get("https://www.alamy.es/forgot-password/")
                    time.sleep(5)
                    email = driver.find_element_by_id("txtBoxEmail")
                    email.send_keys(correo)
                    clickr = driver.find_element_by_id("btnEnviaremailderestablecimiento").click()
                elif opcion1 == 4:
                    driver = webdriver.Chrome()
                    driver.get("https://www.alamy.es/log-in/?returnurl=https%3A%2F%2Fwww.alamy.es%2F")
                    time.sleep(5)
                    email = driver.find_element_by_id("txtBoxEmail")
                    email.send_keys("0@yopmail.com")
                    password = driver.find_element_by_id("txtBoxContraseña")
                    password.send_keys(contraseña)
                    click = driver.find_element_by_xpath('//*[@id="btnIniciarsesión"]').click()
                    time.sleep(3)
                    click = driver.find_element_by_xpath('//*[@id="automationMyAlamy"]').click()
                    time.sleep(3)
                    click = driver.find_element_by_xpath('//*[@id="automationHeaderAccount"]').click()
                    time.sleep(3)
                    click = driver.find_element_by_xpath('//*[@id="ChangePasswodChange"]').click()
                    time.sleep(3)
                    oldpass = driver.find_element_by_id("CurrentPassword")
                    oldpass.send_keys(contraseña)
                    newpass = driver.find_element_by_id("Changepassword")
                    newpass.send_keys("Nuevacontraseña5")
                    click = driver.find_element_by_xpath('//*[@id="SavePasswodChange"]').click()
                elif opcion1 == 5:
                    break
                else: 
                    print("No existe esa opción")
        elif sitio == 3:
            break
        else:
            print("Opcion incorrecta")
