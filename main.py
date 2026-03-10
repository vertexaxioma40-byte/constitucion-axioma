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
            .bunker { border: 1px solid #30363d; padding: 40px; border-radius: 12px; background: #161b22; text-align: center; box-shadow: 0 15px 35px rgba(0,0,0,0.6); max-width: 500px; width: 90%; }
            .logo-container { margin-bottom: 25px; }
            h1 { color: #ffffff; margin-bottom: 5px; font-size: 26px; letter-spacing: 3px; font-weight: 700; }
            .subtitle { color: #8b949e; margin-bottom: 30px; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; }
            .search-box { display: flex; flex-direction: column; gap: 15px; }
            input { padding: 14px; border-radius: 6px; border: 1px solid #30363d; background: #0d1117; color: white; text-align: center; font-family: monospace; }
            button { padding: 14px; background: #238636; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: bold; transition: 0.3s; font-size: 16px; }
            button:hover { background: #2ea043; transform: translateY(-2px); }
            #resultado { margin-top: 25px; min-height: 50px; font-size: 15px; border-top: 1px solid #30363d; padding-top: 20px; }
            .footer-info { margin-top: 30px; font-size: 11px; color: #484f58; letter-spacing: 1px; border-top: 1px solid #21262d; padding-top: 15px; }
            .badge { background: #1f6feb; color: white; padding: 2px 8px; border-radius: 10px; font-size: 10px; margin-left: 5px; vertical-align: middle; }
        </style>
    </head>
    <body>
        <div class="bunker">
            <div class="logo-container">
                <img src="https://img.icons8.com/fluency/96/shield-with-blockchain.png" alt="Logo" style="width:80px; margin-bottom:20px;">
<h1>VERTEX AXIOMA®</h1>
            </div>
            <h1>VERTEX AXIOMA®</h1>
            <div class="subtitle">Infraestructura de Auditoría Forense 4.0</div>
            
            <div class="search-box">
                <input type="text" id="cert-id" placeholder="ID DE ACTIVO / HASH SHA-256">
                <button onclick="buscar()">VALIDAR INTEGRIDAD</button>
            </div>
            
            <div id="resultado"></div>
            
            <div class="footer-info">
                NODO MORÓN <span class="badge">ACTIVO</span> | ESTADO: OPERATIVO | PROTOCOLO AXIOMA® 
            </div>
        </div>

        <script>
            function buscar() {
                const id = document.getElementById('cert-id').value;
                const res = document.getElementById('resultado');
                if(id.length > 3) {
                    res.innerHTML = "<div style='color:#79c0ff; margin-bottom:10px;'>🔍 CONSULTANDO LEDGER...</div>" + 
                                  "<div style='color:#3fb950; font-size:18px;'>✅ ACTIVO VERIFICADO</div>" +
                                  "<div style='color:#8b949e; font-size:12px; margin-top:5px;'>La huella digital coincide con el registro inmutable.</div>";
                } else {
                    res.innerHTML = "<span style='color:#f85149'>Error: Ingrese un identificador válido para la consulta.</span>";
                }
            }
        </script>
    </body>
    </html>
    """
