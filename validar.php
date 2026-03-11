<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Vertex Axioma - Validador</title>
</head>
<body style="background-color: #0d1117; color: #58a6ff; font-family: monospace; padding: 20px;">
    <h2>🛡️ Nodo Vertex Axioma - Ticket de Validación</h2>
    <div id="resultado">Procesando DNA Digital...</div>

    <script>
        async function generarHash(mensaje) {
            const msgBuffer = new TextEncoder().encode(mensaje + Date.now());
            const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
            const hashArray = Array.from(new Uint8Array(hashBuffer));
            return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
        }

        async function ejecutar() {
            const dna = await generarHash("Sello Inmutable Vertex");
            const ticket = {
                "status": "VALIDADO",
                "nodo": "Vertex Axioma - Nodo Morón",
                "dna_digital": dna,
                "timestamp": new Date().toLocaleString(),
                "protocolo": "AXIOMA 4.0",
                "sello": "Inmutabilidad Transfronteriza"
            };
            document.getElementById('resultado').innerHTML = '<pre style="color: #39ff14; background: #161b22; padding: 15px; border: 1px solid #30363d;">' + JSON.stringify(ticket, null, 4) + '</pre>';
        }
        ejecutar();
    </script>
</body>
</html>
