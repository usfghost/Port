<?php
    
    $db_serv 	= '04392E4.NETSOLHOST.COM';
    $db_user	= 'portadmin';
    $db_pass	= 'P!o2r#t4*';
    $db_name	= 'dbport';
    
    function OpenDBConnection() {		
    	$connDB =  new mysqli($db_serv, $db_user, $db_pass, $db_name);
    	if ($connDB->connect_error) {
    		die("<br>Connection failed: " . $connDB->connect_error);
    	} 
    	$connDB->set_charset("utf8");	
    	return $connDB;	
    }
    
    function CloseDBConnection($connDB) {
    	$connDB->close();
    }
?>