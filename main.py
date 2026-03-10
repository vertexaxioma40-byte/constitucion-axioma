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
        <title>Vertex Axioma® - Nodo de Integridad</title>
        <style>
            body { background-color: #0d1117; color: #58a6ff; font-family: 'Segoe UI', sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; margin: 0; }
            .bunker { border: 1px solid #30363d; padding: 40px; border-radius: 15px; background: #161b22; text-align: center; box-shadow: 0 20px 50px rgba(0,0,0,0.7); max-width: 450px; width: 90%; }
            h1 { color: #ffffff; margin: 0; font-size: 26px; letter-spacing: 3px; font-weight: 800; }
            .subtitle { color: #8b949e; margin-bottom: 30px; font-size: 11px; text-transform: uppercase; letter-spacing: 2px; }
            input { padding: 15px; width: 85%; border-radius: 8px; border: 1px solid #30363d; background: #0d1117; color: #ffffff; text-align: center; margin-bottom: 15px; font-family: monospace; }
            button { padding: 15px; background: #238636; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; width: 93%; transition: 0.3s; }
            button:hover { background: #2ea043; }
            
            #certificado { display: none; margin-top: 25px; padding: 20px; border: 1px solid #3fb950; border-radius: 10px; background: #0d1117; text-align: left; animation: fadeIn 0.5s; }
            .seal-header { color: #3fb950; font-weight: bold; border-bottom: 1px solid #3fb950; padding-bottom: 8px; margin-bottom: 15px; font-size: 14px; display: flex; align-items: center; gap: 10px; }
            .data-row { font-size: 12px; color: #c9d1d9; margin-bottom: 8px; line-height: 1.4; }
            .footer { margin-top: 30px; font-size: 9px; color: #484f58; letter-spacing: 1px; border-top: 1px solid #21262d; padding-top: 15px; }
            @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
        </style>
    </head>
    <body>
        <div class="bunker">
            <h1>VERTEX AXIOMA®</h1>
            <div class="subtitle">INFRAESTRUCTURA FORENSE 4.0</div>
            
            <div id="ui-box">
                <input type="text" id="hash-input" placeholder="INGRESE ID O HASH">
                <button onclick="procesar()">VALIDAR INTEGRIDAD</button>
            </div>

            <div id="certificado">
                <div class="seal-header">🛡️ SELLO DE CONFORMIDAD FISCAL 4.0</div>
                <div class="data-row"><b>NODO EMISOR:</b> VERTEX (MORÓN)</div>
                <div class="data-row"><b>ESTADO:</b> PRUEBA PETRIFICADA</div>
                <div class="data-row"><b>HASH DNA:</b> <br><span id="res-hash" style="color:#58a6ff; font-family:monospace; font-size:10px;"></span></div>
                <div class="data-row"><b>PROTOCOLO:</b> Inmutabilidad Transfronteriza</div>
                <button style="background:#1f6feb; width:100%; margin-top:10px;" onclick="window.print()">DESCARGAR CERTIFICADO</button>
            </div>
            
            <div class="footer">NODO MORÓN | OPERATIVO | PROTOCOLO AXIOMA®</div>
        </div>

        <script>
            function procesar() {
                const val = document.getElementById('hash-input').value;
                if(val.length > 4) {
                    document.getElementById('res-hash').innerText = val;
                    document.getElementById('ui-box').style.display = 'none';
                    document.getElementById('certificado').style.display = 'block';
                } else {
                    alert("Error: Identificador inválido.");
                }
            }
        </script>
    </body>
    </html>
    """
