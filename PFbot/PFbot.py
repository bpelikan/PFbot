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

#account
profileURL = 'https://portal.pixelfederation.com/en/profile'
accountLoginFileName = 'logpf.txt'
myUserName, myUserPass = getAccountLoginData(filesPath, accountLoginFileName)

#logging
loggingFolderName = os.path.join(filesPath, 'logs')
os.makedirs(loggingFolderName, exist_ok=True)
setLoggingFileName(loggingFolderName, 'PFbotLog ' + str(datetime.datetime.now().strftime('%Y-%m-%d %H%M%S')) + '.txt')

#cookies
quoraCookiesFileName = 'QuoraCookiesForUpdates.pkl'
quoraCookiesPath = os.path.join(filesPath, quoraCookiesFileName)

#tags

logging.info('Opening browser...')
browser = webdriver.Chrome()

try:
    logging.info('Opening site...')
    browser.get(profileURL)
except Exception as err:
    logging.error('An exception happened during login: ' + str(err))
    playErrorSound()
logging.info('Site opened...')

if browser.current_url != profileURL:
    logging.info('Log in...')
    try:
        print('Log in and press any key...')
        os.system("pause")

    except Exception as err:
        logging.error('An exception happened during login: ' + str(err))
        playErrorSound()
else:
    print("zalogowany")

try:
    logging.info('Opening site...')
    browser.get(profileURL)
except Exception as err:
    logging.error('An exception happened during login: ' + str(err))
    playErrorSound()

if browser.current_url != profileURL:
    print("niezalogowany")
else:
    print("zalogowany")

#os.system("pause")
#browser.close()

sys.exit()
