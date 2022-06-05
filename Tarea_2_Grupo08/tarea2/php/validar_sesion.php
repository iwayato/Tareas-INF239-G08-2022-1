<?php
    session_start();

    if (!isset($_SESSION["id_persona"])) {

        header("Location: ../html/login.html");
        exit("Página Privada");
        
    }
?>
