from admin.main import admin_test
from trustee.main import trustee_test
from voter.main import voter_test
from utils import clear_test

if __name__ == "__main__":
    try:
        # Ejecutamos los test step_1 del administrador
        admin_test("step_1")

        # Ejecutamos los test del trustee
        trustee_test("step_1")

        # Ejecutamos los test step_2 del administrador
        admin_test("step_2")

        # Test del votante
        voter_test("step_1")

        # Ejecutamos los test step_3 del administrador
        admin_test("step_3")

        # Ejecutamos los test step_2 del trustee
        trustee_test("step_2")


    except Exception:
        raise ("Ha ocurrido un error")

    # Al terminar eliminamos la elección
    clear_test()
