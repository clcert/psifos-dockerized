from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config import NAME_ELECTION, TIMEOUT, DOWNLOAD_PATH, TRUSTEE_NAME
from services.election import get_election


def check_decrypt(element):
    print(element.text)
    if element.text != "Desencriptación Parcial enviada exitosamente ✓":
        raise Exception("Las desencriptaciones no han sido calculados")


def decrypt(driver):
    # Accedemos a la etapa 3
    button_decrypt = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "upload-key"))
    )
    button_decrypt.click()

    # Subimos el archivo
    drop_zone = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "file-input"))
    )
    drop_zone.send_keys(
        f"{DOWNLOAD_PATH}/trustee_key_{TRUSTEE_NAME}_{NAME_ELECTION}.txt"
    )

    # Esperamos a que el proceso se complete
    feedback = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "feedback-message-2"))
    )

    check_decrypt(feedback)
