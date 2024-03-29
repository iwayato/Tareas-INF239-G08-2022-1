<?php
    require("db_config.php");

    $email = filter_var($_GET['email'], FILTER_SANITIZE_FULL_SPECIAL_CHARS);
    $password = filter_var($_GET['password'], FILTER_SANITIZE_FULL_SPECIAL_CHARS);

    $sql = "SELECT id, password, nombre_artistico FROM personas WHERE email = '$email';";

    $result = pg_query($dbconn, $sql);
    $row = pg_fetch_row($result);
    $password_hashed = $row[1];

    if (password_verify($password, $password_hashed)) {

        echo("!Obtenido con Éxito!");            
        session_start();
        $_SESSION["id_persona"] = $row[0];

        if (isset($row[2])) {
            $_SESSION["tipo_persona"] = "artista";
            header("Location: ../html/landpage_artista.html");

        } else {
            $_SESSION["tipo_persona"] = "usuario";
            header("Location: ../html/landpage.html");
        }

    } else {
        header("Location: ../html/login.html?error=1");
    }
?>