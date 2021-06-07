from connect_db import ConnectDBSQLite
from fastapi import APIRouter

# Declaracion inicial de rutas
utilsApp = APIRouter()


# Obtener ciudades (Todas)
@utilsApp.get("/ciudades")
def getCiudades():

    query = "SELECT id, nombre FROM ciudad ORDER BY nombre"
    conn = ConnectDBSQLite.getConnection()
    data, _, error = ConnectDBSQLite.makeQuerys(conn, query)
    ConnectDBSQLite.closeDB(conn)

    ciudades = [{"id": ciudad[0], "nombre":ciudad[1]} for ciudad in data]

    response = {
        "Mensaje": error if error else "Ciudades obtenidas correctamente",
        "ciudades": ciudades
    }
    return response


# Obtener localidades por ciudad (Todas), se requiere el id de la ciudad
@utilsApp.get("/localidades")
def getLocalidades(id: int):

    query = "SELECT id, nombre FROM localidad WHERE id_ciudad = ? ORDER BY nombre"
    conn = ConnectDBSQLite.getConnection()
    data, _, error = ConnectDBSQLite.makeQuerys(conn, query, (id,))
    ConnectDBSQLite.closeDB(conn)

    localidades = [{"id": localidad[0], "nombre":localidad[1]}
                   for localidad in data]

    response = {
        "Mensaje": error if error else "Localidades obtenidas correctamente",
        "localidades": localidades
    }
    return response
