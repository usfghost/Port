<?php

    $_username = $_POST['username'];
    $_password= $_POST['password'];

    if($_username == 'usf' && $_password == '123456') {
        echo 'yes it';
    } else {
        echo 'no it';
    }
?>