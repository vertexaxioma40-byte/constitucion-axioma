from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>Vertex Axioma - Auditoría 4.0</title>
            <style>
                body { margin: 0; padding: 0; overflow: hidden; }
                iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none; }
            </style>
        </head>
        <body>
            <iframe src="https://gamma.app/docs/VERTEX-AXIOMA-samkfi5i67siphz?embed=1"></iframe>
        </body>
    </html>
    """
