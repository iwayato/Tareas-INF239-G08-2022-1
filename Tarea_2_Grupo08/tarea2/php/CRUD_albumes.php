<?php
try {
    $host= 'localhost';
    $db = 'Tarea2_BD';
    $user = 'postgres';
    $password = 'iwayato';
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

        $sql = "SELECT * FROM album";

        try {
            $st = $db->query($sql, PDO::FETCH_ASSOC);
            echo json_encode($st->fetchAll());
        } catch (PDOException $exception) {
            http_response_code(500);
            die ("Can't execute query '$sql': '{$exception->getMessage()}'");
        }
        break;

    case 'post':

        $sql = "INSERT INTO album(nombre, imagen, fecha_lanzamiento) VALUES (:nombre, :imagen, :fecha_lanzamiento);";

        $st = $db->prepare($sql);

        try {
            $st->execute([
                'nombre' => $_POST['nombre'],
                'imagen' => $_POST['imagen'],
                'fecha_lanzamiento' => $_POST['fecha_lanzamiento'],
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

        $sql = "DELETE FROM album WHERE id = :id";

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

        if (empty($_POST['nombre']) || empty($_POST['imagen']) || empty($_POST['fecha_lanzamiento'])) {
            http_response_code(400);

            die;
        }

        $sql = 'UPDATE album SET nombre = :nombre, imagen = :imagen, fecha_lanzamiento = :fecha_lanzamiento WHERE id = :id';
        $st = $db->prepare($sql);

        try {
            $st->execute([
                'nombre' => $_POST['nombre'],
                'imagen' => $_POST['imagen'],
                'fecha_lanzamiento' => $_POST['fecha_lanzamiento'],
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