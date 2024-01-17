<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Henkflix dashboard</title>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Sharp:opsz,wght,FILL,GRAD@48,400,0,0" />
  <link rel="stylesheet" href="../style.css">
</head>
<body>
   <div class="container">
      <aside> 
         <div class="top">
           <div class="logo">
             <h2>Henk<span class="danger">Flix</span> </h2>
           </div>
           <div class="close" id="close_btn">
            <span class="material-symbols-sharp">
              close
              </span>
           </div>
         </div>
          <div class="sidebar">
            <a href="../index.php">
              <span class="material-symbols-sharp">grid_view </span>
              <h3>Dashboard</h3>
           </a>
           <a href="#" class="active">
              <span class="material-symbols-sharp">person_outline </span>
              <h3>Accounts</h3>
           </a>
           <a href="./movie_serie.php">
            <span class="material-symbols-sharp"> movie </span>
              <h3>Films & series</h3>
           </a>
           <a href="./finance.php">
            <span class="material-symbols-sharp"> payments </span>
              <h3>Financiën</h3>
           </a>
           <a href="./subscription.php">
              <span class="material-symbols-sharp">subscriptions </span>
              <h3>Abonnementen</h3>
           </a>
           <a href="../login/login.html">
              <span class="material-symbols-sharp">logout </span>
              <h3>uitloggen</h3>
           </a>
          </div>
      </aside>
      <main>
           <h1>{Naam} dashboard</h1>
      <div class="recent_order">
         <h2>Recente accounts</h2>
         <?php
        $endpoint = 'http://127.0.0.1:8000/accounts';

            $headers = [
                'X-API-KEY: kimvissss',
                'Accept: application/json'
            ];

            // Initialize cURL session
            $ch = curl_init($endpoint);

            // Set cURL options including headers
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

            // Execute cURL session and get the response
            $response = curl_exec($ch);

            // Check for cURL errors
            if (curl_errno($ch)) {
                echo 'Curl error: ' . curl_error($ch);
            } else {
                // Process the response
                $data = json_decode($response, true);
            }

            function getSubscriptionDisplayName($subscriptionId) {
                switch ($subscriptionId) {
                    case 1:
                        return 'SD';
                    case 2:
                        return 'HD';
                    case 3:
                        return 'UHD';
                    default:
                        return 'Unknown';
                }
            }

            if ($data) {
                $accountTemplate = '
                    <tbody>
                        <tr>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                        </tr>
                    </tbody>
                ';

                $htmlOutput = '
                    <table>
                        <thead>
                            <tr>
                                <th>Gebruikersnaam</th>
                                <th>Email-adres</th>
                                <th>Abonnement type</th>
                                <th>Betaalwijze</th>
                            </tr>
                        </thead>
                ';

                foreach ($data as $account) {
                  // Get the display name based on subscription_id
                  $subscriptionDisplayName = getSubscriptionDisplayName($account['subscription_id']);
          
                  // Add the row to the HTML output
                  $htmlOutput .= sprintf(
                      $accountTemplate,
                      $account['username'],
                      $account['email'],
                      $subscriptionDisplayName,
                      $account['payment_method']
                  );
                }

                $htmlOutput .= '
                    </table>
                ';

                echo $htmlOutput;
            } else {
                // Handle invalid JSON response
                echo 'Invalid JSON response.';
            }

            // Close cURL session
            curl_close($ch);

        ?>
        </div>
      </main>
    <div class="right">

<div class="top">
   <button id="menu_bar">
     <span class="material-symbols-sharp">menu</span>
   </button>

   <div class="theme-toggler">
     <span class="material-symbols-sharp active">light_mode</span>
     <span class="material-symbols-sharp">dark_mode</span>
   </div>
    <div class="profile">
       <div class="info">
           <p><b>Gerjan</b></p>
           <p>Admin</p>
           <small class="text-muted"></small>
       </div>
       <div class="profile-photo">
         <img src="../images/gerjan.jpg" alt=""/>
       </div>
    </div>
</div>
   <script src="../script.js"></script>
</body>
</html>