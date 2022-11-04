import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import FirefoxOptions

#visiting the uptime kuma

class Automation:
    __driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")
    def __init__(self,url,user_name,password):
        self.url = url
        self.user_name = user_name
        self.password = password

    def login(self):
        try:
            self.__driver.get(self.url)
            sleep(2)
            login_field = self.__driver.find_element("id","floatingInput")
            password_field = self.__driver.find_element("id","floatingPassword")
            login_field.send_keys(self.user_name)
            password_field.send_keys(self.password)

            submit = self.__driver.find_element("class name","btn")
            submit.click()
            sleep(2)
        except:
            print("failed in login phase")
    
    def set_notification(self):
        try:
            notification = self.__driver.find_element("id","notification1")
            notification.click()
        except:
            print("failed in nofication phase!")


    def add_service(self,name,service_url):
        try:
            name_field = self.__driver.find_element("id","name")
            url_field = self.__driver.find_element("id","url")
            name_field.send_keys(name)
            url_field.send_keys(service_url)
        except:
            print("failed in service adding phase")

    def save(self):
        try:
            #scroll down to the end of the page
            self.__driver.find_element(By.TAG_NAME,"html").send_keys(Keys.END)
            sleep(1)
            save_btn = self.__driver.find_element("xpath",'//*[@id="monitor-submit-btn"]')
            save_btn.click()
            self.__driver.quit()
        except:
            print("failed in saving phase")

def main():
    url = "http://10.79.85.55:3001/add"
    # login = os.environ['LOGIN']
    # password = os.environ['PASSWORD']
    login = "admin"
    password = "bh.admin"
    service_name = "test"
    service_url = "apple.com"

    process = Automation(url,login,password)
    process.login()
    process.set_notification()
    process.add_service(service_name,service_url)
    process.save()

if __name__ == "__main__":
    main()



# try:
#     driver.get("http://10.79.85.55:3001/add")
# except:
#     print("there was an error in opening the page")
# sleep(3)
# ### LOGIN ###
# try:
#     login = driver.find_element("id","floatingInput")
#     password = driver.find_element("id","floatingPassword")
#     login_btn = driver.find_element("class name","btn")
#     login.send_keys('admin')
#     password.send_keys('bh.admin')
#     login_btn.click()
#     print("login phase - successful")
# except:
#     print("there was an error in login phase")

# ### ADDING WEBSITE ###
# sleep(2)
# try:
#     notification = driver.find_element("id","notification1")
#     notification.click()
#     print("notification is turned on")
# except:
#     print("failed in notification phase")
# #giving the name 
# try:
#     name_field = driver.find_element("id","name")
#     name_field.send_keys("test name")
#     print("naming phase - successful")
# except:
#     print('there was an error in naming phase')

# #adding url
# try: 
#     url_field = driver.find_element("id","url")
#     url_field.send_keys("apple.com")
#     print("url adding phase - successful")
# except:
#     print('there was an error in url adding phase')

# #saving
# #scroll
# try:
#     driver.find_element(By.TAG_NAME,"html").send_keys(Keys.END)
#     sleep(2)
#     save_btn = driver.find_element("xpath",'//*[@id="monitor-submit-btn"]')
#     save_btn.click()
#     print("saving phase - successful")
# except:
#     print('there was an error in saving phase')
# driver.quit()

