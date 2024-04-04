<?php

$login = addslashes($_POST["login"]);

if (isset($login)) {
    $conn = new PDO("mysql:host=127.0.0.1;dbname=test", "root", "root");
    var_dump("SELECT * from user WHERE login = \"{$login}\"");
    var_dump($conn->query("SELECT * from user WHERE login = \"{$login}\"")->fetch(PDO::FETCH_ASSOC));
}
?>

<form action="" method="POST">
    <input type="text" name="login" placeholder="login">
    <input type="password" name="pass" placeholder="senha">
    <input type="submit">
</form>
