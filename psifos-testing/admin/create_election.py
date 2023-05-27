from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config import URL_ADMIN, NAME_ELECTION, TIMEOUT
from services.election import get_election

import time

def check_election():

    response = get_election(NAME_ELECTION)
    if response.status_code != 200:
        raise Exception("La elección no se ha creado con exito")


def create_election(driver):
    # Ir a la página web
    driver.get(f"{URL_ADMIN}/admin/home")

    # Accedemos a crear una elección
    button_create = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "button-create-election"))
    )
    button_create.click()

    # Completamos los formularios
    short_name_input = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "input-short-name"))
    )
    short_name_input.send_keys(NAME_ELECTION)

    name_input = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "input-name"))
    )
    name_input.send_keys(NAME_ELECTION)

    # Ejecuta JavaScript para realizar el scroll hasta el final de la página
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(1)

    # Enviamos los datos para crear
    button_send = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "button-send-election"))
    )
    button_send.click()

    # Esperamos a la pantalla de inicio
    WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "election-subtitle"))
    )

    check_election()
