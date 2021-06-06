from os import terminal_size
from models.models import Inmuebles
from datetime import date
from connect_db import ConnectDBSQLite
from fastapi import APIRouter

# Declaracion inial de rutas
inmueblesApp = APIRouter()

# Obtener inmuebles (Todos)


@inmueblesApp.get("/obtener")
def getInmuebles():
    return {"Mensaje": "Hola mundo"}

# Crear inmuebles (n)


@inmueblesApp.post("/crear")
def createInmueble(inmuebles: Inmuebles):

    fecha = str(date.today())
    fecha = {
        "fecha_creacion": fecha,
        "fecha_modificacion": fecha
    }

    # Parametro recibido convertido a diccionario
    inmuebles = inmuebles.dict()["inmuebles"]
    inmuebles = [{**inmueble, **fecha} for inmueble in inmuebles]

    query = """
        INSERT INTO inmueble (area, habitaciones, precio, direccion, id_localidad, fecha_creacion, fecha_modificacion) 
        values 
        (:area, :habitaciones, :precio, :direccion, :id_localidad, :fecha_creacion, :fecha_modificacion)
    """

    conn = ConnectDBSQLite.getConnection()
    _, _, error = ConnectDBSQLite.makeQuerys(conn, query, inmuebles, many=True)
    ConnectDBSQLite.closeDB(conn)

    response = {
        "Mensaje": error if error else "Inmueble creado correctamente"
    }

    return response


# Eliminar inmueble
@inmueblesApp.post("/eliminar")
def deleteInmueble():
    return {"Apto": "Eliminado"}
