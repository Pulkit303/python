#!/usr/bin/python2

import time
import os
import webbrowser

x='''
	Press1:to show time
	Press2:to reboot
	Press3:to add a user
	Press4:to search google'''


print x


choice=int(raw_input())

if choice==1:
	print"current time is: " 
	print time.ctime()
elif choice==2:
	print "system rebooting"
	os.system("reboot " )
elif choice==3:
	print "name a user to add"
	name=raw_input()
	os.system("useradd -r "+name)
elif choice==4:
	print "enter the keywords"
	word=raw_input()
	webbrowser.open_new("http://google.com/search?q= "+word)
	
