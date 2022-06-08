<?php
    session_start();

    $tipo_persona = $_SESSION['tipo_persona'];

    if($tipo_persona == "usuario"){

    }
    else{
        exit("No tiene acceso a esta pagina");
    }
             
?>