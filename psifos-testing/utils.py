from services.election import delete_election
from config import DOWNLOAD_PATH, TRUSTEE_NAME, NAME_ELECTION

import os


def clear_test():
    try:
        # Al terminar eliminamos la elección
        delete_election()

        # Eliminar archivo de trustee
        ruta_archivo = f"{DOWNLOAD_PATH}/trustee_key_{TRUSTEE_NAME}_{NAME_ELECTION}.txt"
        os.remove(ruta_archivo)

    except Exception:
        raise ("No se ha podido limpiar luego de los test")
