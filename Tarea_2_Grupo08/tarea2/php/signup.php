<?php

    require("db_config.php");

    $nombre = filter_var($_POST['nombre'], FILTER_SANITIZE_FULL_SPECIAL_CHARS);
    $apellido = filter_var($_POST['apellido'], FILTER_SANITIZE_FULL_SPECIAL_CHARS);
    $email = filter_var($_POST['email'], FILTER_SANITIZE_FULL_SPECIAL_CHARS);
    $password = filter_var($_POST['password'], FILTER_SANITIZE_FULL_SPECIAL_CHARS);
    $password_hashed = password_hash($password, PASSWORD_BCRYPT);

    $sql = "SELECT * FROM personas WHERE email = '$email';";
    $result = pg_query($dbconn, $sql);
    $row = pg_fetch_row($result);

    if(isset($row[0])){
        exit("Este email ya esta ocupado"); 
    }
    else{
        $sql = "INSERT INTO personas(nombre, apellido, email, password, nombre_artistico, verificado, suscripcion_activa) VALUES ('$nombre', '$apellido', '$email', '$password_hashed', null, null, false);";
        $result = pg_query($dbconn, $sql);
    
        if ($result) {
            echo("¡Guardado con éxito!");
            header("Location: ../html/login.html");
        } else {
            echo("¡Error!");
        }
    }
       
?>