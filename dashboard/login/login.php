<!DOCTYPE html>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user = filter_input(INPUT_POST, 'user', FILTER_SANITIZE_SPECIAL_CHARS);
    $apiKey = filter_input(INPUT_POST, 'apiKey');

    $ch = curl_init();

    curl_setopt($ch, CURLOPT_URL, 'http://127.0.0.1:8000/apikey/' . $apiKey);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);

    if (curl_errno($ch)) {
        echo 'cURL fout: ' . curl_error($ch);
    }

    curl_close($ch);

    $responseData = json_decode($response, true);

     echo var_dump($responseData);

    if ($responseData['apikey'] == $apiKey) {
        header("Location: ./index.php");
        exit();
    } else {
        echo 'Invalid API Key';
    }
}
?>

<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script
      src="https://kit.fontawesome.com/64d58efce2.js"
      crossorigin="anonymous"
    ></script>
    <link rel="stylesheet" href="style.css" />
    <title>Login</title>
  </head>
  <body>
    <div class="container">
      <div class="forms-container">
        <div class="signin-signup">
          <form action="<?=$_SERVER['PHP_SELF']?>" class="sign-in-form" method="post">
            <h2 class="title">Login HenkFlix</h2>
            <div class="input-field">
              <i class="fas fa-user"></i>
              <input type="text" name="user" placeholder="Junior/medior/senior" />
            </div>
            <div class="input-field">
              <i class="fas fa-key"></i>
              <input type="password" name="apiKey" placeholder="apiKey" />
            </div>
            <input type="submit" value="Login" class="btn solid" />
          </form>
        </div>
      </div>

      <div class="panels-container">
        <div class="panel left-panel">
          <div class="content">
            <h3>Welkom bij HenkFlix!</h3>
            <p>
              Lorem ipsum, dolor sit amet consectetur adipisicing elit. Debitis,
              ex ratione. Aliquid!
            </p>
          </div>
          <img src="img/log.svg" class="image" alt="" />
        </div>
        <div class="panel right-panel">
          <div class="content">
            <h3>Werkt u bij HenkFlix?</h3>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum
              laboriosam ad deleniti.
            </p>
            <button class="btn transparent" id="sign-in-btn">
              inloggen
            </button>
          </div>
        </div>
      </div>
    </div>

    <script src="app.js"></script>
  </body>
</html>