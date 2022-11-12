import requests,random,sys,json,os,re
from time import sleep as slp
from os import system as cmd
import os
totaldmp = 0
count = 0
try:
	os.mkdir('data')
except:
	pass
try:
	os.remove('temp.txt')
except:
	pass
head = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}
logo = " "
def login():
	os.system("clear")
	print(logo)
	try:
		fbcokis= input('[*] Input Your Facebook Cookie : ')
		print(47*"\033[1;37;1m-")
		head = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}
		ftoken = requests.get("https://business.facebook.com/business_locations", headers=head, cookies = {"cookie":fbcokis}).text
		eaag = re.search("(EAAG\w+)",str(ftoken))
		open("data/token.txt", "w").write(eaag.group(1))
		open("data/cookie.txt", "w").write(fbcokis)
		token = open('data/token.txt','r').read()
		main()
	except Exception as e:
		os.system("rm -f data/token.txt")
		print(f"[*] Error {e}")
		slp(2)
		login()
def grep(f):
	o = input('\033[0;97m[->] Save As : \033[1;32;1m')
	print(47*"\033[1;37;1m-")
	try:
		ask_link = int(input('[->] Enter Grip ID Limit : \033[1;32;1m'))
		print(47*"\033[1;37;1m-")
	except:
		ask_link = 1
		completed = 0
	for links in range(ask_link):
		li = input('[✓] Separate Object : \033[1;32;1m')
		os.system('cat '+f+' | grep "'+li+'" >> '+o)
	print(47*"\033[1;37;1m-")
	print("[->] Separating Successful ")
	print("[->] New File Save \033[1;32;1m" + o)
	print(47*"\033[1;37;1m-")
	input("[>>] Press Inter to go Back < ")
	main()
def main():
	totlex = 0
	fbidz = []
	os.system("clear")
	print(logo)
	try:
		fbcokis = open("data/cookie.txt", "r").read()
		token = open('data/token.txt','r').read()
		ftoken = requests.get("https://business.facebook.com/business_locations", headers=head, cookies = {"cookie":fbcokis}).text
		eaag = re.search("(EAAG\w+)",str(ftoken))
	except:
		slp(1)
		login()
	global totaldmp,count
	try:
		token=open('data/token.txt','r').read()
		fbcokis = open("data/cookie.txt", "r").read()
	except FileNotFoundError:
		print("[*] Login Not Found")
		slp(1)
		cmd('rm -rf data/token.txt')
		login()
	try:
		cmd('clear')
		os.system("clear")
		print(logo)
		try:
			fbbuid = input("[->] Enter Public ID Link : ")
			dmp = requests.get("https://graph.facebook.com/"+fbbuid+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
			for idnm in dmp['friends']['data']:
				uidx = idnm['id']
				uidx = uidx[0:6] 
				if uidx in ["100084","100085","100086","100087","100088","100089","100090"]:
					totaldmp+=1
					fbidz.append(idnm['id'])
		except KeyError:
			print("[*] Public ID Not Found")
			menu()
		filepath = input("[>>] Enter File Path : ")
		print("-"*50)
		print("")
		apnd = open(filepath,'w')
		for fbuid in fbidz:
			count += 1
			try:
				dmp = requests.get("https://graph.facebook.com/"+fbuid+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
				for idnm in dmp['friends']['data']:
					uidx = idnm['id']
					uidx = uidx[0:6]
					if uidx in ["100084","100085","100086","100087","100088","100089","100090"]:
						apnd.write(idnm['id']+"|"+idnm['name']+'\n')
						totlex += 1
					sys.stdout.write(f"\r\r\x1b[1;97m[ \x1b[1;92m{totlex}\x1b[1;97m ]\x1b[1;97m")
					sys.stdout.flush()
			except:
				pass
		apnd.close()
		print(47*"\033[1;37;1m-")
		ch_x1 = "n"
		if ch_x1 in ["yes","Yes","YES","Y","y"]:
			newfile = input("[->] File Without Duplicate ID Save As : ")
			os.system('sort -r '+filepath+' | uniq > '+newfile)
			ch_x2 = "n"
			if ch_x2 in ["yes","Yes","YES","Y","y"]:
				grep(newfile)
			else:
				print(47*"-")
				print (f"\x1b[0;37m Your Dump File Save As :\x1b[1;92m {newfile} \x1b[0;37m")
				print(47*'-')
				input("[>>] Press Inter to go Back < ")
				menu()
		else:
			print('\n')
			ch_x2 = "n"
			if ch_x2 in ["yes","Yes","YES","Y","y"]:
				grep(filepath)
			else:
				print(47*'\033[1;37;1m-')
				print (f"\x1b[0;37m Total ID Dump :\x1b[1;92m {totaldmp}")
				print (f"\x1b[0;37m Your Dump File Save As :\x1b[1;92m {filepath} ")
				print(47*'\033[1;37;1m-')
				input("[>>] Press Inter to go Back < ")
				menu()
	except Exception as e:
		print("[>>] Error : %s"%e)
		exit("")
if __name__ == '__main__':
	main()
