# -*- coding: utf-8 -*-
#Chuong trinh sinh user
#Tran Huu Nam - huunam0@gmail.com
#5/11/2020

import argparse
import random
import string
import hashlib

parser = argparse.ArgumentParser()
parser.add_argument("username")
parser.add_argument("-p", "--password",  help="Mat khau")
args = parser.parse_args()


if args.username is None:
	print ("Usage: user.py username password");
	quit()

mk = args.password
if mk is None:
	mk = ""
	for i in range(random.randint(6,9)):
		mk+=random.choice(string.digits)
result = hashlib.md5(mk.encode('utf-8')).hexdigest()
print (args.username, mk, result)
f = open("user/"+args.username+".acc", "w")
f.write(result)
f.close()
f = open("user/adu.txt", "a")
f.write(args.username+" "+mk+"\n")
f.close()


	

