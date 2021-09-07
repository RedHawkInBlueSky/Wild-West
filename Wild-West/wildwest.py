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

class Prefixes():
    prefixOK = style.GREEN + '[+]' + style.RESET + " "
    prefixWorking = style.YELLOW + '[-]' + style.RESET + " "
    prefixFailed = style.RED + '[!]' + style.RESET + " "
    prefixDATA = style.GREEN + '[DATA]' + style.RESET + " "

print('''

:::       ::: ::::::::::: :::        :::::::::       :::       ::: :::::::::: :::::::: ::::::::::: 
:+:       :+:     :+:     :+:        :+:    :+:      :+:       :+: :+:       :+:    :+:    :+:     
+:+       +:+     +:+     +:+        +:+    +:+      +:+       +:+ +:+       +:+           +:+     
+#+  +:+  +#+     +#+     +#+        +#+    +:+      +#+  +:+  +#+ +#++:++#  +#++:++#++    +#+     
+#+ +#+#+ +#+     +#+     +#+        +#+    +#+      +#+ +#+#+ +#+ +#+              +#+    +#+     
 #+#+# #+#+#      #+#     #+#        #+#    #+#       #+#+# #+#+#  #+#       #+#    #+#    #+#     
  ###   ###   ########### ########## #########         ###   ###   ########## ########     ###     

''')


print(Prefixes.prefixWorking + "Wild-West v. 1.0.2 is a Beta, client may be unstable and prone to crashing. Client is more stable on Windows x64 versions.\n")

# Get input for main website.

hostWebsite = input("Enter Website to Search (i.e. http://www.google.com - Don't use a backslash at the end!):")

def WildWest():

    print(Prefixes.prefixOK + "Wild-West Started.")
    time.sleep(2.0)

    print(Prefixes.prefixOK + "Website set to: " + hostWebsite + ". Attempting to verify that website is up...")

    # Verify that website is up and running. If it returns a 200 OK code, then it is. But anything else,
    # it's most likely offline.

    verifyConnection = hostWebsite

    request_response = requests.head(hostWebsite)
    status_code = request_response.status_code
    website_is_up = status_code == 200 and 301

    if website_is_up == False:
        print(Prefixes.prefixFailed + "Website doesn't appear to be up. Did you enter it like this? HTTP://www.example.com ? - There should be no '/' at the end for Wild-West to work properly.")
        time.sleep(5)

        sys.exit()
    else:
        print(Prefixes.prefixOK + "Website is up! Starting scan.")

WildWest()

def BackSlashCheck():

    backslashCheck = hostWebsite

    result = backslashCheck.endswith('/')

    if result == True:
        print(Prefixes.prefixFailed + "Your website appears to end with '/', for Wild-West to work best, don't add '/' at the end of your URLS.")
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

    print(Prefixes.prefixWorking + "Working...")

    with open(filename) as AdminLBL:
            while (admin_lines := AdminLBL.readline().rstrip()):

                url = hostWebsite + admin_lines
                
                try:
                    page = requests.get(url, headers={'User-Agent': 'internet explorer or something'})
                    WildWest_admin1 = page.status_code == 200 and 301
                except requests.exceptions.ConnectionError:
                    print(Prefixes.prefixFailed + "Connection refused by hosting. Retrying...")
                    time.sleep(10)
                    pass
                except requests.exceptions.TooManyRedirects:
                    print(Prefixes.prefixFailed + "Exceeded redirects limit. Waiting 1 minute and rebooting.")
                    time.sleep(60)
                    pass
                if WildWest_admin1 == False:
                    pass
                else:
                    print(Prefixes.prefixOK + "Yeehaw! Interesting webpage found at " + url)
                    wildwest_successful_links += 1

                        
    print("\n" + Prefixes.prefixOK + "Wild-West Found: " + str(wildwest_successful_links) + " interesting domain names.")

    print(Prefixes.prefixWorking + "Tasks finished. Press enter to close.")
    
    waitOnKeyboard1 = input("")
    sys.exit()

WildWestMain()
