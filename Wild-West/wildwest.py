# !/usr/bin/env python3
# Wild-West | Simple Hidden Directory Fuzzing.
#
# DO NOT USE FOR ILLEGAL PURPOSES!
#
# Written and maintained by Andrew Labby.
# ---------------------------------------
#
# A very simple tool used for fuzzing hidden directories faster.
# If you'd like to add your own parameters, simply just add them to pages.log
# you don't need to modify code in order for it to work, I told you it was simple!
#
# Modified last at: September 6, 2021.

import os
import sys
import time
import requests
import platform
import getpass
import urllib

print("Please review all legal information at: https://github.com/RedHawkInBlueSky/Wild-West. By using this program you agree to all legal conditions.")
time.sleep(2.5)

os.system("cls" or "clear")

os.system("")

class style():
        BLACK = '\033[30m'
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        BLUE = '\033[34m'
        MAGENTA = '\033[35m'
        CYAN = '\033[36m'
        WHITE = '\033[37m'
        UNDERLINE = '\033[4m'
        RESET = '\033[0m'

prefixOK = style.GREEN + '[+]' + style.RESET + " "
prefixWorking = style.YELLOW + '[-]' + style.RESET + " "
prefixFailed = style.RED + '[!]' + style.RESET + " "
prefixDATA = style.GREEN + '[DATA]' + style.RESET + " "

print('''
           (    (    (                      (            
 (  (      )\ ) )\ ) )\ )    (  (           )\ )  *   )  
 )\))(   '(()/((()/((()/(    )\))(   ' (   (()/(` )  /(  
((_)()\ )  /(_))/(_))/(_))  ((_)()\ )  )\   /(_))( )(_)) 
_(())\_)()(_)) (_)) (_))_   _(())\_)()((_) (_)) (_(_())  
\ \((_)/ /|_ _|| |   |   \  \ \((_)/ /| __|/ __||_   _|  
 \ \/\/ /  | | | |__ | |) |  \ \/\/ / | _| \__ \  | |    
  \_/\_/  |___||____||___/    \_/\_/  |___||___/  |_|                                                     
\n
''')


print(prefixWorking + "Wild-West v. 1.0.1 is a Beta, client may be unstable and prone to crashing. Client is more stable on Windows x64 versions.\n")

# Get input for main website.

hostWebsite = input("Enter Website to Search (i.e. http://www.google.com - Don't use a backslash at the end!):")

def WildWest():

    print(prefixOK + "Wild-West Started.")
    time.sleep(2.0)

    print(prefixOK + "Website set to: " + hostWebsite + ". Attempting to verify that website is up...")

    # Verify that website is up and running. If it returns a 200 OK code, then it is. But anything else,
    # it's most likely offline.

    verifyConnection = hostWebsite

    request_response = requests.head(hostWebsite)
    status_code = request_response.status_code
    website_is_up = status_code == 200 and 301

    if website_is_up == False:
        print(prefixFailed + "Website doesn't appear to be up. Did you enter it like this? HTTP://www.example.com ? - There should be no '/' at the end for Wild-West to work properly.")
        time.sleep(5)

        sys.exit()
    else:
        pass

WildWest()

def BackSlashCheck():

    backslashCheck = hostWebsite

    result = backslashCheck.endswith('/')

    if result == True:
        print(prefixFailed + "Your website appears to end with '/', for Wild-West to work best, don't add '/' at the end of your URLS.")
        time.sleep(5)

        os.system("python wildwest.py")
    else:
        pass

BackSlashCheck()

def WildWestMain():

    # Take the contents of pages.log and parse line-by-line (LBL)
    # and search for pages individually.

    filename = "pages.log"

    wildwest_successful_links = 0

    print(prefixWorking + "Working...")

    with open(filename) as AdminLBL:
            while (admin_lines := AdminLBL.readline().rstrip()):

                url = hostWebsite + admin_lines
                
                page = requests.get(url)
                
                WildWest_admin1 = page.status_code == 200 and 301

                if WildWest_admin1 == False:
                    pass
                else:
                    print(prefixOK + "Yeehaw! Interesting webpage found at " + url)
                    wildwest_successful_links += 1

    print(prefixOK + "\nWild-West Found: " + str(wildwest_successful_links) + " interesting domain names.")

    print(prefixOK + "Tasks finished. Press enter to close.")
    
    waitOnKeyboard1 = input("")
    sys.exit()

WildWestMain()
