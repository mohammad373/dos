import os
import time
from colorama import Fore
import platform

def cls_clear():
    name_system = platform.system()
    if name_system == "Windows":
        os.system("cls")
    elif name_system == "Linux":
        os.system("clear")

def _baner_():
    print(
        Fore.RED + """
                                           _                 
 _ __   ___  __ _  ___ ___ _ __ ___   __ _| | _____ _ __ ___  
| '_ \ / _ \/ _` |/ __/ _ \ '_ ` _ \ / _` | |/ / _ \ '__/ __|
| |_) |  __/ (_| | (_|  __/ | | | | | (_| |   <  __/ |  \__ \\
| .__/ \___|\__,_|\___\___|_| |_| |_|\__,_|_|\_\___|_|  |___/
|_|                                                          
        """
    )

def print_ewe(text , time_entered=0.025):
    import os
    import sys
    import time
    counter = 0
    main_text = str(text)
    while True:
        sys.stdout.write(f"{main_text[counter]}"),sys.stdout.flush()
        counter += 1
        time.sleep(time_entered)
        lenght = len(main_text)
        if counter == lenght:
            break
        else:
            continue
