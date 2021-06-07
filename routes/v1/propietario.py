from models.models import ModelId, PropietarioModel
from datetime import date
from connect_db import ConnectDBSQLite
from fastapi import APIRouter

# Declaracion inicial de rutas
propietarioApp = APIRouter()


# Obtener propietarios (Todos)
@propietarioApp.get("/obtener")
def getPropietarios():

    query = """
        SELECT * FROM propietario
    """

    conn = ConnectDBSQLite.getConnection()
    data, _, error = ConnectDBSQLite.makeQuerys(conn, query)
    ConnectDBSQLite.closeDB(conn)

    propietarios = []

    for propietario in data:
        propietarios.append({
            "id": propietario[0],
            "nombre": propietario[1],
            "telefono": propietario[2],
            "correo": propietario[3]
        })

    response = {
        "Mensaje": error if error else "Lista de propietarios obtenida correctamente",
        "propietarios": propietarios
    }

    return response


# Crear propietario
@propietarioApp.post("/crear")
def createPropietario(propietario: PropietarioModel):

    fecha = str(date.today())

    # Parametro recibido convertido a diccionario
    propietario = propietario.dict()
    propietario["fecha_creacion"] = fecha
    propietario["fecha_modificacion"] = fecha

    query = """
        INSERT INTO propietario (nombre, telefono, correo, fecha_creacion, fecha_modificacion) 
        VALUES 
        (:nombre, :telefono, :correo, :fecha_creacion, :fecha_modificacion)
    """

    conn = ConnectDBSQLite.getConnection()
    _, _, error = ConnectDBSQLite.makeQuerys(conn, query, propietario)
    ConnectDBSQLite.closeDB(conn)

    response = {
        "Mensaje": error if error else "Propietario creado correctamente"
    }

    return response


# Eliminar propietario e inmubeles
@propietarioApp.post("/eliminar")
def deletePropietario(id: ModelId):

    id = id.dict()
    conn = ConnectDBSQLite.getConnection()

    query_propietario = """
        DELETE FROM propietario WHERE id = :id
    """

    _, _, error = ConnectDBSQLite.makeQuerys(
        conn, query_propietario, id)

    ConnectDBSQLite.closeDB(conn)

    response = {
        "Mensaje": error if error else "Propietario eliminado correctamente"
    }

    return response
