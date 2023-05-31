from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config import OPERATIVE_URL, NAME_ELECTION, TIMEOUT, DIRECTORY_PATH, TRUSTEE_NAME, TRUSTEE_PASSWORD, LOGIN_SITE


def check_key(element):
    if element.text != "Clave verificada exitosamente ✔":
        raise ("La clase no se ha verificado correctamente")


def check_sk(driver):
    # Ir a la página web
    driver.get(f"{OPERATIVE_URL}/{NAME_ELECTION}/trustee/login")

    if LOGIN_SITE == "uchile":
        # Rellenamos el formulario del custodio
        trustee_name = WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located((By.ID, "usernameInput"))
        )
        trustee_name.send_keys(TRUSTEE_NAME)

        trustee_password = WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located((By.ID, "passwordInput"))
        )
        trustee_password.send_keys(TRUSTEE_PASSWORD)
    
        trustee_password.send_keys(Keys.ENTER)

    # Accedemos a la etapa 1
    button_key_generator = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "verify-key"))
    )
    button_key_generator.click()

    # Subimos el archivo
    drop_zone = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "file-input"))
    )
    drop_zone.send_keys(
        f"{DIRECTORY_PATH}/trustee_key_{TRUSTEE_NAME}_{NAME_ELECTION}.txt"
    )

    # Esperamos a que el proceso se complete
    finish_check = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "feedback-check"))
    )

    check_key(finish_check)
