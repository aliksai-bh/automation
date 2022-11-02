import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
#visiting the uptime kuma
try:
    driver.get("http://10.79.85.55:3001/add")
except:
    print("there was an error in opening the page")
sleep(3)
print(f"login is {os.environ['LOGIN']}, password is {os.environ['PASSWORD']}")
### LOGIN ###
try:
    login = driver.find_element("id","floatingInput")
    password = driver.find_element("id","floatingPassword")
    login_btn = driver.find_element(By.CLASS_NAME,"btn")
    login.send_keys(os.environ['LOGIN'])
    password.send_keys(os.environ['PASSWORD'])
    login_btn.click()
except:
    print("there was an error in login phase")

### ADDING WEBSITE ###
sleep(2)
#giving the name 
try:
    name_field = driver.find_element("id","name")
    name_field.send_keys("test name")
except:
    print('there was an error in naming phase')

#adding url
try: 
    url_field = driver.find_element("id","url")
    url_field.send_keys("apple.com")
except:
    print('there was an error in url adding phase')

#saving
#scroll
try:
    driver.find_element(By.TAG_NAME,"html").send_keys(Keys.END)
    sleep(2)
    save_btn = driver.find_element("xpath",'//*[@id="monitor-submit-btn"]')
    save_btn.click()
except:
    print('there was an error in saving phase')
