from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {
        "Nodo": "Vertex Axioma®",
        "Estado": "Operativo",
        "Protocolo": "Auditoría Forense 4.0",
        "Certificación": "SHA-256 Activa",
        "Mensaje": "El motor de integridad está encendido y esperando datos."
    }
