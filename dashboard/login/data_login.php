<?php
  session_start();
    if($_SERVER["REQUEST_METHOD"] == "POST")
    {
      $username = filter_input(INPUT_POST, 'username', FILTER_SANITIZE_SPECIAL_CHARS);
      $password = filter_input(INPUT_POST, 'password');

      $dataLogin = array('username' => $username, 'password' => $password);
    }
?>