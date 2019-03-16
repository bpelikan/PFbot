#! python3
# PFbot.py - 

#https://portal.pixelfederation.com/en/profile

import os
from selenium import webdriver

profileURL = "https://portal.pixelfederation.com/en/profile"

os.chdir('C:\\Users\\Barpel\\Documents\\PythonScripts\\PFbotAcc')
currentPath = os.getcwd()
print('Current path: %s' %currentPath)

print("open chrome")
browser = webdriver.Chrome()
print("open site")
browser.get(profileURL)
print("site opened")
browser.close()