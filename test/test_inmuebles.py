from main import app
from fastapi.testclient import TestClient
import sys
sys.path.append('..')


# Test para obtener inmuebles
def test_obtener_inmuebles_correctamente():
    client = TestClient(app)
    body = {
        "orden": {
            "tipo": "fecha",
            "by": "ASC"
        }
    }

    respose = client.post("/v1/inmueble/obtener", json=body)
    json_body = respose.json()

    assert respose.status_code == 200
    assert "Mensaje" in json_body
    assert "inmuebles" in json_body


# Test para obtener inmuebles
def test_obtener_inmuebles_incorrectamente():
    client = TestClient(app)
    body = {
        "orden": "Prueba"
    }

    respose = client.post("/v1/inmueble/obtener", json=body)

    assert respose.status_code == 422


# Test para crear inmuebles
def test_crear_inmuebles_correctamente():
    client = TestClient(app)
    body = {
        "inmuebles": [
            {
                "area": 10,
                "habitaciones": 1,
                "direccion": "Calle falsa 123",
                "id_localidad": 1,
                "precio": 100000000
            }
        ],
        "id_propietario": 1
    }

    respose = client.post("/v1/inmueble/crear", json=body)
    json_body = respose.json()

    assert respose.status_code == 200
    assert "Mensaje" in json_body


# Test para crear inmueble incorrecto
def test_crear_inmuebles_incorrectamente():
    client = TestClient(app)
    body = {
        "inmuebles": [
            {
                "area": "",
                "habitaciones": "",
                "direccion": "",
                "id_localidad": "",
                "precio": ""
            }
        ],
        "id_propietario": 1
    }

    respose = client.post("/v1/inmueble/crear", json=body)

    assert respose.status_code == 422


# Test para eliminar inmuebles
def test_eliminar_inmuebles_correctamente():
    client = TestClient(app)
    body = {
        "id": 200
    }

    respose = client.post("/v1/inmueble/eliminar", json=body)
    json_body = respose.json()

    assert respose.status_code == 200
    assert "Mensaje" in json_body


# Test para eliminar inmueble incorrecto
def test_eliminar_inmuebles_incorrectamente():
    client = TestClient(app)
    body = {
        "id": "e"
    }

    respose = client.post("/v1/inmueble/eliminar", json=body)

    assert respose.status_code == 422
