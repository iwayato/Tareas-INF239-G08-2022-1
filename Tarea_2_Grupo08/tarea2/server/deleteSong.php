<?php
    require("../php/db_config.php");

    echo("<h1>Hello</h1>");
    $id = $_GET["id"];
    echo($id);

    $sql = "delete from canciones where ID = $id";
    pg_query($dbconn, $sql);
    header('Location: ../html/CRUDcanciones.html');
?>