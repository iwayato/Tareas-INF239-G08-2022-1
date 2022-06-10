<?php
    session_start();
    if (isset($_SESSION["id_persona"])) {

        $tipo_persona = $_SESSION['tipo_persona'];
        echo($tipo_persona);

        if($tipo_persona == "artista"){
            header("Location: landpage_artista.html");
        }
        else{
            header("Location: landpage.html");
        }  
    }
?>