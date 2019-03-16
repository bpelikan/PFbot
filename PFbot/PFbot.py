#! python3
# PFbot.py - 

#https://portal.pixelfederation.com/en/profile

import os, sys, logging, winsound
from selenium import webdriver


##################################################
##                 FUNCTIONS                    ##
##################################################
def playErrorSound():
    winsound.PlaySound('C:\\Windows\\media\\Windows Exclamation.wav', winsound.SND_FILENAME)

def getAccountLoginData(logPath, fileName):
    try:
        filePath = os.path.join(logPath, fileName)
        logging.debug('Funkcja: getAccountLoginData(%s)' %filePath)
        file = open(filePath)
        filedata = file.readlines()
        for i in range(len(filedata)-1):
            filedata[i] = filedata[i][:-1]
        return filedata
    except Exception as err:
        logging.error('An exception happened during loading account login data: ' + str(err))
        playErrorSound()
        return ['','']
    finally:
        file.close()



filesPath = 'C:\\Users\\Barpel\\Documents\\PythonScripts\\PFbotAcc'
os.chdir(filesPath)
if filesPath != os.getcwd():
    sys.exit()
print('Current path: %s' %os.getcwd())

profileURL = "https://portal.pixelfederation.com/en/profile"
accountLoginFileName = 'logpf.txt'

myUserName, myUserPass = getAccountLoginData(filesPath, accountLoginFileName)


print("open chrome")
browser = webdriver.Chrome()
print("open site")
browser.get(profileURL)
print("site opened")
browser.close()