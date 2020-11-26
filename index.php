<?php
/*
** Du an Trinh cham bai mini THNMinOJ
** Trang chu
** Tran Huu Nam thnam@thptccva - 12/10/2020
*/
session_start();
include_once("funcs.php");
if (!isset($_SESSION['user_name'])) die("Chưa <a href='dangnhap.php'>đăng nhập</a>");

echo "<html><head><title>Trang chủ</title><meta name='author' content='Tran Huu Nam'/><meta http-equiv='refresh' content='15'></head><body>";

$username = $_SESSION['user_name'];
if (isset($_POST['changepass']))
{
	$oldpass = $_POST['oldpass'];
	$newpass = $_POST['newpass'];
	$newpas2 = $_POST['newpas2'];
	
	if (!file_exists("user/$username.acc")) die("Khong tim thay nguoi dung.");
	$nd = file_get_contents("user/$username.acc");
	$dong = explode(PHP_EOL, $nd);
	if ($dong[0] == md5($oldpass)) {
		//$_SESSION['user_name'] = $ten;
		//$_SESSION['full_name'] = $dong[1];
		if ($newpass != $newpas2) die("Mat khau moi khong khop.");
		$dong[0] = md5($newpass);
		$nd = implode(PHP_EOL, $dong);
		file_put_contents("user/$username.acc",$nd);
		//ghink("act.log","$username,change pass\n");
		echo "<p>Đổi mật khẩu thành công</p>";
	} else {
		echo "Mật khẩu cũ không đúng!";
		
	}
	redirect("index.php",3);
}
elseif (isset($_POST['nopbai']))
{
	$sbd = $_POST['sobd'];
	if ($sbd) {
		$made = ppost('made');
		$thumuc="upload";
		$mabai = uploadFile("nfile",$thumuc,$sbd,defined("DEBUG"));
		if ($mabai) {
			echo "Đã nộp xong.<br/>[".$sbd."] Nộp bài : [".$mabai."]";
			//ghi nhat ki nop bai:
			//file_put_contents("." .  "\upload.log",$sbd. " " . $mabai . " ".date('Y-m-d H:i:s ').$_SERVER['REMOTE_ADDR']."\n",FILE_APPEND);
			if (!is_dir("baitoan/$mabai") && !file_exists("baitoan/$mabai.zip"))
				echo "<p>Không có bài toán nào như vậy! Kiểm tra lại tên tệp.</p>";
			echo "<div><a href='?'>Quay lại trang chủ</a></div>";
			
			//redirect("?b=$baitap",30);
		}
		else echo "<p>Nộp bài không thành công!</p>";
	} else {
		echo "Cần nhập tên hoặc số báo danh: dùng các chữ cái a-z, chữ số 0-9; không được có dấu cách";
	}
	//redirect("bai.php?thi=$kithi&bai=$bai",12);
	redirect("index.php",3);
}

echo "<h3>Hi, $username. [<span title='Bấm vào để đổi mật khẩu' onclick='document.getElementById(\"doimatkhau\").style.display=\"block\";'>Đổi MK</span>] [<a href='dangxuat.php'>Thoát</a>]</h3>";
//echo "<p onclick='alert(4);'>Alert</p>";
echo "<div id='doimatkhau' style='display:none;'><form action='?' method='post'><h3>Đổi mật khẩu</h3>";
echo "<p>Mật khẩu đang dùng <input name='oldpass' type='password'/></p>";
echo "<p>Mật khẩu mới <input name='newpass'  type='password'/></p>";
echo "<p>Gõ lại mật khẩu mới <input name='newpas2'  type='password'/></p>";
echo "<p>Cập nhật <input name='changepass' type='submit' value='Cập nhật' /></p>";
echo "</form></div>";
echo "<hr/><div><b>NỘP  BÀI</b>";
	
echo "<form action='' method='post' enctype='multipart/form-data'>";
echo "Thí sinh:<b> $tennd </b><input name='sobd' type='hidden' value='$tennd'>";
echo "<span style='margin-left:20px;'>Tệp bài làm: </span><input name='nfile' type='file'  id='nfile'>";
echo " <input name='nopbai' type='submit' value='Nộp bài' style='margin-left:20px;'>";
echo "</form></div>";

//cac bài chờ chấm
$files = array();
if ($handle = opendir("upload")) 
{
	while (false !== ($file = readdir($handle)))
	{
		if (strpos($file,$tennd) !== false)
		{
			$files[filectime("upload/$file")] = $file;
		}
	}
	closedir($handle);
	
}
if ($files)
{
	echo "<h3>Bạn có ".count($files)." bài chờ chấm.</h3>";
	krsort($files);
	echo "<div id='cacbaicho'><ol>";
	foreach($files as $file)
	{
		echo "<li>$file - ".date("H:i:s d-m-Y",filectime("upload/$file"))."</li>";
	}
	echo "</ol></div>";	
}

//cac bài đã chấm xong
unset($files);
$files = array();
if ($handle = opendir("ketqua")) 
{
	while (false !== ($file = readdir($handle)))
	{
		if (strpos($file,$tennd) !== false)
		{
			$files[filectime("ketqua/$file")] = $file;
		}
	}
	closedir($handle);
	
}
if ($files)
{
	echo "<h3>Có ".count($files)." bài đã chấm xong.</h3>";
	krsort($files);
	echo "<div id='cacbainop'><ol>";
	foreach($files as $file)
	{
		$bai=substr($file,0,strpos($file,"_"));
		echo "<li><a href='ketqua.php?bai=$bai' target='_blank'>$bai</a>   ".date("H:i:s d-m-Y",filectime("ketqua/$file"))."</li>";
	}
	echo "</ol></div>";	
}

echo "</body></html>";
function uploadFile($uname,$folder,$sbd,$debug=false) { //tra ve phan ten tep
	if ($debug) print_r($_FILES);
	//if (!file_exists($folder)) mkdir($folder);
	if (!empty($_FILES[$uname])) {
		if (is_uploaded_file($_FILES[$uname]["tmp_name"])){
			if ($_FILES[$uname]["error"] > 0)  {
				if ($debug) echo "Upload file with error : " . $_FILES[$uname]["error"] . "<br />";
				return "";
			} else {
				$i=1;
				$fileinfo=pathinfo($_FILES[$uname]["name"]);
				$filename=$fileinfo['filename'] . "_" . $sbd . "." . $fileinfo['extension'];
				$filename=strtolower($filename);
				if (file_exists($folder. "/" . $filename)) unlink($folder. "/" . $filename);
				
				move_uploaded_file($_FILES[$uname]["tmp_name"], $folder. "/" . $filename);
				return $fileinfo['filename'];
			}
		} else {
			if ($debug) echo "Upload Fail";
			return "";
		}
	}
	if ($debug) echo "Not found";
	return "";
}
?>
<hr><a href="mailto:thnam@thptccva.edu.vn">THNOJ</a> 2020
</body>
</html>
