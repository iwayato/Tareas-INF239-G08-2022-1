<?php
    require("../php/db_config.php");

    $sql = "SELECT id, nombre, album FROM canciones;";

    $result = pg_query($dbconn, $sql);

    while ($row = pg_fetch_row($result)){
        echo("<tr>");
            for ($j = 0; $j < 3; $j++) { // we're expecting three attributes
                echo "<td>".$row[$j]."</td>"; // gives the current item of the current attribute
            }
        echo "  <td><a href="index.php?section=comic&function=edit&id=$row[0]">Edit</a></td>";
        echo "  <td><a href="index.php?section=comic&function=delete&id=$row[0]">Delete</a></td>";
        include("../html/ButtonsUpdateDelete.html");
        echo("</tr>");
    }
?>