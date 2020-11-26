<html>
<head>
<title>Bảng điểm</title>

</head>
<body>
<?php
/*
** Du an Trinh cham bai mini THNMinOJ
** Trang Xem ket qua lam bai
** Tran Huu Nam thnam@thptccva - 12/10/2020
*/
session_start();
include_once("funcs.php");
if (!$tennd) die("Chưa <a href='dangnhap.php'>đăng nhập</a>");

if (!isset($_GET['bai'])) die("Phải chọn bài toán.");

$bai=$_GET['bai'];
echo "<h3>RESULT: $bai</h3>";
if (!file_exists("ketqua/".$bai."_".$tennd.".html")) 
{
	if (!file_exists("ketqua/".$bai."_".$tennd.".txt")) die ("Không tìm thấy kết quả");
	$txt= file_get_contents("ketqua/".$bai."_".$tennd.".txt");
}
else
	$txt= file_get_contents("ketqua/".$bai."_".$tennd.".html");
$pattern = '/#(\w+):/i';
$replacement = "</p><p><a target='_blank' href='test.php?b=$bai&t=$1'>$1</a>:";

$txt= preg_replace($pattern, $replacement, $txt);
$txt = str_replace("Total:","</p><p><b>Total: ",$txt);
echo "<p>".$txt."</b></pr>";
?>
</body>
</html>
