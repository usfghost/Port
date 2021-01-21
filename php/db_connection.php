<?php
    
    $db_serv 	= "mysqlcluster23.registeredsite.com";
    $db_user	= "portadmin";
    $db_pass	= "PUoSrFt1A2d4m8i0N";
    $db_name	= "dbport";
    
    function OpenDBConnection() {		
    	$connDB =  new mysqli($db_serv, $db_user, $db_pass, $db_name);
    	if ($connDB->connect_error) {
    		die('Connection failed: ' . $connDB->connect_error);
    	} 
    	$connDB->set_charset("utf8");	
    	return $connDB;	
    }
    
    function CloseDBConnection($connDB) {
    	$connDB->close();
    }
?>