<?php  
$servername="localhost";
$username="root";
$password="";
$dbname="login_form";

$con=mysqli_connect($servername, $username, $password, $dbname);
if($con)  { 
     echo"done";
} 
else{
   echo"Connection error!";
}

	
	$user = $_POST['uname'];
	$passwd = $_POST['password'];
	$query="select * from id where user_name='$user' and password='$passwd'";
    
    $result= mysqli_query($con, $query);
    $check = mysqli_num_rows($result);
   if($check==1){
    session_start();
    $_SESSION['logged']=true;
    header("location:welcome.php");
}
// else{echo"incorrect credentials";}
    
			

?>