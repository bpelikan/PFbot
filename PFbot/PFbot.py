#! python3
# PFbot.py - 

#https://portal.pixelfederation.com/en/profile

import os, sys, logging, winsound, datetime
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

def setLoggingFileName(path, fileName):
    logging.basicConfig(filename=os.path.join(path, fileName), level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
    logging.disable(logging.DEBUG)

    #wypisywanie logow na konsole
    root = logging.getLogger()
    ch = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)


filesPath = 'C:\\Users\\Barpel\\Documents\\PythonScripts\\PFbotAcc'
os.chdir(filesPath)
if filesPath != os.getcwd():
    sys.exit()
print('Current path: %s' %os.getcwd())

profileURL = "https://portal.pixelfederation.com/en/profile"
accountLoginFileName = 'logpf.txt'

loggingFolderName = os.path.join(filesPath, 'logs')
os.makedirs(loggingFolderName, exist_ok=True)
setLoggingFileName(loggingFolderName, 'PFbotLog ' + str(datetime.datetime.now().strftime('%Y-%m-%d %H%M%S')) + '.txt')
myUserName, myUserPass = getAccountLoginData(filesPath, accountLoginFileName)


print("open chrome")
browser = webdriver.Chrome()
print("open site")
browser.get(profileURL)
print("site opened")
browser.close()