<?php
try {
    $host= 'localhost';
    $db = 'Tarea2_BD';
    $user = 'postgres';
    $password = 'iwayato';
    $dsn = "pgsql:host=$host;port=5432;dbname=$db;";
    $db = new PDO($dsn, $user, $password, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
} catch (PDOException $exception) {
    die("Can't connect to the database: {$exception->getMessage()}");
}

$sql = "
    SELECT 
        canciones.nombre AS nombre, compositores.nombre AS compositores
    FROM 
        canciones
    INNER JOIN(
        SELECT 
            personas.nombre as nombre, artista_compuso_cancion.id_cancion
        FROM 
            personas
        INNER JOIN
            artista_compuso_cancion
        ON
            personas.id = artista_compuso_cancion.id_artista) as compositores
    ON
        canciones.id = compositores.id_cancion
;";

try {
    $st = $db->query($sql, PDO::FETCH_ASSOC);
    echo json_encode($st->fetchAll());
} catch (PDOException $exception) {
    http_response_code(500);
    die ("Can't execute query '$sql': '{$exception->getMessage()}'");
}
?>
