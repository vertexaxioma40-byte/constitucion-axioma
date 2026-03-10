from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# BASE DE DATOS DE ACTIVOS
db = {
    "AX-2026-DRON01": "Dato Geoespacial - Relevamiento Morón - Sector A1",
    "SHA-256-VADELL-01": "Certificación de Activos 4.0 - Auditoría Tributaria",
    "PROTOCOLO-AXIOMA-77": "Prueba Petrificada - Integridad Forense"
}

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
            body { background-color: #0d1117; color: #c9d1d9; font-family: 'Segoe UI', sans-serif; margin: 0; display: flex; flex-direction: column; align-items: center; }
            .hero { padding: 60px 20px; text-align: center; width: 100%; background: radial-gradient(circle, #161b22 0%, #0d1117 100%); }
            .bunker { border: 1px solid #30363d; padding: 40px; border-radius: 15px; background: #161b22; box-shadow: 0 20px 50px rgba(0,0,0,0.7); max-width: 450px; margin: 0 auto; }
            h1 { color: #ffffff; margin: 0; font-size: 28px; letter-spacing: 4px; font-weight: 800; }
            .subtitle { color: #58a6ff; margin-bottom: 30px; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; }
            
            input { padding: 15px; width: 85%; border-radius: 8px; border: 1px solid #30363d; background: #0d1117; color: #ffffff; text-align: center; margin-bottom: 15px; font-family: monospace; }
            button { padding: 15px; background: #238636; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; width: 93%; transition: 0.3s; }
            
            #certificado, #error-box { display: none; margin-top: 25px; padding: 20px; border-radius: 10px; text-align: left; }
            #certificado { border: 1px solid #3fb950; background: rgba(63, 185, 80, 0.05); }
            #error-box { border: 1px solid #f85149; background: rgba(248, 81, 73, 0.05); color: #f85149; }
            
            .constitucion-section { max-width: 800px; padding: 60px 20px; width: 90%; }
            .constitucion-title { color: #ffffff; font-size: 20px; border-bottom: 2px solid #58a6ff; padding-bottom: 10px; margin-bottom: 30px; text-align: center; letter-spacing: 2px; }
            .grid-constitucion { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; }
            .item-c { background: #161b22; padding: 15px; border-radius: 8px; border: 1px solid #30363d; font-size: 13px; transition: 0.3s; }
            .item-c:hover { border-color: #58a6ff; transform: translateY(-5px); }
            .item-num { color: #58a6ff; font-weight: bold; margin-right: 5px; }

            .footer { padding: 40px; font-size: 10px; color: #484f58; letter-spacing: 1px; text-align: center; }
        </style>
    </head>
    <body>
        <section class="hero">
            <div class="bunker">
                <h1>VERTEX AXIOMA®</h1>
                <div class="subtitle">INFRAESTRUCTURA FORENSE 4.0</div>
                <div id="ui-box">
                    <input type="text" id="hash-input" placeholder="VALIDAR HASH O ACTIVO">
                    <button onclick="procesar()">VALIDAR INTEGRIDAD</button>
                </div>
                <div id="certificado">
                    <div style="color:#3fb950; font-weight:bold; margin-bottom:15px; font-size:14px;">🛡️ SELLO DE CONFORMIDAD FISCAL 4.0</div>
                    <div style="font-size:12px; line-height:1.6;">
                        <b>ESTADO:</b> VERIFICADO<br>
                        <b>ORIGEN:</b> <span id="res-desc"></span><br>
                        <b>HASH:</b> <span id="res-hash" style="color:#58a6ff;"></span><br>
                        <b>Sello de Inmutabilidad Transfronteriza ACTIVADO</b>
                    </div>
                    <button style="background:#1f6feb; width:100%; margin-top:15px;" onclick="window.print()">DESCARGAR CERTIFICADO</button>
                </div>
                <div id="error-box">⚠️ ALERTA: HASH NO RECONOCIDO</div>
            </div>
        </section>

        <section class="constitucion-section">
            <div class="constitucion-title">CONSTITUCIÓN AXIOMA® - Blindaje Técnico</div>
            <div class="grid-constitucion">
                <div class="item-c"><span class="item-num">1.</span> Auditoría 4.0</div>
                <div class="item-c"><span class="item-num">2.</span> Protocolo AXIOMA®</div>
                <div class="item-c"><span class="item-num">3.</span> Contabilidad Forense Digital</div>
                <div class="item-c"><span class="item-num">4.</span> Certificación de Activos 4.0</div>
                <div class="item-c"><span class="item-num">5.</span> Triple Verificación</div>
                <div class="item-c"><span class="item-num">6.</span> Prueba Petrificada</div>
                <div class="item-c"><span class="item-num">7.</span> Vertex (Nodo Innovación)</div>
                <div class="item-c"><span class="item-num">8.</span> Certificado de Existencia</div>
                <div class="item-c"><span class="item-num">9.</span> Custodia Geoespacial</div>
                <div class="item-c"><span class="item-num">10.</span> Sello de Inmutabilidad</div>
                <div class="item-c"><span class="item-num">11.</span> Transparencia Ejecutoria</div>
                <div class="item-c"><span class="item-num">12.</span> Soberanía de Datos</div>
                <div class="item-c"><span class="item-num">13.</span> Integridad de Datos</div>
                <div class="item-c"><span class="item-num">14.</span> Evidencia Forense 4.0</div>
                <div class="item-c"><span class="item-num">15.</span> Guía de Tránsito Digital</div>
                <div class="item-c"><span class="item-num">16.</span> Sello de Conformidad 4.0</div>
                <div class="item-c"><span class="item-num">17.</span> Gemelo Digital</div>
                <div class="item-c"><span class="item-num">18.</span> Hash de Origen (DNA)</div>
                <div class="item-c"><span class="item-num">19.</span> Smart-Settle</div>
            </div>
        </section>

        <div class="footer">NODO MORÓN | OPERATIVO | PROTOCOLO AXIOMA®</div>

        <script>
            const db = {"AX-2026-DRON01": "Dato Geoespacial Morón", "SHA-256-VADELL-01": "Auditoría Tributaria AFIP", "PROTOCOLO-AXIOMA-77": "Prueba Forense"};
            function procesar() {
                const val = document.getElementById('hash-input').value;
                document.getElementById('ui-box').style.display = 'none';
                if(db[val]) {
                    document.getElementById('res-hash').innerText = val;
                    document.getElementById('res-desc').innerText = db[val];
                    document.getElementById('certificado').style.display = 'block';
                } else {
                    document.getElementById('error-box').style.display = 'block';
                }
            }
        </script>
    </body>
    </html>
    """
