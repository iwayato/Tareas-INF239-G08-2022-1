<?php
try {
    $host= 'localhost';
    $db = 'postgres';
    $user = 'postgres';
    $password = 'Usm5615004k';
    $dsn = "pgsql:host=$host;port=5432;dbname=$db;";
    $db = new PDO($dsn, $user, $password, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
    session_start();
    $id_persona = $_SESSION["id_persona"];
} catch (PDOException $exception) {
    die("Can't connect to the database: {$exception->getMessage()}");
}

switch (strtolower($_SERVER['REQUEST_METHOD'])) 
{
    case 'get':

        $sql = "
            SELECT 
                id, nombre, letra, fecha_composicion
            FROM 
                canciones
            INNER JOIN
                artista_compuso_cancion
            ON
                canciones.id = artista_compuso_cancion.id_cancion
            WHERE
                artista_compuso_cancion.id_artista = $id_persona
        ;";

        try {
            $st = $db->query($sql, PDO::FETCH_ASSOC);
            echo json_encode($st->fetchAll());
        } catch (PDOException $exception) {
            http_response_code(500);
            die ("Can't execute query '$sql': '{$exception->getMessage()}'");
        }
        break;

    case 'post':


        $sql = "
        WITH nueva_cancion as (
            INSERT INTO canciones(nombre, letra, fecha_composicion) VALUES (:nombre, :letra, :fecha_composicion)
            RETURNING id
        )
        INSERT INTO artista_compuso_cancion(id_artista, id_cancion) VALUES ($id_persona, (SELECT id FROM nueva_cancion));
        ";

        $sql2 = "WITH id_cancion as (
                SELECT id FROM canciones WHERE nombre = :nombre AND letra = :letra AND fecha_composicion = :fecha_composicion
                )
				INSERT INTO album_tiene_cancion(id_album, id_cancion) VALUES (:id_album, (SELECT id from id_cancion))";

        
        $st = $db->prepare($sql);

        try {
            $st->execute([
                'nombre' => $_POST['nombre'],
                'letra' => $_POST['letra'],
                'fecha_composicion' => $_POST['fecha_composicion'],
            ]);



            echo $db->lastInsertId();
        } catch (PDOException $exception) {
            http_response_code(500);
            die ($exception->getMessage());
        }

        $st = $db->prepare($sql2);

        try {
            $st->execute([
                'nombre' => $_POST['nombre'],
                'letra' => $_POST['letra'],
                'id_album' => $_POST['id_album'],
                'fecha_composicion' => $_POST['fecha_composicion'],
            ]);



            echo $db->lastInsertId();
        } catch (PDOException $exception) {
            http_response_code(500);
            die ($exception->getMessage());
        }

        break;

        

    case 'delete':
        if (empty($id = filter_input(INPUT_GET, 'id'))) {
            http_response_code(400);
            die;
        }

        $sql = "DELETE FROM canciones WHERE id = :id";

        $st = $db->prepare($sql);
        
        try {
            $st->execute([
                'id' => $id,
            ]);
        } catch (Exception $exception) {
            http_response_code(500);
            die($exception->getMessage());
        }
        break;

    case 'put':
        if (empty($id = filter_input(INPUT_GET, 'id'))) {
            http_response_code(400);
    
            die;
        }

        parse_str(file_get_contents('php://input'), $_POST);

        if (empty($_POST['nombre']) || empty($_POST['letra']) || empty($_POST['fecha_composicion'])) {
            http_response_code(400);

            die;
        }

        $sql = 'UPDATE canciones SET nombre = :nombre, letra = :letra, fecha_composicion = :fecha_composicion WHERE id = :id';
        $st = $db->prepare($sql);

        try {
            $st->execute([
                'nombre' => $_POST['nombre'],
                'letra' => $_POST['letra'],
                'fecha_composicion' => $_POST['fecha_composicion'],
                'id' => $id,
            ]);
            http_response_code(200);
        } catch (PDOException $exception) {
            http_response_code(500);

            die ($exception->getMessage());
        }

        break;
}
?>        