<?php

    require("../php/db_config.php");

    $nombre = $_POST['nombre'];
    $apellido = $_POST['apellido'];
    $email = $_POST['email'];
    $password = $_POST['password'];

    $sql = "INSERT INTO personas(nombre, apellido, email, password, nombre_artistico, verificado, suscripcion_activa) VALUES ('$nombre', '$apellido', '$email', '$password', null, null, false);";

    $result = pg_query($dbconn, $sql);
    
    if ($result) {
        echo("¡Guardado con éxito!");
    } else {
        echo("¡Error!");
    }
       
?>