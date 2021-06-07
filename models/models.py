from typing import Text
from pydantic import BaseModel, Field
from typing import Text, Optional, List, Dict


# Validaciones de datos para propietarios
class PropietarioModel(BaseModel):
    id: Optional[int]
    nombre: Text = Field(min_length=1)
    telefono: Text = Field(min_length=1)
    correo: Text = Field(min_length=1)


# Validaciones de datos para cada inmueble
class Inmueble(BaseModel):
    id: Optional[int]
    area: float
    habitaciones: int
    precio: int
    direccion: Text = Field(min_length=1)
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
    orden: Dict[str, str]
