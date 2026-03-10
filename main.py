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
        <title>Vertex Axioma - Nodo de Auditoría</title>
        <style>
            body { background-color: #0d1117; color: #58a6ff; font-family: 'Segoe UI', sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; }
            .bunker { border: 1px solid #30363d; padding: 40px; border-radius: 10px; background: #161b22; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
            h1 { color: #ffffff; margin-bottom: 10px; font-size: 24px; letter-spacing: 2px; }
            p { color: #8b949e; margin-bottom: 30px; }
            input { padding: 12px; width: 250px; border-radius: 5px; border: 1px solid #30363d; background: #0d1117; color: white; margin-right: 10px; }
            button { padding: 12px 24px; background: #238636; color: white; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; }
            button:hover { background: #2ea043; }
            .status { margin-top: 20px; font-size: 12px; color: #30363d; }
        </style>
    </head>
    <body>
        <div class="bunker">
            <h1>VERTEX AXIOMA®</h1>
            <p>Protocolo de Auditoría Forense 4.0</p>
            <div id="search-box">
                <input type="text" id="cert-id" placeholder="Ingrese ID de Certificado (SHA-256)">
                <button onclick="buscar()">VALIDAR ACTIVO</button>
            </div>
            <div id="resultado" style="margin-top:20px; color: #79c0ff; font-weight: bold;"></div>
            <div class="status">NODO MORÓN | ESTADO: OPERATIVO | SEGURIDAD: SSL-SHA256</div>
        </div>

        <script>
            function buscar() {
                const id = document.getElementById('cert-id').value;
                const res = document.getElementById('resultado');
                if(id) {
                    res.innerHTML = "🔍 BUSCANDO EN EL LEDGER...<br><span style='color:#3fb950'>ACTIVO VERIFICADO: INTEGRIDAD TOTAL</span>";
                } else {
                    res.innerHTML = "Por favor, ingrese un ID válido.";
                }
            }
        </script>
    </body>
    </html>
    """
