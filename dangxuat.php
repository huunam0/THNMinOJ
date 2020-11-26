<?php
/*
/*
** Du an Trinh cham bai mini THNMinOJ
** Trang Dang xuat
** Tran Huu Nam thnam@thptccva - 12/10/2020
*/
*/

//echo "<html><head><title>Đăng nhập</title><meta name='author' content='Tran Huu Nam'></head><body>";
//include("thamso.php");
include_once ("funcs.php");
session_start();
unset($_SESSION);
session_destroy();
echo "Đã thoát";
redirect("dangnhap.php",3);
//echo "</body></html>";

?>
