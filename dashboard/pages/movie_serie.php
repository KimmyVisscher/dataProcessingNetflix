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
           <a href="./account.php">
              <span class="material-symbols-sharp">person_outline </span>
              <h3>Accounts</h3>
           </a>
           <a href="./movie_serie.php" class="active">
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
         <h2>Films</h2>
         <?php
            $endpoint = 'http://127.0.0.1:8000/movies'; 

            $headers = [
                'X-API-KEY: kimvissss',
                'Accept: application/json'
            ];

            $ch = curl_init($endpoint);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
            $response = curl_exec($ch);

            if (curl_errno($ch)) {
                echo 'Curl error: ' . curl_error($ch);
            } else {
                $data = json_decode($response, true);
            }

            function getAgeRestriction($ageRestriction) {
                switch ($ageRestriction) {
                    case "ALL_AGES":
                        return 'Alle leeftijden';
                    case "SIX_YEARS":
                        return '6+';
                    case "TWELVE_YEARS":
                        return '12+';
                    case "SIXTEEN_YEARS":
                        return '16+';
                    default:
                        return 'Unknown';
                }
            }

            if ($data) {
                $htmlOutput = '
                    <table>
                        <thead>
                            <tr>
                                <th>Film id</th>
                                <th>Naam</th>
                                <th>film duur</th>
                                <th>Leeftijd</th>
                                <th>IMDB</th>
                            </tr>
                        </thead>
                        <tbody>
                ';

                foreach ($data as $movie) {
                    $movieId = $movie['movie_id'];
                    $imdbEndpoint = "http://127.0.0.1:8000/movies/{$movieId}/imdb";

                    $imdbCh = curl_init($imdbEndpoint);
                    curl_setopt($imdbCh, CURLOPT_RETURNTRANSFER, true);
                    curl_setopt($imdbCh, CURLOPT_HTTPHEADER, $headers);
                    $imdbResponse = curl_exec($imdbCh);

                    if (curl_errno($imdbCh)) {
                        echo 'Curl error for IMDb: ' . curl_error($imdbCh);
                    } else {
                        $imdbData = json_decode($imdbResponse, true);
                        $ageRestriction = getAgeRestriction($movie['age_restriction']);

                        $htmlOutput .= sprintf(
                            '<tr>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s minuten</td>
                                <td>%s</td>
                                <td>%s</td>
                            </tr>',
                            $movieId,
                            $movie['title'],
                            $movie['movie_duration'],
                            $ageRestriction,
                            isset($imdbData['imdbRating']) ? $imdbData['imdbRating'] : 'N/A'
                        );
                    }

                    curl_close($imdbCh);
                }

                $htmlOutput .= '
                        </tbody>
                    </table>
                ';

                echo $htmlOutput;
            } else {
                echo 'Invalid JSON response.';
            }

            curl_close($ch);
?>
        <div class="recent_order">
          <h2>Series</h2>
          <?php
            $endpoint = 'http://127.0.0.1:8000/series'; 

            $headers = [
                'X-API-KEY: kimvissss',
                'Accept: application/json'
            ];

            $ch = curl_init($endpoint);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
            $response = curl_exec($ch);

            if (curl_errno($ch)) {
                echo 'Curl error: ' . curl_error($ch);
            } else {
                $data = json_decode($response, true);
            }

            function getAgeRestrictionSerie($ageRestrictionSerie) {
                switch ($ageRestrictionSerie) {
                    case "ALL_AGES":
                        return 'Alle leeftijden';
                    case "SIX_YEARS":
                        return '6+';
                    case "TWELVE_YEARS":
                        return '12+';
                    case "SIXTEEN_YEARS":
                        return '16+';
                    default:
                        return 'Unknown';
                }
            }

            if ($data) {
                $htmlOutput = '
                    <table>
                        <thead>
                            <tr>
                                <th>Serie id</th>
                                <th>Naam</th>
                                <th>Leeftijd</th>
                                <th>IMDB</th>
                            </tr>
                        </thead>
                        <tbody>
                ';

                foreach ($data as $serie) {
                    $serieId = $serie['serie_id'];
                    $imdbEndpoint = "http://127.0.0.1:8000/series/{$serieId}/imdb";

                    $imdbCh = curl_init($imdbEndpoint);
                    curl_setopt($imdbCh, CURLOPT_RETURNTRANSFER, true);
                    curl_setopt($imdbCh, CURLOPT_HTTPHEADER, $headers);
                    $imdbResponse = curl_exec($imdbCh);

                    if (curl_errno($imdbCh)) {
                        echo 'Curl error for IMDb: ' . curl_error($imdbCh);
                    } else {
                        $imdbData = json_decode($imdbResponse, true);
                        $ageRestrictionSerie = getAgeRestrictionSerie($serie['age_restriction']);

                        $htmlOutput .= sprintf(
                            '<tr>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s</td>
                            </tr>',
                            $serieId,
                            $serie['serie_name'],
                            $ageRestrictionSerie,
                            isset($imdbData['imdbRating']) ? $imdbData['imdbRating'] : 'N/A'
                        );
                    }

                    curl_close($imdbCh);
                }

                $htmlOutput .= '
                        </tbody>
                    </table>
                ';

                echo $htmlOutput;
            } else {
                echo 'Invalid JSON response.';
            }

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
<?php
  $searchValue = isset($_GET['search']) ? $_GET['search'] : '';

  $endpoint = 'http://127.0.0.1:8000/movies/1/subtitles';

  if (!empty($searchValue)) {
    // Ensure the search value is a valid integer to prevent security issues
    if (ctype_digit($searchValue)) {
        $endpoint = 'http://127.0.0.1:8000/movies/' . $searchValue . '/subtitles';
    } else {
        // Handle the case where the search value is not a valid integer
        echo 'Invalid search value.';
        exit;
    }
}



  $headers = [
      'X-API-KEY: kimvissss',
      'Accept: application/json'
  ];

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
  function getName($name) {
    switch ($name) {
        case 1:
            return 'The Shawshank Redemption';
        case 2:
            return 'The Godfather';
        default:
            return 'Unknown';
    }
}

      if ($data) {
          // HTML template for a single movie
          $subtitleTemplate = '
              <div class="update">
                  <div class="message">
                  <span class="material-symbols-sharp">subtitles</span>
                      <p><strong> %s</strong></p>
                      <p>Taal: %s</p>
                      <p>Locatie: %s</p><br>
                  </div>
              </div>
          ';

          // HTML container for all movies
          $htmlOutput = '
              <div class="recent_updates">
                  <h2>Ondertitelingen</h2>
                  <form method="get" action="">
                    <input type="number" id="search" name="search" placeholder="Enter movie ID">
                    <button type="submit">Zoeken</button>
                </form>
                  <div class="updates">
          ';

          // Loop through the first 5 movies in the $data array
          foreach ($data as $subtitle) {
            $name = getName($subtitle['movie_id']);
              $htmlOutput .= sprintf(
                  $subtitleTemplate,
                  $name,
                  strtolower($subtitle['language']),
                  $subtitle['subtitle_location']
              );
          }

          // Close the HTML container
          $htmlOutput .= '
                  </div>
              </div>
          ';

          // Output the final HTML
          echo $htmlOutput;
      } else {
          // Handle invalid JSON response
          echo 'Invalid JSON response.';
      }

      // Close cURL session
      curl_close($ch);
?>
<?php
  $searchValue = isset($_GET['searchSerie']) ? $_GET['searchSerie'] : '';

  $endpoint = 'http://127.0.0.1:8000/series/1/episodes';

  if (!empty($searchValue)) {
    // Ensure the search value is a valid integer to prevent security issues
    if (ctype_digit($searchValue)) {
        $endpoint = 'http://127.0.0.1:8000/series/' . $searchValue . '/episodes';
    } else {
        // Handle the case where the search value is not a valid integer
        echo 'Invalid search value.';
        exit;
    }
}



  $headers = [
      'X-API-KEY: kimvissss',
      'Accept: application/json'
  ];

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
  function getSerieName($serieName) {
    switch ($serieName) {
        case 1:
            return 'Stranger things';
        case 2:
            return 'The crown';
        case 3:
            return "Breaking bad";
        default:
            return 'Unknown';
    }
}

      if ($data) {
          // HTML template for a single movie
          $episodeTemplate = '
              <div class="update">
                  <div class="message">
                  <span class="material-symbols-sharp">movie</span>
                      <p><strong> %s</strong></p>
                      <p>Titel: %s</p>
                      <p>Serie duur: %s minuten</p><br>
                  </div>
              </div>
          ';

          // HTML container for all movies
          $htmlOutput = '
              <div class="recent_updates">
                  <h2>Afleveringen</h2>
                  <form method="get" action="">
                    <input type="number" id="searchSerie" name="searchSerie" placeholder="Enter serie ID">
                    <button type="submit">Zoeken</button>
                </form>
                  <div class="updates">
          ';

          // Loop through the first 5 movies in the $data array
          foreach ($data as $episode) {
            $serieName = getSerieName($episode['serie_id']);
              $htmlOutput .= sprintf(
                  $episodeTemplate,
                  $serieName,
                  $episode['title'],
                  $episode['episode_duration']
              );
          }

          // Close the HTML container
          $htmlOutput .= '
                  </div>
              </div>
          ';

          // Output the final HTML
          echo $htmlOutput;
      } else {
          // Handle invalid JSON response
          echo 'Invalid JSON response.';
      }

      // Close cURL session
      curl_close($ch);
?>
   <script src="../script.js"></script>
</body>
</html>