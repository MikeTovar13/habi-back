import sys
sys.path.append('..')
from fastapi.testclient import TestClient
from main import app

# Test para obtener propietarios
def test_obtener_propietarios():
    client = TestClient(app)

    respose = client.get("/v1/propietario/obtener")
    json_body = respose.json()

    assert respose.status_code == 200
    assert "Mensaje" in json_body
    assert "propietarios" in json_body

# Test para crear propietarios
def test_crear_propietarios_correctamente():
    client = TestClient(app)
    body = {
        "nombre": "Propietario prueba",
        "telefono": "1230456789",
        "correo": "prueba@exaple.com"
    }

    respose = client.post("/v1/propietario/crear", json=body)
    json_body = respose.json()

    assert respose.status_code == 200
    assert "Mensaje" in json_body

# Test para crear propietario incorrecto
def test_crear_propietarios_incorrectamente():
    client = TestClient(app)
    body = {
        "nombre": "",
        "telefono": "",
        "correo": ""
    }

    respose = client.post("/v1/propietario/crear", json=body)

    assert respose.status_code == 422

# Test para eliminar propietarios
def test_eliminar_propietarios_correctamente():
    client = TestClient(app)
    body = {
        "id": 200
    }

    respose = client.post("/v1/propietario/eliminar", json=body)
    json_body = respose.json()

    assert respose.status_code == 200
    assert "Mensaje" in json_body

# Test para eliminar propietario incorrecto
def test_eliminar_propietarios_incorrectamente():
    client = TestClient(app)
    body = {
        "id": "e"
    }

    respose = client.post("/v1/propietario/eliminar", json=body)

    assert respose.status_code == 422