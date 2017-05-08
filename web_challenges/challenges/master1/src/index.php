<?php
session_start();
if(!isset($_SESSION['username'])) {
    header('Location: login.php');
	exit(0);
  }
include("config.php");
$username = $_SESSION['username'];
$team = $_SESSION['teamname'];


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

     <h1>CTF Review</h1>
     <?php
     if($username == "admin"){
     echo "<form action='index.php' method='POST'>\n<p><label for='review'>Your Feedback:</label><input type='text' id='review' name='review' size='25'><label for='team'>Team Name:</label><input type='text' id='team' name='team' size='25'><button type='submit' class='btn waves-effect waves-light col s12' name='action' value='submit'>Submit</button></p></form><!-- Just remember the golden rules! -->";
   }
   else{
     echo "<p>Currently only admin can give feedback.Sorry for the inconvenience.You are ". $username ." </p>";
   }
   ?>


     <?php

     if(isset($_POST["review"]))
     {
      $con = mysqli_connect($db_host, $db_user, $db_pass, $db_name);
       $comments=mysqli_real_escape_string($con,$_POST['review']);
       $team_submitted = mysqli_real_escape_string($con,$_POST['team']);
       $url=mysqli_real_escape_string($con,$_SERVER['X_HTTP_FORWARDED_FOR']);
       if($team_submitted !== $team){
         echo "Don't try to submit review as others!";
         die;
       }
       $team_submitted = $team_submitted. "-". $_SERVER['REMOTE_ADDR'];

      $date = date("d H:i:s", time() + (330 * 60));
       $team_submitted = $team_submitted. "-". $_SERVER['REMOTE_ADDR']. "-".$date;

      file_put_contents('/var/www/html/sQlAlLlOgS15945.log', $team . " " . $date . " " . $url . "\n", FILE_APPEND);
       $query = "Insert into reviews values('".$comments."','".urldecode($url)."','".$team_submitted."')";
       $patterns = array('sleep','benchmark');
       $patterns_flattened = implode('|', $patterns);
       if (preg_match('/'.$patterns_flattened .'/i',urldecode($url)))
       {echo 'Attacking attempt detected!We hate hackers!';
         die;
       }
       $result = mysqli_query($con, $query);
        if ($result) {
        echo "Thank you for your feedback!";
        }
        else
        {
        echo "Something bad happened :(";
        }

     }

     ?>
 </div>
</body>

</html>
