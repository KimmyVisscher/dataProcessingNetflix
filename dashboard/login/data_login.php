<?php
  $ch = curl_init();

    if($_SERVER["REQUEST_METHOD"] == "POST")
    {
      $username = filter_input(INPUT_POST, 'username', FILTER_SANITIZE_SPECIAL_CHARS);
      $password = filter_input(INPUT_POST, 'password');

      $dataLogin = array('username' => $username, 'password' => $password);

      curl_setopt($ch, CURLOPT_URL, 'http://localhost:8000/#/components/schemas/Account');
      curl_setopt($ch, CURLOPT_POST, 1);
      curl_setopt($ch, CURLOPT_POSTFIELDS, $dataLogin);
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

      $response = curl_exec($ch);

      if (curl_errno($ch)) {
        echo 'cURL fout: ' . curl_error($ch);
      }

      curl_close($ch);

    }
?>