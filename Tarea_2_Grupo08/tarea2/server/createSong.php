<?php

    require("../php/db_config.php");

    $nombre = $_POST['nombre'];
    $letra = $_POST['letra'];
    $fecha_composicion = $_POST['fecha_composicion'];

    $sql = "INSERT INTO canciones(nombre, letra, fecha_composicion) VALUES ('$nombre', '$letra', '$fecha_composicion');";

    $result = pg_query($dbconn, $sql);
    
    if ($result) {
        echo("¡Guardado con éxito!");
        header("Location: ../html/CRUDcanciones.html");
    } else {
        echo("¡Error!");
    }
       
?>