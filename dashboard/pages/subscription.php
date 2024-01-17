<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Henkflix dashboard</title>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Sharp:opsz,wght,FILL,GRAD@48,400,0,0" />
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
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
           <a href="account.php">
              <span class="material-symbols-sharp">person_outline </span>
              <h3>Accounts</h3>
           </a>
           <a href="movie_serie.php">
            <span class="material-symbols-sharp"> movie </span>
              <h3>Films & series</h3>
           </a>
           <a href="finance.php">
            <span class="material-symbols-sharp"> payments </span>
              <h3>Financiën</h3>
           </a>
           <a href="#" class="active">
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
        <div class="insights">
            <div class="sales">
               <span class="material-symbols-sharp">subscriptions</span>
               <div class="middle">
                 <div class="left">
                   <h3>Basis abonnement</h3>
                   <h1>750x</h1>
                 </div>
               </div>
               <small>SD</small>
               <small>€7.99</small>
            </div>
              <div class="expenses">
                <span class="material-symbols-sharp">subscriptions</span>
                <div class="middle">
                  <div class="left">
                    <h3>Standaard abonnement</h3>
                    <h1>300x</h1>
                  </div>
                </div>
                <small>HD</small>
                <small>€10.99</small>
             </div>
               <div class="income">
                <span class="material-symbols-sharp">subscriptions</span>
                <div class="middle">
                  <div class="left">
                    <h3>Premium abonnement</h3>
                    <h1>500x</h1>
                  </div>
                </div>
                <small>UHD</small>
                <small>€13.99</small>
             </div>
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

  
   <script src="script.js"></script>
</body>
</html>