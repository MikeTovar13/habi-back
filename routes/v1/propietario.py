from models.models import ModelId, Propietario
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
    data,_,error = ConnectDBSQLite.makeQuerys(conn, query)
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
        "propietarios": propietarios}

    return response

# Crear propietario
@propietarioApp.post("/crear")
def createPropietario(propietario: Propietario):
    
    fecha = str(date.today())

    #Parametro recibido convertido a diccionario
    propietario = propietario.dict() 
    propietario["fecha_creacion"] = fecha
    propietario["fecha_modificacion"] = fecha

    query = """
        INSERT INTO propietario (nombre, telefono, correo, fecha_creacion, fecha_modificacion) 
        values 
        (:nombre, :telefono, :correo, :fecha_creacion, :fecha_modificacion)
    """

    conn = ConnectDBSQLite.getConnection()
    _,_,error = ConnectDBSQLite.makeQuerys(conn, query, propietario)
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

    # Querys de borrado
    query_inmueble = """
        SELECT * FROM inmueble WHERE
        id in (SELECT id_inmueble FROM propietario_inmueble WHERE id_propietario = :id)
    """

    query_relacion = """
        SELECT * FROM propietario_inmueble WHERE id_propietario = :id
    """

    query_propietario = """
        SELECT * FROM propietario WHERE id = :id
    """

    # Ejecucion de querys
    data_relacion,_,error_relacion = ConnectDBSQLite.makeQuerys(conn, query_relacion, id) 
    print(data_relacion)

    data_inmueble,_,error_inmueble = ConnectDBSQLite.makeQuerys(conn, query_inmueble, id) 
    print(data_inmueble)

    data_propietario,_,error_propietario = ConnectDBSQLite.makeQuerys(conn, query_propietario, id) 
    print(data_propietario)

    ConnectDBSQLite.closeDB(conn)

    response = {}
    if error_inmueble or error_relacion or error_propietario:
        response = {"Mensaje" : (f"Error en inmueble {error_inmueble}, Error en relacion {error_relacion}, Error en propietario {error_propietario}")}
    else:
        response = {"Mensaje": "Propietario e inmuebles eliminados correctamente"}

    return response

