from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from config import (
    NAME_ELECTION,
    TIMEOUT,
    DIRECTORY_PATH,
    OPERATIVE_URL,
    TRUSTEE_NAME,
    TRUSTEE_PASSWORD,
)
from services.election import get_election

import time


def check_key():
    response = get_election(NAME_ELECTION)

    json_data = response.json()
    trustees = json_data["trustees"]
    if trustees[0]["public_key"] == "":
        raise Exception("La clave no ha sido generada con éxito")


def key_generator(driver):
    # Ir a la página web
    driver.get(f"{OPERATIVE_URL}/{NAME_ELECTION}/trustee/login")

    # Rellenamos el formulario del custodio
    trustee_name = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "id_username"))
    )
    trustee_name.send_keys(TRUSTEE_NAME)

    trustee_password = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "id_password"))
    )
    trustee_password.send_keys(TRUSTEE_PASSWORD)
    trustee_password.send_keys(Keys.ENTER)
    # Accedemos a la etapa 1
    button_key_generator = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "init-key-generator"))
    )
    button_key_generator.click()

    # Descargamos la key
    button_download_key = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "download-key"))
    )
    button_download_key.click()

    time.sleep(3)

    # Subimos el archivo
    drop_zone = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "file-input"))
    )
    drop_zone.send_keys(
        f"{DIRECTORY_PATH}/trustee_key_{TRUSTEE_NAME}_{NAME_ELECTION}.txt"
    )

    time.sleep(20)
    check_key()
