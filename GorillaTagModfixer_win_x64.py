import requests # for downloading BepInEx
import os.path # for checking paths
from colorama import Fore # for making the text cool colors

def exit_with_delay(exit_message, exit_delay = 3, exit_code = 0):
    import time # for setting delay

    # output exit message
    print(exit_message)

    # exit after 3 sec
    time.sleep(exit_delay)
    quit(exit_code)

def is_path_valid(gt_path = ""):
    if os.path.exists(gt_path) and os.path.exists(gt_path+"\Gorilla Tag.exe"):
        return True
    else:
        return False

# Get GTAG path
print(f"{Fore.CYAN}Welcome to the modfixer - MADE BY ASPECT{Fore.WHITE}\nTrying to find path to Gorilla Tag...")
path = ""
if os.path.exists(os.path.expanduser('~') + "\Desktop\Steam\steamapps\common\Gorilla Tag"):
    path = os.path.expanduser('~') + "\Desktop\Steam\steamapps\common\Gorilla Tag"
elif os.path.exists("C:\Program Files (x86)\Steam\steamapps\common\Gorilla Tag"):
    path = "C:\Program Files (x86)\Steam\steamapps\common\Gorilla Tag"
else:
    path = input(f"{Fore.RED}We couldn't find your gtag folder{Fore.WHITE}, point to it yourself: ")

# Ask user to confirm path
if path == os.path.expanduser('~') + "\Desktop\Steam\steamapps\common\Gorilla Tag" or path == "C:\Program Files (x86)\Steam\steamapps\common\Gorilla Tag":
    confirm = input(f"{Fore.GREEN}FOUND PATH{Fore.WHITE}\nThe path found is '{Fore.YELLOW}{path}{Fore.WHITE}', is that the correct path? [y/n]: ")
    if confirm.lower()[0] != 'y':
        path = input("Point us to it: ")

# exit if path isn't valid
print("\nChecking path...")
if is_path_valid(path):
    print(f"{Fore.GREEN}The path is valid{Fore.WHITE}\nGetting files...")
elif path.startswith(os.path.expanduser('~')) == False:
    exit_with_delay(f"{Fore.RED}PATH NOT FOUND, exiting now...{Fore.WHITE}")
else:
    exit_with_delay(f"{Fore.RED}PATH IS NOT VALID, exiting now...{Fore.WHITE}")

# Download BepInEx data
print("Downloading BepInEx...")
url = 'https://github.com/BepInEx/BepInEx/releases/download/v5.4.23.1/BepInEx_win_x64_5.4.23.1.zip'
r = requests.get(url, allow_redirects=True)

# Write data onto file
print("Writing files...")
open('BepInEx_win_x64_5.4.23.1.zip', 'wb').write(r.content)

# importing the zipfile module 
print("Unzipping BepInEx...")
from zipfile import ZipFile 
  
# loading the temp.zip and creating a zip object 
with ZipFile('BepInEx_win_x64_5.4.23.1.zip', 'r') as zObject: 
  
    # Extracting all the members of the zip
    # into a specific location. 
    zObject.extractall( 
        path=path)

if os.path.exists(path+"\BepInEx\config") == False:
    # Create config folder
    print("Creating config folder...")
    os.mkdir(path=path+"\BepInEx\config")

if os.path.exists(path+"\BepInEx\plugins") == False:
    # Create plugins folder
    print("Creating plugins folder...")
    os.mkdir(path=path+"\BepInEx\plugins")
    
# Download config file
print("Downloading config file...")
url = 'https://raw.githubusercontent.com/AspectGTAG/Gorilla-Tag-mod-fixer/main/fixed_BepInEx.cfg'
r = requests.get(url, allow_redirects=True)

# Write data onto file
print("Writing config file...")
open(path+'\BepInEx\config\BepInEx.cfg', 'wb').write(r.content)

# Ask user if they should download Aspect Cheat Panel
a = input("\nDo you want to download Aspects Cheat Panel [y/n]: ")

# If user says yes download Aspects Cheat Panel
if a.lower()[0] == 'y':
    # Get data
    print("\nDownloading Aspects Cheat Panel...")
    url = 'https://github.com/AspectGTAG/Aspect-Cheat-Panel/releases/latest/download/AspectCheatPanel.dll'
    r = requests.get(url, allow_redirects=True)

    # Write data onto file
    print("Writing data to file...")
    open(path+'\BepInEx\plugins\AspectCheatPanel.dll', 'wb').write(r.content)

# Exit after fixing gorillatag mods
print(f"\n{Fore.GREEN}GORILLA TAG MODS HAS BEEN FIXED!{Fore.WHITE}")
exit_with_delay(f"{Fore.RED}Exiting now...{Fore.WHITE}")