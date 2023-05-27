from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config import URL_ADMIN, NAME_ELECTION, TIMEOUT, TRUSTEE_NAME
from services.election import get_election

import time

NUM_ANSWERS = 3


def check_trustee():
    response = get_election(NAME_ELECTION)

    json_data = response.json()
    trustees = json_data["trustees"]
    if len(trustees) == 0 and trustees[0]["name"] != "ahevia":
        raise Exception("El custodio no ha sido creado con exito")


def create_trustee(driver):
    # Ir a la página web
    driver.get(f"{URL_ADMIN}/admin/{NAME_ELECTION}/panel")

    # Accedemos a crear una elección
    button_create_trustee = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "button-add-trustee"))
    )
    button_create_trustee.click()

    # Entramos al formulario del custodio
    button_trustee = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "add-trustee"))
    )
    button_trustee.click()

    button_trustee_modal = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "next-trustee"))
    )
    button_trustee_modal.click()

    # Rellenamos el formulario del custodio
    trustee_name = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "trustee-name"))
    )
    trustee_name.send_keys(TRUSTEE_NAME)

    trustee_id = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "trustee-id"))
    )
    trustee_id.send_keys(TRUSTEE_NAME)

    trustee_email = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "trustee-email"))
    )
    trustee_email.send_keys(TRUSTEE_NAME)

    # Enviamos la información del custodio
    send_trustee = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "send-trustee"))
    )
    send_trustee.click()

    # Esperamos a la pantalla de inicio
    WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "election-subtitle"))
    )

    check_trustee()
