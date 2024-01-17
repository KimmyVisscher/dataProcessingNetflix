<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user = filter_input(INPUT_POST, 'user', FILTER_SANITIZE_SPECIAL_CHARS);
    $apiKey = filter_input(INPUT_POST, 'apiKey');

    $ch = curl_init();

    // Replace 'your_api_key' with the actual API key from the form
    curl_setopt($ch, CURLOPT_URL, 'http://localhost:8000/apikey/' . urlencode($apiKey));
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);

    if (curl_errno($ch)) {
        echo 'cURL fout: ' . curl_error($ch);
    }

    curl_close($ch);

    // Decode the JSON response
    $responseData = json_decode($response, true);

    // Check the status and handle accordingly
    if ($responseData['status'] == 'success') {
        // API key is valid, redirect to another page
        header("Location: ./index.php");
        exit();
    } else {
        // API key is invalid, handle accordingly (show an error message, redirect, etc.)
        echo 'Invalid API Key';
    }
}
?>
