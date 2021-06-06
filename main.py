from models.models import Propietario
from fastapi import FastAPI
import uvicorn
from routes.v1.inmuebles import inmueblesApp
from routes.v1.propietario import propietarioApp

app = FastAPI(title="Habi Backend", version="1.0.0")
app.include_router(inmueblesApp, prefix="/v1/inmueble")
app.include_router(propietarioApp, prefix="/v1/propietario")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)