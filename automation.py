import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="chromedriver.exe")

#visiting the uptime kuma
driver.get("http://10.79.85.55:3001/add")
sleep(3)

### LOGIN ###
login = driver.find_element("id","floatingInput")
password = driver.find_element("id","floatingPassword")
login_btn = driver.find_element(By.CLASS_NAME,"btn")
login.send_keys("admin")
password.send_keys("bh.admin")
login_btn.click()

### ADDING WEBSITE ###
sleep(2)
#giving the name 
name_field = driver.find_element("id","name")
name_field.send_keys("test name")

#adding url 
url_field = driver.find_element("id","url")
url_field.send_keys("apple.com")

#saving
#scroll
driver.find_element(By.TAG_NAME,"html").send_keys(Keys.END)
sleep(2)
save_btn = driver.find_element("xpath",'//*[@id="monitor-submit-btn"]')
try:
    save_btn.click()
except:
    print('what')