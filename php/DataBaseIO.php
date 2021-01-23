<?php
// DataBaseIO
class DataBaseIO {

    public static function OpenDBConnection() {

        $db_servername = "mysqlcluster23.registeredsite.com";				      
        $db_username = "portadmin";
        $db_password = "P!o2r3tA1d2m3i4n5";
        $db_name = "dbport";

        $connDB =  new mysqli($db_servername, $db_username, $db_password, $db_name);
        if ($connDB->connect_error) {
            die("<br>Connection failed: " . $connDB->connect_error);
        } 
        $connDB->set_charset("utf8");	
        return $connDB;	
    }

    public static function CloseDBConnection($connDB) {
        $connDB->close();
    }

    public static function ExecuteQuery($sql){
        $strResponse = "";
        $conn = DataBaseIO::OpenDBConnection();
        $result = $conn->query($sql);
        DataBaseIO::CloseDBConnection($conn);
        return $result;
    }
}
?>