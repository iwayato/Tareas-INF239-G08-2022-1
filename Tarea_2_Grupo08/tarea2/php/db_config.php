<?php
    /* Detalles de la conexión */
    $conn_string = "host=localhost port=5432 dbname=postgres user=postgres password=Usm5615004k";
    // Recuerde reemplazar "<contraseña>" por su contraseña y "<nombre_db>" por el nombre de su BD. No se incluyen los "<>".
    // Establecemos una conexión con el servidor postgresSQL
    $dbconn = pg_connect($conn_string);

    // Revisamos el estado de la conexión en caso de errores.
    if(!$dbconn) {
        echo("No se ha podido conectar con la base de datos");
    }
    else {
        echo("Conectado a la base de datos \n");
    }
    //Carlos estuvo aquí
    /* Para incluir la configuración de este archivo en otro archivo .php utilice 
    <?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php'; ?>
    */
?>