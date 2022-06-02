<?php
    require("../php/db_config.php");

    $id = $_GET["id"];
    $nuevoNombreCancion = $_POST["nombre"];
    $nuevaLetra = $_POST["letra"];
    //$function = $_GET["function"];

    // if ($function == "edit") {

    //     echo "<form action='updateSong.php?id=$id&function=edited' method='POST'>";
    //     echo "<table>";

    //     $result = pg_query($dbconn, "select id, nombre, album from canciones where ID = $id");

    //     while ($row = pg_fetch_row($result)) {
    //         echo "<tr>";
    //         echo "<td>ID</td>";
    //         echo "<td>".$row[0]."</td>"; // not changeable
    //         echo "</tr>";
    //         echo "<tr>";
    //         echo "<td>nombre</td>";
    //         echo "<td><input type='text' name='edited_comic_name' value='".$row[1]."'/></td>"; // changeable
    //         echo "</tr>";

    //         echo "<td>album</td>";
    //         echo "<td><input type='text' name='edited_comic_album' value='".$row[2]."'/></td>"; // changeable
    //         echo "</tr>";
    //     }

    //     echo "</table>";
    //     echo "<input name='id' value='$id' type='hidden'/>";
    //     echo "<input name='Save' value='Save' type='submit'/>";
    //     echo "</form>";
    // }


    //if ($function == "edited") {
        //$edited_comic_name = $_POST["edited_comic_name"];
        //$edited_comic_album = $_POST["edited_comic_album"];
        //$comic_id = $_POST["id"];
        $sql = "UPDATE canciones set nombre = '$nuevoNombreCancion', letra = '$nuevaLetra' WHERE id = $id;";

        pg_query($dbconn, $sql);
        header('Location: ../html/CRUDcanciones.html');
    //}

    //NO OLVIDAR COLOCAR &function=edited EN EL ARCHIVO readSongs.php si se descomenta lo anterior
?>