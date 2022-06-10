<?php
    session_start();

    $tipo_persona = $_SESSION['tipo_persona'];

    if($tipo_persona == "artista"){

    }
    else{
        exit("No tiene acceso a esta página");
    }
             
?>