from services.election import delete_election, get_election
from config import DIRECTORY_PATH, TRUSTEE_NAME, NAME_ELECTION

import os


def clear_test():
    try:
        election = get_election(NAME_ELECTION)
        if election.status_code == 200:
            # Al terminar eliminamos la elección
            delete_election()

        # Eliminar archivo de trustee
        ruta_archivo = (
            f"{DIRECTORY_PATH}/trustee_key_{TRUSTEE_NAME}_{NAME_ELECTION}.txt"
        )
        if os.path.exists(ruta_archivo):
            os.remove(ruta_archivo)

        print("Datos limpiados")

    except Exception:
        raise ("No se ha podido limpiar luego de los test")
