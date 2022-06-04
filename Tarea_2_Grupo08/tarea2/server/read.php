<?php
    require("../php/db_config.php");

    $email = $_POST['email'];
    $password = $_POST['password'];

    $sql = "SELECT id,password FROM personas WHERE email = '$email';";

    $result = pg_query($dbconn, $sql);
    $row = pg_fetch_row($result);
    $password_hashed = $row[1];

    if (password_verify($password,$password_hashed)) {
        echo("!Obtenido con Éxito!");

        session_start();
        $_SESSION["id_artista"] = $row[0];
        
        header("Location: ../html/frontpage.html");
    } else {
        echo("¡Error!");
    }
?>