<?php

    require("../php/db_config.php");

    $nombre = $_POST['nombre'];
    $album = $_POST['album'];
    
    $sql = "INSERT INTO canciones(nombre, album) VALUES ('$nombre', '$album');";

    $result = pg_query($dbconn, $sql);
    
    if ($result) {
        echo("¡Guardado con éxito!");
        header("Location: ../html/CRUDcanciones.html");
    } else {
        echo("¡Error!");
    }
       
?>