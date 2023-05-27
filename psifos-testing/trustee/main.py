from trustee.key_generator import key_generator
from trustee.check_key import check_sk
from trustee.decrypt import decrypt
from trustee.login_trustee import login_trustee
from selenium import webdriver

import traceback


def trustee_test(actual_step):
    steps = {
        "step_1": {
            "key_generator": key_generator,
            "check_sk": check_sk,
        },
        "step_2": {"login_trustee": login_trustee, "decrypt": decrypt},
    }

    options = webdriver.FirefoxOptions()
    options.add_argument("--private")
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.dir", "ruta_de_la_carpeta")
    options.set_preference(
        "browser.helperApps.neverAsk.saveToDisk", "application/octet-stream"
    )

    # Abrimos el navegador
    driver = webdriver.Firefox(options=options)

    step = steps[actual_step]

    print("======TRUSTEE-TEST======")
    for index, (name, test) in enumerate(step.items()):
        try:
            print(f"\nEjecutando prueba {name} {index + 1}/{len(step)}")
            test(driver)
            print(f"Prueba {name} correcta ✓\n")

        except Exception as e:
            print(f"Ha ocurrido un error en la prueba {index + 1} x")
            print(e)
            traceback.print_exc()
            driver.quit()

    driver.quit()
