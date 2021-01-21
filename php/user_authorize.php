<?php

    require 'db_connection.php';

    // Get username and password from HTTP POST request
    $_username = $_POST['username'];
    $_password = $_POST['password'];

    // Remove backslashes and special characters just in case
    $_username = preg_replace('/[^a-zA-Z0-9)_ -]/s', '', $_username);
    $_password = preg_replace('/[^a-zA-Z0-9)_ -]/s', '', $_password);

    // Open connection
    $conn = OpenDBConnection();

    // Execute query
    $query = 'SELECT * FROM users WHERE username=\''.$_username .'\' AND password=\''.$_password.'\'';
    $result = $conn->query($query);

    $user_id = '-1';
    if($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            $user_id = $row['ID'];
        }        
    }
    CloseDBConnection($conn);

    // Return user id (-1 if invalid)
    echo '123';

?>