#!/usr/bin/python2
# coding=utf-8

import os
import sys
import time
import datetime
import re
import threading
import json
import random
import requests
import hashlib
import cookielib
import uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
__author__ = 'ZEESHII.MALIK'
__copyright = 'All rights reserved . Copyright  ZEESHII.MALIK'
os.system('termux-setup-storage')

try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000, 40000)

header = {
    'x-fb-connection-bandwidth': repr(bd),
    'x-fb-sim-hni': repr(sim),
    'x-fb-net-hni': repr(sim),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }
os.system('git pull')
os.system('clear')
              /|                                           |\                 
             /||             ^               ^             ||\                
            / \\__          //               \\          __// \               
           /  |_  \         | \   /     \   / |         /  _|  \              
          /  /  \  \         \  \/ \---/ \/  /         /  /     \             
         /  /    |  \         \  \/\   /\/  /         /  |       \            
        /  /     \   \__       \ ( 0\ /0 ) /       __/   /        \           
       /  /       \     \___    \ \_/|\_/ /    ___/     /\         \          
      /  /         \_)      \___ \/-\|/-\/ ___/      (_/\ \      `  \         
     /  /           /\__)       \/  oVo  \/       (__/   ` \      `  \        
    /  /           /,   \__)    (_/\ _ /\_)    (__/         `      \  \       
   /  '           //       \__)  (__V_V__)  (__/                    \  \      
  /  '  '        /'           \   |{___}|   /         .              \  \     
 /  '  /        /              \/ |{___}| \/\          `              \  \    
/     /        '       .        \/{_____}\/  \          \    `         \  \   
     /                ,         /{_______}\   \          \    \         \     
                     /         /{___/_\___}\   `          \    
logo = """                                                          
\x1b[0;32m    ____________ ______  _____ _    _ _____ _____ 
\x1b[0;32m   |___  /  ____|  ____|/ ____| |  | |_   _|_   _|
\x1b[0;32m      / /| |__  | |__  | (___ | |__| | | |   | |  
\x1b[0;32m     / / |  __| |  __|  \___ \|  __  | | |   | |  
\x1b[0;30m    / /__| |____| |____ ____) | |  | |_| |_ _| |_ 
\x1b[0;30m   /_____|______|______|_____/|_|  |_|_____|_____|
\x1b[0;30m  ____________ ZEESHII X3 TABIR _______________                                              
\x1b[0;30m  ______WORLD -----------HACKER_____________\\\\\                                                                                                                                                                                                          
\033[1;97m-----------------------------------------------
\x1b[0;36mDEVOLPER    : ZEESHII MALIK
\x1b[0;36mWHATSAAP    : +923072780963
\x1b[0;36mFACEBOOK    : https://www.facebook.com/zeeshii.malik420
\033[1;97m-----------------------------------------------
"""

def log_menu():
    
    try:
        t_check = open('access_token.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\033[1;92m         (Login menu) \033[1;94m'
	print 47 * '-'
        print '\033[1;97m(\033[1;91m1\033[1;97m) Login with FaceBook'
        print '\033[1;97m(\033[1;91m2\033[1;97m) Login with token'
        print '\033[1;97m(\033[1;91m3\033[1;97m) Login with cookies'
        print ''
        log_menu_s()



def log_menu_s():
    s = raw_input(' \033[1;97m••➤ ')
    if s == '1':
        log_fb()
    elif s == '2':
        log_token()
    elif s == '3':
        log_cookie()
    else:
        print ''
        print '\\ Select valid option '
        print ''
        log_menu_s()


def log_fb():
    os.system('clear')
    print logo
    print '\033[1;92m      (Login id/email/pass) \033[1;94m'
    
    print 47 * '-'
    lid = raw_input('\033[1;92m Id/mail/no: ')
    pwds = raw_input(' \033[1;93mPassword: ')
    
    try:
        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd).text
        q = json.loads(data)
        if 'loc' in q:
            ts = open('access_token.txt', 'w')
            ts.write(q['loc'])
            ts.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print ' User must verify account before login'
            raw_input('\033[1;92m Press enter to try again ')
            log_fb()
        else:
            print ' Id/Pass may be wrong'
            raw_input(' \033[1;92mPress enter to try again ')
            log_fb()
    except:
        print ''
        print 'Exiting tool'
        os.system('exit')



def log_token():
    os.system('clear')
    print logo
    print '\033[1;92m         (Login Token) \033[1;94m'
    print 47 * '-'
    tok = raw_input(' \033[1;96mPaste token : \033[1;91m')
    print 47 * '-'
    t_s = open('access_token.txt', 'w')
    t_s.write(tok)
    t_s.close()
    menu()


def log_cookie():
    os.system('clear')
    print logo
    print ''
    print '\033[1;92m      (Login Cookies) \033[1;94m'
    print ''
    
    try:
        cookie = raw_input(' Paste cookies : ')
        data = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36',
            'referer': 'https://m.facebook.com/',
            'host': 'm.facebook.com',
            'origin': 'https://m.facebook.com',
            'upgrade-insecure-requests': '1',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'content-type': 'text/html; charset=utf-8',
            'cookie': cookie }
        c1 = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = data)
        c2 = re.search('(EAAA\\w+)', c1.text)
        hasil = c2.group(1)
        ok = open('access_token.txt', 'w')
        ok.write(hasil)
        ok.close()
        menu()
    except AttributeError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \033[1;92mPress enter to try again ')
        log_menu()
    except UnboundLocalError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \033[1;92mPress enter to try again ')
        log_menu()
    except requests.exceptions.SSLError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \033[1;92mPress enter to try again ')
        log_menu()



def menu():
    os.system('clear')
    
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print ''
        print logo
        print '\033[1;31;1mLogin FB id to continue'
        time.sleep(1)
        log_menu()

    
    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print logo
        print ''
        print '\t Account Cheekpoint\x1b[0;97m'
        print ''
        os.system('rm -rf access_token.txt')
        time.sleep(1)
        log_menu()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\t Turn on mobile data/wifi\x1b[0;97m'
        print ''
        raw_input(' \033[1;92mPress enter after turning on mobile data/wifi ')
        menu()

    os.system('clear')
    print logo
    tok = open('/sdcard/.hst.txt', 'r').read()
    print '  \033[1;92mLogged in user: \033[1;94m' + z
    print 47 * '-'
    print ' \033[1;90m Active token: \033[1;94m' + tok
    print ' ------------------------------------------ '
    print '\033[1;97m(\033[1;91m1\033[1;97m) Start Cloning' 
    print '\033[1;97m(\033[1;91m2\033[1;97m) File Extract'
    print '\033[1;97m(\033[1;91m3\033[1;97m) View token'
    print '\033[1;97m(\033[1;91m4\033[1;97m) Logout'
    print '\033[1;97m(\033[1;91m5\033[1;97m) Delete trash files'
    menu_s()


def menu_s():
    ms = raw_input('\033[1;97m••➤ ')
    if ms == '1':
        auto_crack()
    elif ms == '2':
        os.system('python2 .ok.py')
    elif ms == '3':
        v_tok()
    elif ms == '4':
        lout()
    elif ms == '5':
        rtrash()
        
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu_s()
        
def crack():
    global toket
    
    try:
	toket=open('login.txt','r').read()
    except (KeyError, IOError):
	os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()
    os.system('clear')
    print logo
    print '\033[1;92m         (Choice Pass Cracking) \033[1;97m'
    print 47 * '-'
    print '\033[1;97m(\033[1;91m1\033[1;97m) Dump Friends list'
    print '\033[1;97m(\033[1;91m0\033[1;97m) Back'
    a_s()

def auto_crack(): 
    global token
    
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Login FB id to continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\033[1;92m      (Choice Pass Cracking) \033[1;94m'
    print 47 * '-'
    print '\033[1;97m(\033[1;91m1\033[1;97m) Dump Friends list'
    print '\033[1;97m(\033[1;91m0\033[1;97m) Back'
    a_s()


def a_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' \033[1;97m••➤ ')
    if a_s == '1':
	    os.system('clear')
		print logo
		idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
		try:
			seat = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			op = json.loads(seat.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] Friend not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(50000)&access_token="+fb_token)
		z=json.loads(r.text)
		mkdir('\033[1;91m[✺] \033[1;92mGet all friend id from friend \033[1;97m...')
		print 47*"\033[1;97m═"
		make_action = open('/sdcard/id_from_friends.txt','w')
		for a in z['friends']['data']:
			idfromfriends.append(a['id']+"<=>"+a['name'])
			make_action.write(a['id']+"<=>"+a['name'])
		make_action.close()
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get id \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idfromfriends))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('/sdcard/id_from_friends.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		
		auto_crack()
	
        

if __name__ == '__main__':
    log_menu()
