<?php
// Motor Simple de Validación Vertex Axioma v1.0
header('Content-Type: application/json');

// 1. Recibimos la data del "tubo"
$input = file_get_contents('php://input');
$data = json_decode($input, true);

if ($data) {
    // 2. Generamos el DNA Digital (Hash)
    $dna_digital = hash('sha256', $input . time());
    
    // 3. Creamos el Ticket
    $ticket = [
        "status" => "VALIDADO",
        "nodo" => "Vertex Axioma - Nodo Morón",
        "dna_digital" => $dna_digital,
        "timestamp" => date("Y-m-d H:i:s"),
        "protocolo" => "AXIOMA 4.0",
        "mensaje" => "Prueba Petrificada en Capa de Recepción"
    ];

    // 4. Guardamos un registro (Tu Auditoría interna)
    file_put_contents("auditoria_log.txt", date("Y-m-d H:i:s") . " | HASH: " . $dna_digital . PHP_EOL, FILE_APPEND);

    echo json_encode($ticket, JSON_PRETTY_PRINT);
} else {
    echo json_encode(["error" => "No se recibieron datos para validar"]);
}
?>
