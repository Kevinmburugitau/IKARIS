<?php
$username = $_POST['username'];
$regno = $_POST['regno'];
$password = $_POST['password'];
//connect to database
$conn = new mysqli('localhost', 'root', '', 'LOGIN');
//check connection
if ($conn->connect_error) {
    die('Connection failed: ' . $conn->connect_error);
}
else {
    $stmt = $conn->prepare("INSERT INTO Registration (username, regno, password) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $username, $regno, $password);
    $stmt->execute();
    echo "Registration successful!";
    $stmt->close();
    $conn->close();
}
?>