#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  encryption-generator.py 
#  
#  Copyright 2016 Mualiful Mizan <mualifulmizan@outlook.com>
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

import os
import sys
import base64
import hashlib
from datetime import date
from datetime import datetime

if os.name in ['nt','win32']:
	os.system('cls')
else:
	os.system('clear')
date=date.today()
time=datetime.now()
print "[*] Author Pidof		[*]"
print "[*] encryption generator	[*]"
print "[*] date :",date,"		[*]"
print
back = 'back'
while back == 'back':
	try:	
		menu=raw_input('encrypt or decrypt $ ')
		menu_item="encrypt"
		if menu == menu_item:
			print
			print "----> md5"
			print "----> sha1"
			print "----> sha256"
			print "----> base32"
			print "----> base64"
			print
			raw=raw_input('type and choice one $ ')	
			menu_item="exit"
			if raw == menu_item:
				print "[*] thanks"
				sys.exit()
			menu_item="base64"
			if raw == menu_item:
				telo=raw_input('string $ ')
				base64=base64.b64encode('%s' % (telo))
				for i in(1,2,3,4,5):
					print "[*] encrypted at",time
				print "\n[*] result :",base64
			menu_item="md5"
			if raw == menu_item:
				telo=raw_input('string $ ')
				md5=hashlib.md5('%s' % (telo)).hexdigest()
				for i in(1,2,3,4,5):
					print "[*] encrypted at",time
				print "\n[*] result :",md5
			menu_item="sha256"
			if raw == menu_item:
				telo=raw_input('string $ ')
				sha256=hashlib.sha256('%s' % (telo)).hexdigest()
				for i in(1,2,3,4,5):
					print "[*] encrypted at",time
				print "\n[*] result :",sha256
			menu_item="sha1"
			if raw == menu_item:
				telo=raw_input('string $ ')
				sha1=hashlib.sha1('%s' % (telo)).hexdigest()
				for i in(1,2,3,4,5):
					print "[*] encrypted at",time
				print "\n[*] result :",sha1
			menu_item="base32"
			if raw == menu_item:
				telo=raw_input('string $ ')
				base32=base64.b32encode('%s' % (telo))
				for i in(1,2,3,4,5):
					print "[*] encrypted at",time
				print "\n[*] result :",base32
		menu_telo="decrypt"
		if menu_telo == menu:
			print
			print "----> base64"
			print "----> base32"
			print	
			oke=raw_input('type and choice one $ ')
			menu_telo="base32"
			if menu_telo == oke:
				decode=raw_input('string $ ')
				base32=base64.b32decode('%s' % (decode))
				for i in(5,4,3,2,1):
					print "[*] decrypted at",time
				print "\n[*] result :",base32
			menu_telo="base64"
			if menu_telo == oke:
				decode=raw_input('string base64 $ ')
				base64=base64.b64decode('%s' % (decode)) #this is Bug's
				for i in (5,4,3,2,1):
					print "[*] decrypted at",time
				print "\n[*] result :",base64
		menu_item="exit"
		if menu == menu_item:
			print "[*] thanks for shopping"
			sys.exit()
		back=raw_input('\ntype back or no $ ')
		print "[*] thanks"
	except KeyboardInterrupt:
		print "[*] you press CTRL-C "
		sys.exit()
	
##### Finished #################################### Finished ##################
###############################################################################
#the Bug is cannot decrypt crypto encryption but i will try to repair and make#
#progam is the best ever #you can wait this progam to be version 2.0 		  #
