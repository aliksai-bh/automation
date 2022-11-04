import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import FirefoxOptions
import json

class Automation:
    __opts = FirefoxOptions()
    __opts.add_argument("--headless")
    __driver = webdriver.Firefox(executable_path=r"./geckodriver",options=__opts)

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
    payload = json.loads(os.environ['PAYLOAD'])
    service_name = payload['website']
    service_url = payload['url']
    print(f"service - {service_name}, url - {service_url}")
    process = Automation(url,login,password)
    process.login()
    process.set_notification()
    process.add_service(service_name,service_url)
    process.save()

if __name__ == "__main__":
    main()