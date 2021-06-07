import sys
sys.path.append('..')
from fastapi.testclient import TestClient
from main import app

# Test para obtener ciudades
def test_obtener_ciudades():
    client = TestClient(app)

    respose = client.get("/v1/utils/ciudades")
    json_body = respose.json()

    assert respose.status_code == 200
    assert "Mensaje" in json_body
    assert "ciudades" in json_body

# Test para obtener localidades
def test_obtener_localidades_correctamente():
    client = TestClient(app)

    respose = client.get("/v1/utils/localidades?id=1")
    json_body = respose.json()

    assert respose.status_code == 200
    assert "Mensaje" in json_body
    assert "localidades" in json_body

# Test fallido de parametro get() faltante en localidades
def test_obtener_localidades_incorrectamente():
    client = TestClient(app)

    respose = client.get("/v1/utils/localidades")

    assert respose.status_code == 422 # not found param id