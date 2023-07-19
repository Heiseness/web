"""
pip install selenium
pip install webdriver_manager
pip install csv

"""

import csv
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"Funcion de llenado"
def llenado(pn,dpt):
    button = driver.find_element(By.NAME,"login")
    pn_input = driver.find_element(By.ID, "email")
    dpt_input = driver.find_element(By.ID, "pass")
    pn_input.clear()
    pn_input.send_keys(pn)
    dpt_input.clear()
    dpt_input.send_keys(dpt)
    button.click()


"entral cpts"

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get("https://www.facebook.com/")

correct_password = False

form = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "login_form")))

while not correct_password:
    try:
        error_message = driver.find_element(By.ID, "error_box")
        if  error_message.is_displayed:
            print("error de usuario: ", error_message)
            WebDriverWait(driver, 15).until(EC.staleness_of(form))
    except NoSuchElementException:
        correct_password = True
print("Inicio exitoso")



"""
# Encuentra el elemento de búsqueda por su atributo 'id'
with open('test.csv','r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    pn_index = headers.index('np')
    dpt_index = headers.index('dpt')

    for row in reader:
        pn = row[pn_index]
        dpt = row[dpt_index]
        llenado(pn,dpt)
"""
