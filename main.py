from fastapi import FastAPI
import uvicorn
from routes.v1.inmuebles import inmueblesApp
from routes.v1.propietario import propietarioApp
from routes.v1.utils import utilsApp
from fastapi.middleware.cors import CORSMiddleware

# Routes de servicios
app = FastAPI(title="Habi Backend", version="1.0.0")
app.include_router(inmueblesApp, prefix="/v1/inmueble")
app.include_router(propietarioApp, prefix="/v1/propietario")
app.include_router(utilsApp, prefix="/v1/utils")

# Cors Allowed
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicio de ejecucion
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
