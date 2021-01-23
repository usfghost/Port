<?
    require_once "DataBaseIO.php";

    $_username = $_POST['username'];
    $_password = $_POST['password'];

    $sql = "SELECT * FROM users WHERE username='" . $_username . "' AND password='" . $_password . "'";
    $result = DataBaseIO::ExecuteQuery($sql);
    $userid = '-1';
    if($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            $userid = $row['id'];
        }
    }

    echo $userid;
?>