from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
async def read_root():
    # Esta redirección mantiene el motor activo pero lleva al usuario a la estética
    return RedirectResponse(url="https://gamma.app/docs/VERTEX-AXIOMA-samkfi5i67siphz")

@app.get("/status")
async def get_status():
    return {"Nodo": "Vertex Axioma®", "Estado": "Activo", "Protocolo": "Auditoría 4.0"}
