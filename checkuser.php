<?php 
$post_username = $_POST['Username'];
$post_password = $_POST['Password'];

include "language.php";
include "dbconnection.php";


$post_username = preg_replace('/[^a-zA-Z0-9_ -]/s','',$post_username);
$post_password = preg_replace('/[^a-zA-Z0-9_ -]/s','',$post_password);

$host  = $_SERVER['HTTP_HOST'];
$uri   = trim(dirname($_SERVER['PHP_SELF']), '/\\');

//module constants 
//$host  = $_SERVER['HTTP_HOST'];
//$uri = "j4ad.com/geopoint";
//$uri   = trim(dirname($_SERVER['PHP_SELF']), '/\\');


// Create connection
$conn = OpenDBConnection();
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
//$conn->query("set names 'utf8'");
$sqlWhere = "WHERE username='" . $post_username. "' AND password='" .$post_password."'";
$sql = "SELECT * FROM Users " . $sqlWhere;
$result = $conn->query($sql);

$userId = "-1";
if ($result->num_rows > 0) {	
    while($row = $result->fetch_assoc()) {
        $userId = $row["ID"];    
	}

	setcookie("cUsername", $post_username);
	setcookie("cPassword", $post_password);	
	setcookie("cUserId", $userId);
	
	if (isset ($_GET['dID']) && $_GET['dID'] != ""){
		$extra = "diary_edit.php?ID=" . $_GET['dID'];
	}
	else {		
		$extra = $urlMyTasks."?AssignedTo=".$userId."&MinStatusID=3";
	}
} else {
    $extra = 'login.php';
}
CloseDBConnection($conn);

echo "<br>" . $_COOKIE["cUserId"] . "<br>" .$_COOKIE["cUsername"] . "<br>" .$_COOKIE["cPassword"] . "<br>" . $extra;

header("Location: http://$host/$uri/$extra"); 
exit ; 

?>
