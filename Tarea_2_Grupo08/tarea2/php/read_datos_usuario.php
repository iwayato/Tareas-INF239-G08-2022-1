<?php
    try {
        $host= 'localhost';
        $db = 'postgres';
        $user = 'postgres';
        $password = 'Usm5615004k';
        $dsn = "pgsql:host=$host;port=5432;dbname=$db;";
        $db = new PDO($dsn, $user, $password, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
    } catch (PDOException $exception) {
        die("Can't connect to the database: {$exception->getMessage()}");
    }
    session_start();
    $id = $_SESSION["id_persona"];

    $sql = "SELECT * FROM personas WHERE id = '$id'";

    try {
        $st = $db->query($sql, PDO::FETCH_ASSOC);
        echo json_encode($st->fetchAll());
    } catch (PDOException $exception) {
        http_response_code(500);
        die ("Can't execute query '$sql': '{$exception->getMessage()}'");
    }
?>