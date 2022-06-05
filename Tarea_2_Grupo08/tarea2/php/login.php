<?php
    require("db_config.php");

    $email = filter_var($_GET['email'], FILTER_SANITIZE_FULL_SPECIAL_CHARS);
    $password = filter_var($_GET['password'], FILTER_SANITIZE_FULL_SPECIAL_CHARS);

    $sql = "SELECT id, password FROM personas WHERE email = '$email';";

    $result = pg_query($dbconn, $sql);
    $row = pg_fetch_row($result);
    $password_hashed = $row[1];

    if (password_verify($password, $password_hashed)) {
        echo("!Obtenido con Éxito!");

        session_start();
        $_SESSION["id_persona"] = $row[0];
        
        header("Location: ../html/landpage.html");
    } else {
        echo("¡Error!");
    }
?>