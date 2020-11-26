#trinh cham tu dong
#by Tran Huu Nam thnam@thptccva.edu.vn 12/10/2020
#cu phap chamtudong.py 
#------------------------------------------
import argparse
import os
import subprocess
from glob import glob
from os.path import isfile, isdir, join 
import re 
from datetime import datetime
import platform  

#------------------------------------------------------------------------------------
#Khoi tao bien
duoiexe=".exe"
if platform.system() != "Windows":
	duoiexe=""
	
loichay = ""
kqsosanh=""
thumuclamviec = os.path.dirname(os.path.abspath(__file__))
dangcham = join(thumuclamviec,"dangcham.txt")
if isfile(dangcham):
	print("Chuong trinh cham dang ban")
	quit()
dsinput = []
thumucbaitoan = ""
#thumucbailam = ""
bangdiem=join(thumuclamviec,"bangdiem.csv")
mabaitoan = ""
bailam = ""
kieu=1
tgchay=1
bonho=128 #bo nho su dung toi da - default 128MB
inf = ""
outf = "" #- inf, outf: ten file vao/ra 
dung = 0 #- dung: so test dung 
sotestsai=2 #So test sai dau tien co luu lai output
debugmod = 0
#--------------------------------------------------------------------------------
#Ham
def getInts(s):
	return  re.findall('\d+', s)
#--------------------------------------------------------------------------
def ghink(filename, noidung):
	f = open(filename,"a+")
	f.write(noidung + '\n')
	f.close()
def ghink2(filename, noidung, maso):
	f = open(filename,"a+")
	f.write(noidung)
	f.write('#%d \r\r' % maso)
	f.close()
#-----------------------------------------------------
	
def changext(filename, duoi):
	l = len(filename)
	for i in range(1,5):
		if filename[l-i]=='.':
			return filename[:l-i]+duoi
	return filename+duoi
#-----------------------------------------------------
def showHelp():
	pass
#------------------------------------------------------	
def DelFile(tep): # xoa tep neu ton tai
	if isfile(tep):
		os.remove(tep)
#--------------------------------------------------------
def doccauhinh(thumucbaitoan): #Doc cau hinh
	global loichay, tgchay, kieu, inf, outf
	if not isdir(thumucbaitoan):
		#print("unzip" + " " + thumucbaitoan+".zip" + " -d " + thumucbaitoan+" >/dev/null")
		if not isfile(thumucbaitoan+".zip"):
			loichay = "LOI CHAY: Khong co thu muc bai toan"
			return False
		os.system("unzip" + " " + thumucbaitoan+".zip"+ " -d " + os.path.dirname(thumucbaitoan)+" >/dev/null")
	if not isdir(thumucbaitoan):
		loichay = "LOI CHAY: Khong co thu muc bai toan ke ca file zip"
		return False
	fname = join(thumucbaitoan,"chamthi.inf")
	if not isfile(fname):
		loichay = "LOI CHAM: Khong co tep cau hinh"
		return False
	f = open(fname, "r")
	for dong in f:
		dong=dong.strip()  
		tmp = dong.split("=")
		#print(tmp)
		tmp[0] = tmp[0].strip()
		if tmp[0] == "desciption":
			#print ("#",tmp[1])
			pass
		elif tmp[0] == "time":
			tgchay = int(getInts(tmp[1])[0])
		elif tmp[0] == "type":
			kieu = int(getInts(tmp[1])[0])
		elif tmp[0] == "memory":
			bonho = int(getInts(tmp[1])[0])
		elif tmp[0] == "inout":
			inf = tmp[1].strip()
			if inf: # neu input khac rong
				outf = inf + ".out"
				inf = inf + ".inp"
			
	if inf == "": # neu rong thi mac dinh output file name la output.out
		outf = "output.out"
	return True
#----------------------------------------------------
def chuanhoaxau(s): #chuan hoa truc tiep xau s
	tmp = re.sub(' +', ' ', s)
	return tmp.strip()
#-------------------------------------------------------	
def biendich(bai): #dich bai lam co ten la bai
	duoi = bai[-4:]
	manguon = os.path.abspath(bai)
	mamay = manguon[:-4] + duoiexe
	kqdich = manguon[:-4] + ".txt"
	
	DelFile(mamay) #xoa cac file dich cu
	DelFile(kqdich) #Xoa ket qua dich cu
	
	if duoi == ".pas":
		os.system("fpc"+duoiexe + " " + manguon + " > " + kqdich)
	elif duoi == ".cpp":
		os.system("g++"+duoiexe+" -std=c++11 -o " + mamay + " " + manguon + " 2> " + kqdich)
	else:
		ghink(kqdich, "LOI BIEN DICH: Ngon ngu lap trinh khong duoc ho tro.")
		return False
	if not os.path.isfile(kqdich):
		ghink(kqdich, "LOI BIEN DICH: Khong bien dich duoc")
		return False
	if not os.path.isfile(mamay):
		ghink(kqdich, "LOI BIEN DICH: Khong bien dich duoc ra file thuc thi")
		return False
	else:
		DelFile(kqdich)
	return True
def biendich2(bai): #dich bai lam co ten la bai
	duoi = bai[-4:]
	manguon = os.path.abspath(bai)
	mamay = manguon[:-4] + duoiexe
	
	if duoi == ".pas":
		MyOut = subprocess.Popen(["fpc"+duoiexe, manguon], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	else:
		MyOut = subprocess.Popen(["g++"+duoiexe,"-std=c++11","-o",mamay, manguon], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	stdout,stderr = MyOut.communicate()
	print(stdout)	
#------------------------------------------------------------------------	 
def layDSDLvao(thumuc): #lay danh sach file input tu thumuc
	global dsinput,thumuclamviec,loichay
	dsinput = glob(join(thumuc,"test*.inp"))
	if len(dsinput)==0:
		loichay="Khong co file test nao"
		return False
	dsinput.sort()
	#print("So luong bo test: ",len(dsinput))
	return True
#------------------------------------------------------------------------
def soketqua1(outmau, outchay): #so sanh kieu 1 (so khop)
	global kqsosanh
	kqsosanh=""
	strchay = [line.strip() for line in open(outchay)]
	strmau = [line.strip() for line in open(outmau)]
	i = 0
	for dong in strmau:
		if dong:
			if i >= len(strchay): #strchay da het noi dung
				kqsosanh+="SOKQ: Thieu ket qua: " + dong
				return False
			else:
				tmp = dong.split("|")
				#print(tmp)
				strchay[i] = chuanhoaxau(strchay[i])
				if not strchay[i] in tmp:
					kqsosanh+="SOKQ: Sai ket qua: " + strchay[i] + " vs " +dong
					return False
			i+=1
	while i < len(strchay):
		strchay[i] = chuanhoaxau(strchay[i])
		if strchay[i]:
			kqsosanh+="SOKQ: Thua noi dung: " + strchay[i]
			return False
		i+=1
	return True
	
def soketqua2(outmau, outchay): #so sanh kieu 2
	kqsosanh=""
	return False
def soketqua3(outmau, outchay): #so sanh kieu 3 (Thu tu cac dong la tuy y - Dong dau la so luong)
	global kqsosanh
	kqsosanh=""
	strchay = [line.strip() for line in open(outchay)]
	strmau = [line.strip() for line in open(outmau)]
	if strchay[0] != strmau[0]: #so luong khong khop
		kqsosanh+="SOKQ: So luong khong dung : " + strchay[0] + " vs " + strmau[0]
		return False
	strchay.remove(strchay[0])
	strmau.remove(strmau[0])
	for dong in strchay:
		if not dong in strmau:
			kqsosanh+="SOKQ: Thua dong : " + dong
			return False
		else:
			strmau.remove(dong)
	for dong in strmau:
		if dong:
			kqsosanh+="SOKQ: Thieu dong : " + dong
			return False
	return True
def soketqua4(outmau, outchay): #so sanh kieu 4 (Thu tu cac dong la tuy y - khong co so luong)
	global kqsosanh
	kqsosanh=""
	strchay = [line.strip() for line in open(outchay)]
	strmau = [line.strip() for line in open(outmau)]
	for dong in strchay:
		if not dong in strmau:
			kqsosanh+="SOKQ: Thua dong : " + dong
			return False
		else:
			strmau.remove(dong)
	for dong in strmau:
		if dong:
			kqsosanh+="SOKQ: Thieu dong : " + dong
			return False
	return True
	
def soketqua(outmau, outchay, kieu): #so sanh kieu 
	if kieu == 1:
		return soketqua1(outmau, outchay)
	elif kieu == 2:
		return soketqua2(outmau, outchay)
	elif kieu == 3:
		return soketqua3(outmau, outchay)
	elif kieu == 4:
		return soketqua4(outmau, outchay)
	else:
		return False


#------------------------------------------------------------------------
def chaytest(exefile, inputfile,thumucbaitoan): #chay thu voi test 
	global inf, outf, tgchay, loichay, dung, sotestsai
	#print ("Chay test ",exefile, inputfile)
	testsai = sotestsai
	exedir = os.path.dirname(exefile)
	outputmau = changext(inputfile,".out")
	inputname = os.path.basename(inputfile)
	#print("--- CHAY ",inputname)
	output1 = join(exedir,outf)
	DelFile(output1)
	exe_kq = changext(exefile,".txt")
	exe_kq2 = changext(exefile,"2.txt")
	#exe_chay = changext(exefile, "_chay.txt")
	txtkq =  "#"+inputname[:-4]+":"
	#ghink(exe_chay, inputname)
	os.chdir(exedir) #Change working directory to exe_dir
	bd = datetime.now()
	if inf: #Input tu tep
		input1 = join(exedir,inf)
		DelFile(input1)
		os.system("copy " + inputfile + " " + input1 + ">nul")
		proc = subprocess.Popen(exefile, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=exedir)
	else: # Input tu stdin
		myinput = open(inputfile)
		myoutput = open(output1,"w")
		proc = subprocess.Popen(exefile, stdin=myinput, stdout=myoutput, stderr=subprocess.PIPE, cwd=exedir)
	try:
		outs, errs = proc.communicate(timeout = tgchay)
		tg = (datetime.now() - bd).microseconds
	except subprocess.TimeoutExpired: # Chay qua gio
		proc.kill() # close process
		outs, errs = proc.communicate()
		loichay = "LOI CHAY: " + inputname + ": Chay qua thoi gian "
		ghink(exe_kq, txtkq + " Overtime")
		return False
	if proc.returncode != 0: #Chay co loi
		loichay = 'LOI CHAY: "{}" co loi: \n\nstderr: {}\nstdout: {}'.format(inputname, errs.decode('utf-8'), outs.decode('utf-8'))
		ghink(exe_kq, txtkq + " Runtime-Error")
		return False
	#print ("--- --- Time:",tg/1000,"ms")
	txtkq+= " " + str(tg/1000) + "ms "
	if not isfile(output1): #khong co file output
		loichay += "LOI CHAY: " + inputname + ": Khong co file output"
		#print("--- --- LOI: output file not found")
		ghink(exe_kq, txtkq + " NOOUTPUT")
		return False
	
	if kieu == 10: # cham rieng -> goi trinh cham rieng
		chamrieng = join(thumucbaitoan,"chamrieng.py")
		outputo2 = join(exedir, "output.o2")
		if isfile(chamrieng):
			macham = os.system('{} {} {} {} {}'.format(chamrieng,inputfile,outputmau,output1,outputo2))
		else:
			chamrieng = join(thumucbaitoan,"chamrieng"+duoiexe)
			if isfile(chamrieng):
				macham = os.system('{} {} {} {} {}'.format(chamrieng,inputfile,outputmau,output1,outputo2))
			else:
				print("Khong tim thay trinh cham rieng")
				return False
		if not isfile(outputo2): #Khong sinh ra duoc tep output.o2
			#print("Trinh cham rieng khong sinh duoc tep o2")
			ghink(exe_kq, txtkq + " SPJ-ERROR")
			return False
		if soketqua(inputfile[:-3]+".o2", outputo2):
			dung+=1
			#print("--- --- KQ: DUNG")
			ghink(exe_kq, txtkq + " OK ")
			return True
		else:
			#print("--- --- KQ: SAI")
			ghink(exe_kq, txtkq + " WRONG")
			if testsai>0:
				#os.system("copy /Y "+output1+ " " + changext(exefile,"_"+inputname+".txt"))
				testsai-=1
			#print(kqsosanh)
			ghink(exe_kq2,inputname+": "+kqsosanh)
			return False
	else: # Su dung trinh cham mac dinh
		if soketqua(outputmau, output1, kieu):
			dung+=1;
			#print("--- --- KQ: DUNG")
			ghink(exe_kq, txtkq + " OK ")
			return True
		else:
			#print("--- --- KQ: SAI")
			ghink(exe_kq, txtkq + " WRONG")
			if testsai>0:
				#os.system("copy /Y "+output1+ " " + changext(exefile,"_"+inputname+".txt"))
				testsai-=1
			#print(kqsosanh)
			ghink(exe_kq2,inputname+": "+kqsosanh)
			return False
	#sosanhoutput
#-------------------------------------------------------------------------------------
def chay(exefile,thumucbaitoan): #chay cham bai lam exe
	global dsinput, loichay
	#os.system("del /q "+changext(exefile,"_*.txt"))
	exe_chay = changext(exefile,".txt")
	exe_chay2 = changext(exefile,"2.txt")
	#print("So bo test:",len(dsinput))
	for p in dsinput:
		loichay = ""
		chaytest(exefile, p,thumucbaitoan)
		ghink(exe_chay2,loichay)
#----------------------------------------------------------------------
def laymabaitoan(bai):
	tmp = os.path.basename(bai)
	tmp = tmp.split(".")
	tmp = tmp[0].split("_")
	return tmp[0]
#--------
def chambai(bai, thumucbaitoan): #cham bai lam 
	global kieu,dsinput,dung,loichay
	exechay=changext(bai,".txt")
	exechay2=changext(bai,"2.txt")
	DelFile(exechay)
	DelFile(exechay2)
	DelFile(changext(bai,duoiexe))
	DelFile(changext(bai,".o"))
	now=datetime.now()
	ghink(exechay,laymabaitoan(bai)+" " +now.strftime("%H:%M:%S %d-%m-%Y"))
	dung=0
	if (not isdir(thumucbaitoan)) and (not isfile(thumucbaitoan+".zip")):
		loichay+="Khong co thu muc bai toan "+thumucbaitoan
		#print ("Khong co thu muc bai toan",thumucbaitoan)
		ghink(exechay,"ERROR: Problem not found")
		ghink(exechay2,"ERROR: Problem not found")
		return False
	#print ("CHAM:"+bai)
	if not biendich(bai):
		return False
	if not doccauhinh(thumucbaitoan):
		return False
	if kieu == 10: #Kiem tra trinh cham rieng
		if not (isfile(join(thumucbaitoan,"chamrieng.py")) or isfile(join(thumucbaitoan,"chamrieng.cpp"))):
			#khong co trinh cham rieng
			ghink(exechay,"ERROR: SPJ not found")
			ghink(exechay2,"ERROR: SPJ not found")
			return False
	if not layDSDLvao(thumucbaitoan):
		ghink(exechay2,"ERROR: TEST not found")
		return False
	tongtest = len(dsinput)
	chay(changext(bai,duoiexe),thumucbaitoan)
	if loichay:
		#print("Loi cham: ", loichay)
		ghink(exechay2, loichay)
		loichay=""
	ghink(exechay, "Total: "+str(dung)+" / "+str(tongtest))

	
#----------------------------------------------------------------------------------
def thongbaosau(): #thong bao sau khi cham xong
	print("-----------------------------------------")
	print("Cham tu dong, luc ",datetime.now())
	print("By Tran Huu Nam - http://gv.thptccva.edu.vn/thnam")
#---------------------------------------------------------------------------
def test1(): #chay thu 1 file *.exe voi 01 test
	global thumucbaitoan, dsinput
	print ("test1")
	thumucbaitoan="baitoan"
	baitoan="bin2hex"
	doccauhinh(os.path.join(thumucbaitoan,baitoan))
	filechay=join(thumuclamviec,"temp","bin2hex_nam11tin.exe")
	botest=join(thumuclamviec,"baitoan","bin2hex","test2.inp")
	chaytest(filechay,botest,os.path.join(thumucbaitoan,baitoan))
	print ("SO test dung: ",dung)
	print(loichay)
	
def test2(): #chay thu 1 file *.exe voi tat ca bo test
	global thumucbaitoan, dsinput
	
	thumucbaitoan = os.path.join(thumuclamviec,"baitoan","bin2hex")
	doccauhinh(thumucbaitoan)
	layDSDLvao(thumucbaitoan)
	filechay=join(thumuclamviec,"temp","bin2hex_nam11tin.exe")
	print ("test chay:",filechay,thumucbaitoan)
	chay(filechay,thumucbaitoan)
	#print ("SO test dung: ",dung)

def test3(): #cham thu 01 file *.cpp
	global thumucbaitoan
	
	thumucbaitoan = os.path.join(thumuclamviec,"baitoan","bin2hex")
	filechay=join(thumuclamviec,"temp","bin2hex_nam11tin.cpp")
	#filechay=join(thumuclamviec,"temp","bin2hex_2.pas")
	print ("test 3 cham:",filechay,thumucbaitoan)
	chambai(filechay,thumucbaitoan)
	
#------------------------------------------------------------------------------------

# chay cac test
#test3()
#quit()
#------Het chay test------

thumuclaybai = join(thumuclamviec,"upload")
thumuctam = join(thumuclamviec,"temp")


files = glob(thumuclaybai+'/*.cpp')
files.extend(glob(thumuclaybai+'/*.pas'))

dssapxep = {}
for f in files:
	dssapxep[os.path.getmtime(f)]=f;

if len(dssapxep)>0:
	ghink(dangcham,"0")
	for i in sorted (dssapxep):
		file=dssapxep[i]
		file = os.path.basename(file)
		baitoan = laymabaitoan(file)
		#print (file,baitoan)
		#Xoa het thu muc tam
		for f in glob(join(thumuctam,"*.*")):
			os.remove(f)
		#Di chuyen file vaof thu muc tam
		os.replace(join(thumuclaybai,file),join(thumuctam,file))
		#chambai
		chambai(join(thumuctam,file), join(thumuclamviec,"baitoan",baitoan))
		#Di chuyen file vao thu muc bailam
		os.replace(join(thumuctam,file), join(thumuclamviec,"bailam",file))
		#Di chuyen ket qua
		os.replace(join(thumuctam,changext(file,".txt")), join(thumuclamviec,"ketqua",changext(file,".txt")))
		os.replace(join(thumuctam,changext(file,"2.txt")), join(thumuclamviec,"ketqua",changext(file,"2.txt")))
	DelFile(dangcham)
	






#thongbaosau()
#DelFile(dangcham)