<?php
function OpenDBConnection()
{
	$db_servername = "mysqlcluster6.registeredsite.com";				      
	$db_username = "yousefk";
	$db_password = "Y1o2u3s4e5f6";
	$db_name = "geopointofficedb";

	// Create connection
	$conn = new mysqli($db_servername, $db_username, $db_password, $db_name);
	// Check connection
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	} 
	//$conn->query("set names 'utf8'");
	$conn->set_charset("utf8");	
	return $conn;
}

function CloseDBConnection($conn)
{
	$conn->close();
}
?>
