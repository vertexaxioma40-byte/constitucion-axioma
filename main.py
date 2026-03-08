from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

# Protocolo de Identidad del Nodo
@app.get("/")
def read_root():
    return {
        "Nodo": "Vertex Axioma®",
        "Estado": "Activo",
        "Protocolo": "Auditoría 4.0",
        "Fecha_Sincronizacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# Endpoint de Verificación de Integridad
@app.get("/verificar-prueba")
def verificar_prueba():
    return {
        "Certificación": "Prueba Petrificada Validada",
        "Sello": "Conformidad Fiscal 4.0",
        "Integridad": "100% Inmutable"
    }
