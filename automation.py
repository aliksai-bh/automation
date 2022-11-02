import os
from selenium import webdriver
from time import sleep

os.environ['PATH'] += r"C:\Users\aliksai\Documents\GitHub\automation"
driver = webdriver.Chrome()

#visiting the uptime kuma
driver.get("http://10.79.85.55:3001/dashboard/")
sleep(3)
login = driver.find_element("id","floatingInput")
password = driver.find_element("id","floatingPassword")

login.send_keys("admin")
password.send_keys("bh.admin")