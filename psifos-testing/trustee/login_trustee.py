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
)


def login_trustee(driver):
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
