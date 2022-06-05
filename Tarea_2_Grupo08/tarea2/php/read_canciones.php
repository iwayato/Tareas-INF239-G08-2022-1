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

    $sql = 'SELECT * FROM canciones';

    try {
        $st = $db->query($sql, PDO::FETCH_ASSOC);
        echo json_encode($st->fetchAll());
    } catch (PDOException $exception) {
        http_response_code(500);
        die ("Can't execute query '$sql': '{$exception->getMessage()}'");
    }

?>