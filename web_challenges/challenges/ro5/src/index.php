<?php
session_start();
if(!isset($_SESSION['username'])) {
    header('Location: login.php');
	exit(0);
  }
$username = $_SESSION['username'];
$secret = 'MeraGharKaSecretHaiBabuBhaiya';
if(isset($_COOKIE['admin'])){
  if($_COOKIE['admin']==='1'){
      if(array_key_exists("HTTP_USER_AGENT", $_SERVER) && ($_SERVER['HTTP_USER_AGENT'] === 'CS628A')){
        if(array_key_exists("HTTP_REFERER", $_SERVER) && (strpos($_SERVER['HTTP_REFERER'],'securitymooc.in') !== false)){
          if(array_key_exists("HTTP_DNT", $_SERVER) && ($_SERVER['HTTP_DNT'] === '1')){
            if(array_key_exists("HTTP_X_UIDH", $_SERVER)){
              $flag = md5($secret . $username);
              header("X-HTTP-Flag: flag{". $flag . "}");
              echo "Congratulations !! The flag has been sent.Hold your headers high!";
            }
            else{
              print "<p>I'm hungry! Can I get a 'perma-cookie' or 'supercookie' to eat!</p>";
            }
          }
          else{
            print "<p>Only people who are concerned for their privacy will be given access.Turn on Do_Not_Tracking!</p>";
          }
        }
        else{
          print "<p>Only people (requests) coming from securitymooc.in will be allowed!</p>";
        }
      }
      else{
          print "<p>You can view me only from a specially made browser for this class!It's name is 'CS628A'.</p>";
      }
  }
  else{
    print "<p>Only admins are allowed here.Get Lost!</p>";
  }
}
else{
    setcookie('admin', '0');
    print "<p>Only admins are allowed here.Get Lost!</p>";
}
 ?>
