<?php
include("config.php");
session_start();
if(isset($_POST['username']) && isset($_POST['password']) && isset($_POST['team'])) {
  $conn = new PDO("mysql:host=$db_host;dbname=$db_name", $db_user, $db_pass);
    // set the PDO error mode to exception
  $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  $sql = $conn->prepare("insert into users values (:name,:pass,:team)");
  $username = $_POST['username'];
  $password = $_POST['password'];
  $team = $_POST['team'];
  if($username == "admin"){
    echo "Sorry you can't register as admin";
    die;
  }
  $result = $sql->execute(array(':name' => $username, ':pass' =>$password, ':team' => $team));
  // $database_file = "../users.db";
  // $con = new SQLite3($database_file);
  // $stmt = $con->prepare('SELECT * FROM users WHERE username = :name and password = :password');
  // $stmt->bindValue(':name', $username, SQLITE3_TEXT);
  // $stmt->bindValue(':password', $password, SQLITE3_TEXT);
  // $result = $stmt->execute();
  if(!$sql){
        print "Something's wrong";
        exit(0);
      }
  else{
    echo "Registered successfully!";
  }
}
?>
