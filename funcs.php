<?php
/*
/*
** Du an Trinh cham bai mini THNMinOJ
** Mot so ham dung chung
** Tran Huu Nam thnam@thptccva - 12/10/2020
*/
*/

function redirect($location, $delaytime = 0) {
    if ($delaytime>0) {    
        header( "refresh: $delaytime; url='".str_replace("&amp;", "&", $location)."'" );
    } else {
        header("Location: ".str_replace("&amp;", "&", $location));
    }    
}
function dirspace() {
	$agent = $_SERVER['HTTP_USER_AGENT'];
	if(preg_match('/Win/',$agent)) 
		return "\\"; //windows
	else 
		return "//";  //Linux and others
}

function pget($s)
{
	if (!isset($_GET[$s])) return "";
	return $_GET[$s];
}
function ppost($s)
{
	if (!isset($_POST[$s])) return "";
	return $_POST[$s];
}
function includeornot($tenfile,$thongbao="")
{
	if (file_exists($tenfile))
		include($tenfile);
	else
		echo $thongbao;
}

$tennd = isset($_SESSION['user_name']) ? $_SESSION['user_name'] : "";
$tendaydu = isset($_SESSION['full_name']) ? $_SESSION['full_name'] : "";
date_default_timezone_set("Asia/Ho_Chi_Minh");
$whitelist = array(
    '127.0.0.1',
    '::1'
);
$MYIP=$_SERVER['REMOTE_ADDR'];
$local = in_array($MYIP, $whitelist) || $tennd=="thn";



?>
