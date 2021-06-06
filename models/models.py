from typing import Text
from pydantic import BaseModel
from typing import Text, Optional, List

# Validaciones de data para propietarios
class Propietario(BaseModel):
    id: Optional[int]
    nombre: Text
    telefono: Text
    correo: Text

# Validaciones de data para cada inmueble 
class Inmueble(BaseModel):
    id: Optional[int]
    area: float
    habitaciones: int
    precio: int
    direccion: Text
    id_localidad: int

# Validaciones de data para inmuebles enviados (n)
class Inmuebles(BaseModel):
    inmuebles: List[Inmueble]

class ModelId(BaseModel):
    id: int