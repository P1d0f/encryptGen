#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
#  encryption-generator.py 
#  
#  Copyright 2016 Netuser <zorgonteam@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA. 
#  encryption-generator.py Version 1.0
#  site http://zorgonteam.wordpress.com

import os
import sys
import base64
import hashlib
from datetime import date
from datetime import datetime

date=date.today()
time=datetime.now()
if os.name in ['nt','win32']:
	os.system('cls')
else:
	os.system('clear')
print "[*] Author Netuser		[*]"
print "[*] encryption generator	[*]"
print "[*] date :",date,"		[*]"
print
back = 'back'
while back == 'back':
	try:	
		menu=raw_input('\nencrypt or decrypt $ ')
		menu_item="help"
		if menu == menu_item:
			print """
			you just type encrypt or decrypt 
			example : 
			encrypt = encrypt or decrypt $ encrypt (enter)
			decrypt = encrypt or decrypt $ decrypt (enter)
			""" 
		menu_item="encrypt"
		if menu == menu_item:
			print
			print "----> md5"
			print "----> sha1"
			print "----> sha224"
			print "----> sha256"
			print "----> sha384"
			print "----> sha512"
			print "----> base16"
			print "----> base32"
			print "----> base64"
			print
			raw=raw_input('type and choice one $ ')	
			menu_item="exit"
			if raw == menu_item:
				print "[*] thanks for shopping"
				sys.exit()
			menu_item="base16"
			if menu_item == raw:
				telo=raw_input('string $ ')
				base16=base64.b16encode('%s' % (telo))
				for i in(5,4,3,2,1):
					print "[*] encoded at",time
				print "\n[*] result :",base16
			menu_item="sha224"
			if menu_item == raw:
				telo=raw_input('string $ ')
				sha224=hashlib.sha224('%s' % (telo)).hexdigest()
				for i in(5,4,3,2,1):
					print "[*] encrypted at",time
				print "\n[*] result :",sha224
			menu_item="sha384"
			if menu_item == raw:
				telo=raw_input('string $ ')
				sha384=hashlib.sha384('%s' % (telo)).hexdigest()
				for i in(5,4,3,2,1):
					print "[*] encrypted at",time
				print "\n[*] result :",sha384
			menu_item="sha512"
			if menu_item == raw:
				telo=raw_input('string $ ')
				sha512=hashlib.sha512('%s' % (telo)).hexdigest()
				for i in(5,4,3,2,1):
					print "[*] encrypted at",time
				print "\n[*] result :",sha512
			menu_item="base64"
			if menu_item == raw:
				telo=raw_input('string $ ')
				base64=base64.b64encode('%s' % (telo))
				for i in(1,2,3,4,5):
					print "[*] encoded at",time
				print "\n[*] result :",base64
			menu_item="md5"
			if menu_item == raw:
				telo=raw_input('string $ ')
				md5=hashlib.md5('%s' % (telo)).hexdigest()
				for i in(1,2,3,4,5):
					print "[*] encrypted at",time
				print "\n[*] result :",md5
			menu_item="sha256"
			if menu_item == raw:
				telo=raw_input('string $ ')
				sha256=hashlib.sha256('%s' % (telo)).hexdigest()
				for i in(1,2,3,4,5):
					print "[*] encrypted at",time
				print "\n[*] result :",sha256
			menu_item="sha1"
			if menu_item == raw:
				telo=raw_input('string $ ')
				sha1=hashlib.sha1('%s' % (telo)).hexdigest()
				for i in(1,2,3,4,5):
					print "[*] encrypted at",time
				print "\n[*] result :",sha1
			menu_item="base32"
			if menu_item == raw:
				telo=raw_input('string $ ')
				base32=base64.b32encode('%s' % (telo))
				for i in(1,2,3,4,5):
					print "[*] encoded at",time
				print "\n[*] result :",base32
		menu_telo="decrypt"
		if menu_telo == menu:
			print
			print "----> base16"
			print "----> base32"
			print "----> base64"
			print	
			oke=raw_input('type and choice one $ ')
			menu_telo="base16"
			if oke == menu_telo:
				raw1=raw_input('string base16 $ ')
				dec16=base64.b16decode('%s' % (raw1))
				for i in(5,4,3,2,1):
					print "[*] decoded at",time
				print "\n[*] result :",dec16
			menu_telo="base32"
			if oke == menu_telo:
				raw2=raw_input('string base32 $ ')
				dec32=base64.b32decode('%s' % (raw2))
				for i in(5,4,3,2,1):
					print "[*] decoded at",time
				print "\n[*] result :",dec32
			menu_telo="base64" 				#this is Bug Sorry
			if oke == menu_telo:				#
				raw3=raw_input('string base64 $ ')	#
				dec64=base64.b64decode('%s' % (raw3))	#
				for i in (5,4,3,2,1):			#
					print "[*] decoded at",time	#
				print "\n[*] result :",dec64		#
			menu_telo="exit"
			if menu_telo == oke:
				print "[*] thanks for shopping"
				sys.exit()
		menu_item="exit"
		if menu == menu_item:
			print "[*] thanks for shopping"
			sys.exit()
	except KeyboardInterrupt:
		print "\n[*] ctrl+c active "
		sys.exit()
	
##### Finished #################################### Finished ##################
###############################################################################
#the Bug is cannot decrypt crypto encryption but i will try to repair and make#
#progam is the best ever #you can wait this progam to be version 2.0 	      #
