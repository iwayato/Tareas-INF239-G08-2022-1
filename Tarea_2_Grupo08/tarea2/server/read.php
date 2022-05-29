<?php
    require("../php/db_config.php");

    $email = $_POST['email'];
    $password = $_POST['password'];

    $sql = "SELECT nombre, apellido FROM personas WHERE email = '$email' AND password = '$password';";

    $result = pg_query($dbconn, $sql);

    if ($result) {
        echo("!Obtenido con Éxito!");
        header("Location: ../html/frontpage.html");
    } else {
        echo("¡Error!");
    }
?>