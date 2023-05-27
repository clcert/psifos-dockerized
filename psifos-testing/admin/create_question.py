from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config import URL_ADMIN, NAME_ELECTION, TIMEOUT
from services.election import get_election

import time

NUM_ANSWERS = 3


def check_question():
    response = get_election(NAME_ELECTION)
    if response.status_code != 200:
        raise Exception("La elección no se ha creado")

    json_data = response.json()
    if json_data["questions"] == "":
        raise Exception("Las preguntas no han sido creadas")


def create_question(driver):
    # Ir a la página web
    driver.get(f"{URL_ADMIN}/admin/{NAME_ELECTION}/panel")

    # Accedemos a crear una elección
    button_create_question = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "button-add-questions"))
    )
    button_create_question.click()

    # Completamos los formularios
    add_question = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "add-question"))
    )
    add_question.click()

    name_input = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "name-1"))
    )
    name_input.send_keys("Pregunta 1")

    # Enviamos los datos para crear
    button_add_option = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "add-option-1"))
    )

    for i in range(NUM_ANSWERS):
        # Ejecuta JavaScript para realizar el scroll hasta el final de la página
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(1)
        button_add_option.click()

        # Esperamos a la pantalla de inicio
        input_option = WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located((By.ID, f"text-option-{i}"))
        )
        input_option.send_keys(f"Respuesta {i + 1}")

    save_question = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "button-save-questions"))
    )
    save_question.click()

    # Esperamos a la pantalla de inicio
    WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "election-subtitle"))
    )

    check_question()
