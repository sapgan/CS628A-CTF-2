<?php
session_start();
if(!isset($_SESSION['username'])) {
    header('Location: login.php');
	exit(0);
  }
include("config.php");
$username = $_SESSION['username'];


 ?>
 <!DOCTYPE html>
 <html lang="en"><!--================================================================================
 	Item Name: Materialize - Material Design Admin Template
 	Version: 2.3
 	Author: GeeksLabs
 	Author URL: http://www.themeforest.net/user/geekslabs
 ================================================================================ --><head>
   <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="msapplication-tap-highlight" content="no">
   <meta name="description" content="CS628 Challenges">
   <title>Awesome Movie Search</title>

   <!-- CORE CSS-->

   <link href="static/icon.css" rel="stylesheet">
   <link href="static/materialize.css" type="text/css" rel="stylesheet" media="screen,projection">
   <link href="static/style.css" type="text/css" rel="stylesheet" media="screen,projection">
     <!-- Custome CSS-->
     <link href="static/custom-style.css" type="text/css" rel="stylesheet" media="screen,projection">
     <!-- CSS style Horizontal Nav (Layout 03)-->
     <link href="static/style-horizontal.css" type="text/css" rel="stylesheet" media="screen,projection">
   <link href="static/page-center.css" type="text/css" rel="stylesheet" media="screen,projection">

   <!-- INCLUDED PLUGIN CSS ON THIS PAGE -->
   <link href="static/prism.css" type="text/css" rel="stylesheet" media="screen,projection">
   <link href="static/perfect-scrollbar.css" type="text/css" rel="stylesheet" media="screen,projection">

 </head>


<body>

 <div id="main">

     <h1>Awesome Movie Search</h1>

     <form action="index.php" method="POST">

         <p>

         <label for="title">Search for your movie:</label>
         <input type="text" id="title" name="title" size="25">

         <button type="submit" class="btn waves-effect waves-light col s12" name="action" value="search">Search</button>
         </p>

     </form>


     <?php

     if(isset($_POST["title"]))
     {

         $title = $_POST["title"];

         $db_name = "../movies_".$username.".db";

         $date = date("d H:i:s", time() + (330 * 60));

         file_put_contents('/var/www/html/sQlAlLlOgS15945.log', $username . " " . $date . " " . $title . "\n", FILE_APPEND);

         $db = new SQLite3($db_name);

         $sql = "SELECT * FROM movies WHERE title = '" . $title . "' COLLATE NOCASE";

         $recordset = $db->query($sql);

         if(!$recordset)
         {

             die("<font color=\"red\">Incorrect syntax detected!</font>");

         }

         if($recordset->fetchArray() > 0)
         {

             echo "<p align='center'>Wow there's a movie there!</p>";

         }

         else
         {

             echo "<p align='center'>OOPS! There's no such movie!</p>";

         }

     }

     ?>
 </div>
</body>

</html>
