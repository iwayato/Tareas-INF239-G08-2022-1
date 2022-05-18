<?php

    require_once("db_config.php");

    $nombre = $_POST['nombre'];
    $apellido = $_POST['apellido'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    
    $sql = "INSERT INTO personas(nombre, apellido, email, 'password') VALUES ($1, $2, $3, $4);";

    
    $result = pg_query_params($conn_string, $sql, array($nombre, $apellido, $email, $password));
    
    echo("checkpoint");
?>