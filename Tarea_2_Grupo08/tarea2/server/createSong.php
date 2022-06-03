<?php

    require("../php/db_config.php");
    
    $nombre = filter_var($_POST['nombre'],FILTER_SANITIZE_FULL_SPECIAL_CHARS);
    $letra = filter_var($_POST['letra'],FILTER_SANITIZE_FULL_SPECIAL_CHARS);
    $fecha_composicion = $_POST['fecha_composicion'];
    
    $sql = "INSERT INTO canciones(nombre, letra, fecha_composicion) VALUES ('$nombre','$letra','$fecha_composicion');";
    $result = pg_query($dbconn, $sql);
    
    if ($result) {
        echo("¡Guardado con éxito!");
        header("Location: ../html/CRUDcanciones.html");
    } else {
        echo("¡Error!");
    }
       
?>