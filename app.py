from datetime import datetime as dt
import time

host_path = "/etc/hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]

while True:
	if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
		print("Working Hours...")
		with open(host_path,"r+") as file:
			for website in website_list:
				content=file.read()
				if website in content:
					pass
				else:
					file.write(redirect+" "+website+"\n")

	else:
		print("Fun Hours...")
		with open(host_path,"r+") as file:
			content=file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()

	time.sleep(5)