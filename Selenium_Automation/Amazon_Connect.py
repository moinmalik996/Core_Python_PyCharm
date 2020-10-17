from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd


# Change this to your own chromedriver path!
webdriver = webdriver.Chrome('C:\\Users\\moinm\\Desktop\\Github\\Core_Python_PyCharm\\Selenium_Automation\\Drivers\\chromedriver.exe') 
# webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)

webdriver.get('https://voice-foundry.awsapps.com/connect/login')
sleep(3)

username = webdriver.find_element_by_id('wdc_username')
username.send_keys('mohsin.malik')
password = webdriver.find_element_by_id('wdc_password')
password.send_keys('Welcome1')

sleep(3)

login = webdriver.find_element_by_id('wdc_login_button')
login.click()

sleep(3)

webdriver.get('https://voice-foundry.awsapps.com/connect/ctr/')

sleep(3)

from_date = webdriver.find_element_by_class_name('c-m-4 > span')
from_date.click()

date = webdriver.find_element_by_css_selector('datepicker-00K-5023-4 > button')
date.click()


table = webdriver.find_element_by_class_name('metric-table')
rows = table.find_elements_by_tag_name('tr')


contact_ids = []


for row in range(rows):
    cells = webdriver.find_element_by_xpath("//table/tbody/tr["+str(row)+"]/td[1]").text()
    contact_ids.append(cells)
    with open("contact_ids.txt", "a") as myfile:
        myfile.write(contact_ids[row])
        myfile.write("\n")
