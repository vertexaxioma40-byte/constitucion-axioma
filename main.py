from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Vertex Axioma® - Nodo de Auditoría</title>
        <style>
            body { background-color: #0d1117; color: #58a6ff; font-family: sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; margin: 0; text-align: center; }
            .bunker { border: 1px solid #30363d; padding: 40px; border-radius: 15px; background: #161b22; box-shadow: 0 20px 50px rgba(0,0,0,0.7); max-width: 500px; width: 90%; }
            .shield { font-size: 60px; margin-bottom: 10px; }
            h1 { color: #ffffff; margin: 10px 0; font-size: 24px; letter-spacing: 2px; }
            .subtitle { color: #8b949e; margin-bottom: 30px; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; border-bottom: 1px solid #30363d; padding-bottom: 10px; }
            input { padding: 15px; width: 85%; border-radius: 8px; border: 1px solid #30363d; background: #0d1117; color: #ffffff; text-align: center; margin-bottom: 15px; font-family: monospace; }
            button { padding: 15px; background: #238636; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; width: 92%; font-size: 14px; }
            #certificado { display: none; margin-top: 25px; padding: 20px; border: 1px solid #3fb950; border-radius: 10px; background: #0d1117; text-align: left; }
            .seal-title { color: #3fb950; font-weight: bold; border-bottom: 1px solid #3fb950; padding-bottom: 10px; margin-bottom: 15px; text-transform: uppercase; font-size: 14px; }
            .footer { margin-top: 25px; font-size: 10px; color: #484f58; letter-spacing: 1px; }
        </style>
    </head>
    <body>
        <div class="bunker">
            <div class="shield">🛡️</div>
            <h1>VERTEX AXIOMA®</h1>
            <div class="subtitle">Infraestructura de Integridad & Auditoría 4.0</div>
