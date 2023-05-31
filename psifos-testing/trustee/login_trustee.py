from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from config import (
    OPERATIVE_URL,
    NAME_ELECTION,
    TIMEOUT,
    TRUSTEE_NAME,
    TRUSTEE_PASSWORD,
    LOGIN_SITE
)


def login_trustee(driver):
    # Ir a la página web
    driver.get(f"{OPERATIVE_URL}/{NAME_ELECTION}/trustee/login")

    if LOGIN_SITE == "clcert":
        username_element_id = "id_username"
        password_element_id = "id_password"
    if LOGIN_SITE == "uchile":
        username_element_id = "usernameInput"
        password_element_id = "passwordInput"

    # Rellenamos el formulario del custodio
    trustee_name = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, username_element_id))
    )
    trustee_name.send_keys(TRUSTEE_NAME)

    trustee_password = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, password_element_id))
    )
    trustee_password.send_keys(TRUSTEE_PASSWORD)
    
    trustee_password.send_keys(Keys.ENTER)
