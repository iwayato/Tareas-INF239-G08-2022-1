<?php
    $function = $_GET["function"];
    $comic_id = $_GET["id"];
    if ($function == "delete") {
        $sql = "delete from COMIC where ID = $comic_id";
        mysql_query($sql);
        header('Location: index.php?section=comic');
    }
?>