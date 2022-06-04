<?php

    require("../php/db_config.php");

    $nombre = $_POST['nombre'];
    $apellido = $_POST['apellido'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    $password_hashed = password_hash($password,PASSWORD_BCRYPT);
    

    $sql = "INSERT INTO personas(nombre, apellido, email, password, nombre_artistico, verificado, suscripcion_activa) VALUES ('$nombre', '$apellido', '$email', '$password_hashed', null, null, false);";

    $result = pg_query($dbconn, $sql);
    
    if ($result) {
        echo("¡Guardado con éxito!");
        header("Location: ../index.html");
    } else {
        echo("¡Error!");
    }
       
?>