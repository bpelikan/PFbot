#! python3
# PFbot.py - 

#https://portal.pixelfederation.com/en/profile

import os, sys, logging, winsound, datetime, pickle, time, random
from selenium import webdriver
from random import randint

##################################################
##                 FUNCTIONS                    ##
##################################################
def playErrorSound():
    winsound.PlaySound('C:\\Windows\\media\\Windows Exclamation.wav', winsound.SND_FILENAME)
def playFinishSound():
    winsound.PlaySound('C:\\Windows\\media\\Windows Logon.wav', winsound.SND_FILENAME)

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

# def randTime():
#     return (randint(4.0, 10.0))

filesPath = 'C:\\Users\\Barpel\\Documents\\PythonScripts\\PFbotAcc'
os.chdir(filesPath)
if filesPath != os.getcwd():
    sys.exit()
print('Current path: %s' %os.getcwd())

#account
profileURL = 'https://portal.pixelfederation.com/en/profile'
# accountLoginFileName = 'logpf.txt'
# myUserName, myUserPass = getAccountLoginData(filesPath, accountLoginFileName)

#logging
loggingFolderName = os.path.join(filesPath, 'logs')
os.makedirs(loggingFolderName, exist_ok=True)
setLoggingFileName(loggingFolderName, 'PFbotLog ' + str(datetime.datetime.now().strftime('%Y-%m-%d %H%M%S')) + '.txt')

#cookies
quoraCookiesFileName = 'QuoraCookiesForUpdates.pkl'
quoraCookiesPath = os.path.join(filesPath, quoraCookiesFileName)

logging.info('Opening browser...')
browser = webdriver.Chrome()
browser.get('https://www.google.pl/')
time.sleep(1)

#Loading cookies file
if os.path.isfile(quoraCookiesPath) == True:
    logging.info('Loading cookies file')
    try:
        for cookie in pickle.load(open(quoraCookiesPath, "rb")):
            print(cookie)
            browser.add_cookie(cookie)
    except Exception as err:
        logging.error('An exception happened during loading cookies: ' + str(err))
        playErrorSound()

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

        #Zapisanie plikow cookie
        logging.info('Saving cookies')
        cookieFile = open(quoraCookiesPath, "wb")
        pickle.dump(browser.get_cookies() , cookieFile)
        cookieFile.close()

    except Exception as err:
        logging.error('An exception happened during login: ' + str(err))
        playErrorSound()
else:
    print("Already logged")

invitationCount = 0
while True:
    if invitationCount > 1000:
        playFinishSound()
        logging.info('--------- BREAK invitationCount: (%s)' %invitationCount)
        break

    logging.info('--------- InvitationCount: %s ---------' %invitationCount)
    try:
        logging.info('Opening site')
        browser.get(profileURL)
    except Exception as err:
        logging.error('An exception happened during opening site: ' + str(err))
        playErrorSound()
    
    if browser.current_url != profileURL:
        logging.error('User not logged: ')
        logging.error('An exception happened during opening site: ')
        playErrorSound()
        sys.exit()
    
    logging.info('Searching search button...')
    searchButton = browser.find_elements_by_class_name('fa-search')[0]
    searchButton.click()

    logging.info('Searching invite buttons')
    inviteButtons = browser.find_elements_by_class_name('player-list__item__button')
    logging.info('Found %s buttons' %len(inviteButtons))
    
    whileIteractionBreak = 18
    while inviteButtons == []:
        logging.info('Waiting for invite buttons - (%s)' %whileIteractionBreak)
        inviteButtons = browser.find_elements_by_class_name('player-list__item__button')
        logging.info('Found %s buttons' %len(inviteButtons))
        whileIteractionBreak = whileIteractionBreak - 1
        if whileIteractionBreak < 0:
            logging.info('--------- BREAK whileIteractionBreak: (%s)' %whileIteractionBreak)
            break
        if inviteButtons == []:
            sleepTime = 4 #randint(1.0, 4.0)
            logging.info('Sleep time: %s...' %sleepTime)
            time.sleep(sleepTime)

    random.shuffle(inviteButtons)
    i = 1
    for button in inviteButtons:
        button.click()
        invitationCount = invitationCount + 1
        sleepTime = randint(10.0, 50.0)/100
        logging.info('Invitation (%s) click sleep time: %s' %(i, sleepTime))
        i = i + 1
        time.sleep(sleepTime)

    sleepTime = randint(1.0, 9.0)
    logging.info('Sleep time: %s...' %sleepTime)
    time.sleep(sleepTime)
    
#os.system("pause")
#browser.close()

#sys.exit()
