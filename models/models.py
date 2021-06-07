from typing import Text
from pydantic import BaseModel
from typing import Text, Optional, List, Dict


# Validaciones de datos para propietarios
class PropietarioModel(BaseModel):
    id: Optional[int]
    nombre: Text
    telefono: Text
    correo: Text


# Validaciones de datos para cada inmueble
class Inmueble(BaseModel):
    id: Optional[int]
    area: float
    habitaciones: int
    precio: int
    direccion: Text
    id_localidad: int


# Validaciones de listado de inmuebles a crear
class Inmuebles(BaseModel):
    inmuebles: List[Inmueble]
    id_propietario: int


# Validaciones de envio de id
class ModelId(BaseModel):
    id: int


# Validaciones de datos para filtros
class FiltrosModel(BaseModel):
    pagina: int
    orden: Dict[str, str]
