<?php
  require 'vendor/autoload.php';
  
  use GuzzleHttp\Client;
  
  $client = new Client();
  
  $response = $client->request('POST', 'http://localhost:8000/accounts', [
      'form_params' => [
          'username' => $_POST['username'],
          'email' => $_POST['email'],
          'password' => $_POST['password'],
      ]
  ]);
  
  $status_code = $response->getStatusCode();
  
  if ($status_code == 201) {
      header('Location: welcome.php');
  } else {
      echo "Registration failed. Please try again.";
  }
?>