<?php
    require("db_config.php");

    session_start();

    $nombre_artistico = filter_var($_POST['nombre_artistico'], FILTER_SANITIZE_FULL_SPECIAL_CHARS);
    $verificado = $_POST['verificado'];
    $id = $_SESSION["id_persona"];

    if (empty($verificado)) {
        $sql = "UPDATE personas set nombre_artistico = '$nombre_artistico', verificado = false WHERE id = '$id';";
    } else {
        $sql = "UPDATE personas set nombre_artistico = '$nombre_artistico', verificado = true WHERE id = '$id';";
    }
    
    pg_query($dbconn, $sql);

    header("Location: ../html/perfilusuario.html");
?>