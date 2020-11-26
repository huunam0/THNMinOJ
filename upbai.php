<html>
<head>
<meta charset='utf8'/>
</head>
<body>
<?php
/*
** Du an Trinh cham bai mini THNMinOJ
** Trang up bai toan moi len he thong
** Tran Huu Nam thnam@thptccva - 12/10/2020
*/
		if (isset($_POST['upload'])) { //co bai de cham
			$ufile = uploadFile("tep","baitoan");
			echo "<p>Uploaded - $ufile - successfully!</p>";
			echo "<p><a href='?'>Up Next</a></p>";
			redirect("?",30);
		}
		else {
			echo "<h3>UPLOAD</h3>";
			echo '<form action="" method="post" enctype="multipart/form-data">';
			echo '<input id="tep" name="tep" type="file" />';
			echo '<input type="submit" name="upload" value="Upload"/>';
			echo '</form>';	
		}

function uploadFile($uname,$folder,$debug=false) {
	if ($debug) print_r($_FILES);
	if (!empty($_FILES[$uname])) {
		if (is_uploaded_file($_FILES[$uname]["tmp_name"])){
			if ($_FILES[$uname]["error"] > 0)  {
				if ($debug) echo "Upload file with error : " . $_FILES[$uname]["error"] . "<br />";
				return "";
			} else {
				if ($debug) echo "Upload: " . $_FILES[$uname]["name"] . "<br />";
				if ($debug) echo "Type: " . $_FILES[$uname]["type"] . "<br />";
				if ($debug) echo "Size: " . ($_FILES[$uname]["size"] / 1024) . " Kb<br />";
				if ($debug) echo "Temp file: " . $_FILES[$uname]["tmp_name"] . "<br />";
				$filename = $_FILES[$uname]["name"];
				move_uploaded_file($_FILES[$uname]["tmp_name"], $folder. "/" . $filename);
				return $filename;
			}
		} else {
			if ($debug) echo "Upload Fail";
			return "";
		}
	}
	if ($debug) echo "Not found";
	return "";
}
function redirect($location, $delaytime = 0) {
    if ($delaytime>0) {    
        header( "refresh: $delaytime; url='".str_replace("&", "&", $location)."'" );
    } else {
        header("Location: ".str_replace("&", "&", $location));
    }    
}
?>
</body>
</html>