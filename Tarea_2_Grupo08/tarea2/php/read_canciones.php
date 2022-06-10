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
        canciones.nombre AS nombre, canciones.fecha_composicion, canciones.letra, compositores.nombre AS compositores, album.nombre as nombre_album
    FROM 
        canciones
    INNER JOIN(
        SELECT 
            personas.nombre_artistico as nombre, artista_compuso_cancion.id_cancion
        FROM 
            personas
        INNER JOIN
            artista_compuso_cancion
        ON
            personas.id = artista_compuso_cancion.id_artista
        ) as compositores
    ON
        canciones.id = compositores.id_cancion
    INNER JOIN
        album_tiene_cancion
    ON
        canciones.id = album_tiene_cancion.id_cancion
    INNER JOIN
        album
    ON
        album_tiene_cancion.id_album = album.id
;";

try {
    $st = $db->query($sql, PDO::FETCH_ASSOC);
    echo json_encode($st->fetchAll());
} catch (PDOException $exception) {
    http_response_code(500);
    die ("Can't execute query '$sql': '{$exception->getMessage()}'");
}
?>
