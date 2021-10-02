# Wild-West | Simple Hidden Directory Fuzzing.
#
# DO NOT USE FOR ILLEGAL PURPOSES!
#
# Written and maintained by Andrew Labby.
#
# A very simple tool used for fuzzing hidden directories faster.
# If you'd like to add your own parameters, simply just add them to pages.log
# you don't need to modify code in order for it to work, I told you it was simple!
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION 
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

try:
    import os
    import sys
    import time
    import requests
    import platform
    import getpass
    import urllib
except Exception:
    print('''
    [!] One or more modules isn't on your system. To fix this, try to install these modules:
    -REQUESTS
    -GETPASS
    -URLLIB
    -PLATFORM
    TO INSTALL, OPEN COMMAND PROMPT OR TERMINAL AND TYPE 'PIP INSTALL [MODULE-NAME]' ''')
    sys.exit()

print("Please review all legal information at: https://github.com/RedHawkInBlueSky/Wild-West. By using this program you agree to all legal conditions.")
time.sleep(2.5)

# After the legal disclaimer is printed, clear the screen
# and launch the program

def WILDWEST_OS_CHECK():
    HOST_OS = platform.platform()

    if "Windows" in HOST_OS:
        os.system("cls")
    else:
        os.system("clear")
WILDWEST_OS_CHECK()

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

#Get input for main website, do not do this inside a class,
# because otherwise the URI data can't be removed.

WILDWEST_HOST = input("Enter Website to Search (i.e. http://www.google.com - Don't use a backslash at the end!):")

def WildWest():

    print(Prefixes.prefixOK + "Wild-West Started.")
    time.sleep(2.0)

    print(Prefixes.prefixOK + "Website set to: " + WILDWEST_HOST + ". Attempting to verify that website is up...")

    # Verify that website is up and running. If it returns a 200 OK code, then it is. But anything else,
    # it's most likely offline.

    verifyConnection = WILDWEST_HOST

    request_response = requests.head(WILDWEST_HOST)
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
    WILDWEST_BACKSLASH1 = WILDWEST_HOST
    WILDWEST_BACKCHECK1 = WILDWEST_BACKSLASH1.endswith('/')

    if WILDWEST_BACKSLASH1 == True:
        print(Prefixes.prefixFailed + "Your website appears to end with '/', for Wild-West to work best, don't add '/' at the end of your URLS.")
        sys.exit()
    else:
        pass
BackSlashCheck()

def WildWestMain():

    # Take the contents of pages.log and parse line-by-line (LBL)
    # and search for pages individually.

    WILDWEST_HOST_FILE = "pages.log"
    WILDWEST_SUCCESS_COUNT = 0

    print(Prefixes.prefixWorking + "Working...")

    with open(WILDWEST_HOST_FILE) as UNDERTOW:
            while (admin_lines := UNDERTOW.readline().rstrip()):

                url = WILDWEST_HOST + admin_lines
                
                try:
                    page = requests.get(url, headers={'User-Agent': 'WILD-WEST'})
                    WildWest_admin1 = page.status_code == 200 and 301
                except requests.exceptions.ConnectionError:
                    print(Prefixes.prefixFailed + "Connection refused by host. Retrying...")
                    time.sleep(10)
                    pass
                except requests.exceptions.TooManyRedirects:
                    print(Prefixes.prefixFailed + "Exceeded redirects limit. Waiting 1 minute and rebooting.")
                    time.sleep(60)
                    pass
                if WildWest_admin1 == False:
                    pass
                else:
                    print(Prefixes.prefixOK + "Possibly interesting webpage found at " + url)
                    WILDWEST_SUCCESS_COUNT += 1

    # Finish parsing, escape the verification sequence
    # then close the program.

    print("\n" + Prefixes.prefixOK + "Wild-West Found: " + str(WILDWEST_SUCCESS_COUNT) + " interesting domain names.")
    print(Prefixes.prefixWorking + "Tasks finished. Press enter to close.")
    
    WILDWEST_KEYINPUT = input("")
    sys.exit()

WildWestMain()
