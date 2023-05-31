from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from config import OPERATIVE_URL, NAME_ELECTION, TIMEOUT, VOTER_NAME, VOTER_PASSWORD, LOGIN_SITE


def vote_normal(driver):
    # Ir a la página web
    driver.get(f"{OPERATIVE_URL}/{NAME_ELECTION}/vote")

    if LOGIN_SITE == "clcert":
        username_element_id = "id_username"
        password_element_id = "id_password"
    if LOGIN_SITE == "uchile":
        username_element_id = "usernameInput"
        password_element_id = "passwordInput"

    # Rellenamos el formulario del votante
    trustee_name = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, username_element_id))
    )
    trustee_name.send_keys(VOTER_NAME)

    trustee_password = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, password_element_id))
    )
    trustee_password.send_keys(VOTER_PASSWORD)
    
    trustee_password.send_keys(Keys.ENTER)

    # Elegimos la alternativa
    input_answers = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.NAME, "answer_0"))
    )
    input_answers.click()

    # Siguiente
    next_button = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "next-button"))
    )
    next_button.click()

    # Enviar voto
    send_button = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "proceed_button"))
    )
    send_button.click()

    # El voto ha sido enviado con exito
    WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "back-vote-button"))
    )
