#!/usr/bin/env python
import argparse
import signal 
import os 
try : 
	import mechanize , youtube_dl 
	import sys  , re
	from bs4 import BeautifulSoup
except : 
	print "[-] Dependacies not found"
	print "[*] Downloading now "
	os.system("sudo pip install BeautifulSoup4 , mechanize , youtube_dl")

def receive_signal(signal, frame):
	print ""
	print '[+]Exiting'
	exit()
# register the handler
signal.signal(signal.SIGINT, receive_signal)

# cli args
parser = argparse.ArgumentParser(description="got.py http://www.vidbaba.com/new_files/xxxxxxxxxxxx")
parser.add_argument('-u', type=str, help="Vidbaba URL", required=True)

cmdargs = parser.parse_args()
resoluton = raw_input("1 For HD \n2 For 360px\n: ")
if int(resoluton) == 1 : 
	hd = "718"
	print "[+] You chose HD "
else : 
	hd = "360"
	print "[+] You chose 360px "
# grab vpn password from vpnbook website
def getVideoURL(url,hd) : 
	br = mechanize.Browser()
	br.set_handle_equiv(True)
	br.set_handle_gzip(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)
	br.addheaders = [('User-agent',' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0'),
                 ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                 ('Accept-Encoding', 'gzip,deflate,sdch'),
                 ('Accept-Language', 'en-US,en;q=0.8'),
                 ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3')]
	temp_url = url.split("/")
	new_url = ["http:/","mycollection.net",temp_url[3],"embed",temp_url[-1]]
	url  = "/".join(new_url)
	br.open(url)

	res = br.response().read()
	bt = BeautifulSoup(res,"lxml")
	script = bt.find("script" , text=re.compile("jwplayer"))
	to_string = script.string.split("\n")
	for i in range(len(to_string)):
		if hd in to_string[i] : 
			video_url =  to_string[i-1]
			return video_url 

res =  getVideoURL(cmdargs.u,hd).split('"')[1]
if res != "" : 
	print "[+] NOW Downloading :  "
	os = os.system("youtube-dl -c "+res)
	if os == 0 :  
		print "[+] Done , Happy watching :)"
	else : 
		print "[-] Not completed , please retry "
else : 
	print "[-] Not Found :("
