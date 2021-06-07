from starlette import responses
from settings import NUMBER_INMUEBLES_PAGE
from models.models import FiltrosModel, Inmuebles, ModelId
from datetime import date
from connect_db import ConnectDBSQLite
from fastapi import APIRouter


# Declaracion inial de rutas
inmueblesApp = APIRouter()


# Obtener inmuebles (Todos)
@inmueblesApp.post("/obtener")
def getInmuebles(filtros: FiltrosModel):

    filtros = filtros.dict()
    r_final = filtros["pagina"] * NUMBER_INMUEBLES_PAGE
    r_inicial = r_final - NUMBER_INMUEBLES_PAGE + 1

    query = f"""SELECT id, area, habitaciones, precio, direccion, localidad, propietario FROM(
        SELECT i.*,l.nombre localidad, p.nombre propietario,
            ROW_NUMBER() over(
            ORDER BY {"i.fecha_creacion" if filtros["orden"]["tipo"] == "fecha" else "l.nombre"} {filtros["orden"]["by"]}
            ) RowNum
        FROM inmueble i INNER JOIN localidad l ON l.id= i.id_localidad INNER JOIN propietario p ON p.id=i.id_propietario
        )a WHERE rownum BETWEEN {r_inicial} AND {r_final}"""

    conn = ConnectDBSQLite.getConnection()
    datos, _, error = ConnectDBSQLite.makeQuerys(conn, query)
    ConnectDBSQLite.closeDB(conn)

    inmuebles=[]
    for inmueble in datos:
        inmuebles.append({
            "id":inmueble[0],
            "area":inmueble[1],
            "habitaciones":inmueble[2],
            "precio":inmueble[3],
            "direccion":inmueble[4],
            "localidad":inmueble[5],
            "propietario":inmueble[6],

        })

    response = {
        "Mensaje":  error if error else "Inmuebles obtenidos correctamente",
        "inmuebles": inmuebles
    }

    return response


# Crear inmuebles (n)
@inmueblesApp.post("/crear")
def createInmueble(inmuebles: Inmuebles):

    inmuebles = inmuebles.dict()
    propietario_id = inmuebles["id_propietario"]
    fecha = str(date.today())
    fecha = {
        "fecha_creacion": fecha,
        "fecha_modificacion": fecha,
        "id_propietario": propietario_id
    }

    # Parametro recibido convertido a diccionario
    inmuebles = [{**inmueble, **fecha} for inmueble in inmuebles["inmuebles"]]

    query = """
        INSERT INTO inmueble (area, habitaciones, precio, direccion, id_localidad, id_propietario, fecha_creacion, fecha_modificacion) 
        VALUES 
        (:area, :habitaciones, :precio, :direccion, :id_localidad, :id_propietario, :fecha_creacion, :fecha_modificacion)
    """

    conn = ConnectDBSQLite.getConnection()
    _, _, error = ConnectDBSQLite.makeQuerys(conn, query, inmuebles, many=True)
    ConnectDBSQLite.closeDB(conn)

    response = {
        "Mensaje": error if error else f"{len(inmuebles)} inmueble(s) creado(s) correctamente"
    }

    return response


# Eliminar inmueble
@inmueblesApp.post("/eliminar")
def deleteInmueble(id: ModelId):

    id = id.dict()
    query = "DELETE FROM inmueble WHERE id= :id"
    conn = ConnectDBSQLite.getConnection()
    _, _, error = ConnectDBSQLite.makeQuerys(conn, query, id)
    ConnectDBSQLite.closeDB(conn)

    response = {
        "Mensaje": error if error else "Inmueble eliminado correctamente"
        }

    return response
