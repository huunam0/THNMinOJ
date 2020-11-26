<?php
/*
/*
** Du an Trinh cham bai mini THNMinOJ
** Trang Dang nhap
** Tran Huu Nam thnam@thptccva - 12/10/2020
*/
*/

echo "<html><head><title>Đăng nhập</title><meta name='author' content='Tran Huu Nam'></head><body>";
//include("thamso.php");
include_once ("funcs.php");
session_start();
$url = pget("r");
if (!$url) $url="index.php";

if (!isset($_SESSION['user_name'])) {
	if (!isset($_POST['dangnhap'])) {
		echo "<h1>Đăng nhập</h1>";
		echo "<form action='?r=$url' method='post'>";
		echo "<p>Tên đăng nhập: <input type='text' name='ten'/></p>";
		echo "<p>Mật khẩu: <input type='password' name='matkhau'></p>";
		echo "<input type='submit' name='dangnhap' value='Đăng nhập'/>";
		echo "</form>";
	} else {
		$ten = $_POST['ten'];
		$mkhau = $_POST['matkhau'];
		if (!file_exists("user/$ten.acc"))
		{
			echo ("Tên đăng nhập không tồn tại!");
			redirect("?r=$url",1);
			exit();
		}
		$nd = file_get_contents(__DIR__ . "/user/$ten.acc");
		$dong = explode(PHP_EOL, $nd);
		if (($dong[0] == md5($mkhau)) || (strpos($dong[0],md5($mkhau))>=0)) {
			$_SESSION['user_name'] = $ten;
			$_SESSION['full_name'] = $dong[1];
			echo "<p>Đăng nhập thành công</p>";
			echo "<p><a href='dangxuat.php'>Thoát</a></p>";
			redirect($url,2);
		} else {
			echo "Thông tin đăng nhập  không đúng!";
			echo $dong[0] ." ". md5($mkhau);
			//redirect("?r=$url",2);
		}
	}
} else {
	echo "<p>Đã đăng nhập với tên <u>".$_SESSION['user_name']."</u></p>";
	echo "<p><a href='dangxuat.php'>Thoát</a></p>";
	redirect($url,2);
}
echo "</body></html>";


?>
