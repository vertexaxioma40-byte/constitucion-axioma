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
            body { background-color: #0d1117; color: #58a6ff; font-family: 'Segoe UI', Tahoma, sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; margin: 0; }
            .bunker { border: 1px solid #30363d; padding: 40px; border-radius: 15px; background: #161b22; text-align: center; box-shadow: 0 20px 50px rgba(0,0,0,0.7); max-width: 600px; width: 90%; margin: 20px; }
            img.logo { width: 280px; margin-bottom: 10px; border-radius: 8px; box-shadow: 0 0 15px rgba(88, 166, 255, 0.2); }
            .subtitle { color: #8b949e; margin-bottom: 30px; font-size: 13px; text-transform: uppercase; letter-spacing: 2px; border-bottom: 1px solid #30363d; padding-bottom: 10px; }
            .search-box { display: flex; flex-direction: column; gap: 15px; }
            input { padding: 15px; border-radius: 8px; border: 1px solid #30363d; background: #0d1117; color: #ffffff; text-align: center; font-family: 'Courier New', monospace; font-size: 14px; }
            button { padding: 15px; background: #238636; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 16px; transition: 0.3s; }
            button:hover { background: #2ea043; transform: scale(1.02); }
            
            /* Estilo del Certificado */
            #certificado { display: none; margin-top: 30px; padding: 25px; border: 2px double #3fb950; border-radius: 10px; background: #0d1117; text-align: left; position: relative; }
            .seal { color: #3fb950; font-weight: bold; font-size: 18px; margin-bottom: 15px; border-bottom: 1px solid #3fb950; padding-bottom: 5px; }
            .data-row { margin-bottom: 10px; font-size: 13px; color: #c9d1d9; }
            .data-label { color: #8b949e; font-weight: bold; }
            .btn-print { margin-top: 20px; background: #1f6feb; width: 100%; }
            
            .footer { margin-top: 30px; font-size: 10px; color: #484f58; text-transform: uppercase; }
        </style>
    </head>
    <body>
        <div class="bunker">
