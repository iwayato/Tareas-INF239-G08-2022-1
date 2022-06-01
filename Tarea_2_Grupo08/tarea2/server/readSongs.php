<?php
    require("../php/db_config.php");

    $sql = "SELECT id, nombre, album FROM canciones;";

    $result = pg_query($dbconn, $sql);

    while ($row = pg_fetch_row($result)){
        echo("<tr>");
            for ($j = 0; $j < 3; $j++) { // we're expecting three attributes
                echo "<td>".$row[$j]."</td>"; // gives the current item of the current attribute
            }
        echo(
            "<td>
                <button 
                    type='button' 
                    class='btn btn-sm'
                    data-toggle='modal'
                    data-target='#ModificarCancion$row[0]'>
                    <svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='blue' class='bi bi-pencil' viewBox='0 0 16 16'>
                    <path d='M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168l10-10zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207 11.207 2.5zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293l6.5-6.5zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325z'></path>
                    </svg>
                </button>"
        );
        echo(
                "<a href='../server/deleteSong.php?id=$row[0]'>
                    <button type='button' class='btn btn-sm'>
                        <svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='red' class='bi bi-trash' viewBox='0 0 16 16'>
                        <path d='M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z'></path>
                        <path fill-rule='evenodd' d='M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z'></path>
                        </svg>
                    </button>
                </a>
            </td>"
        );
        
        echo("</tr>");

        echo("
            <div id='ModificarCancion$row[0]' class='modal fade' role='dialog'>
                <div class='modal-dialog'>
            
                <div class='modal-content'>
                    <div class='modal-header'>
                        <h4 class='modal-title'>Actualizar Canción</h4>
                    </div>
            
                    <div class='modal-body'>
                        <form action='../server/updateSong.php?id=$row[0]' method='post'>
                            <input
                                type='text'
                                id='nombre'
                                name='nombre' required
                                size='50'
                                placeholder='$row[1]'>
                        
                            <br>
                        
                            <input
                                type='text'
                                id='album'
                                name='album' required
                                size='50'
                                placeholder='$row[2]'>
                        
                            <br>
                        
                            <button type='submit'>
                                <strong>Actualizar Canción</strong>
                            </button>
            
                            <br>
                        </form>
                    </div>
            
                    <div class='modal-footer'>
                        <button type='button' class='btn btn-default' data-dismiss='modal'>Close</button>
                    </div>
                </div>
            
                </div>
            </div>
        ");
    }
?>