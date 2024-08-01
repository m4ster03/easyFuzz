from os import *		
from colorama import *		
import subprocess

# Requerimientos
subprocess.run(["sudo apt install wfuzz"], shell=True)
subprocess.run(["clear"], shell=True)

# Título
print(Fore.GREEN + """
███████╗░█████╗░░██████╗██╗░░░██╗
██╔════╝██╔══██╗██╔════╝╚██╗░██╔╝
█████╗░░███████║╚█████╗░░╚████╔╝░
██╔══╝░░██╔══██║░╚═══██╗░░╚██╔╝░░
███████╗██║░░██║██████╔╝░░░██║░░░
╚══════╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░""" + "   " + "Version: 1.0.0" + "  " + "Author: M4ster" + Fore.WHITE + """
███████╗██╗░░░██╗███████╗███████╗
██╔════╝██║░░░██║╚════██║╚════██║
█████╗░░██║░░░██║░░███╔═╝░░███╔═╝
██╔══╝░░██║░░░██║██╔══╝░░██╔══╝░░
██║░░░░░╚██████╔╝███████╗███████╗
╚═╝░░░░░░╚═════╝░╚══════╝╚══════╝""")
print("")
print(Fore.WHITE + "Welcome to easyFuzz!!!, the best tool for easy fuzzing")
print("")

# Descargo de responsabilidad
print("---DISCLAIMER-----------------------------------------------------------------------------")
print("")
print("I am not responsible for improper use of this tool. This tool is made for ethical purposes.")
print("")

# Herramienta
print("Select the type of fuzzing:")
print(" ")
print("1. Subdomain")
print("2. Directory")
print(" ")
print(" ")
selection = input("Select 1 or 2:")

if selection == "2":
    print("")
    url = input("What is the url that you want to fuzz?: ")
    print("")
    wordlist = input("What is the wordlist that you want to use?: ")
    print("")
    hidel = input("Do you want to hide a line?: ")
    if hidel == "no":
        subprocess.run([f"wfuzz -c --hc=404 -w {wordlist} {url}FUZZ"], shell=True)
    elif hidel == "yes":
        print("")
        hidel = input("What line do you want to hide?: ")
        subprocess.run([f"wfuzz -c --hc=404 --hl {hidel} -w {wordlist} {url}FUZZ"], shell=True)
    else:
        print("Error: Invalid option")
        
elif selection == "1":
    print("")
    url = input("What is the url that you want to fuzz?: ")
    print("")
    domain = input("Put only the domain: ")
    print("")
    wordlist = input("What is the wordlist that you want to use?: ")
    print("")
    hidel = input("Do you want to hide a line?: ")
    if hidel == "no":
        subprocess.run([f""" wfuzz -c --hc=404 -w {wordlist} -u "{url}" -H "Host: FUZZ.{domain}" """], shell=True)
    elif hidel == "yes":
        print("")
        hidel = input("What line do you want to hide?: ")
        subprocess.run([f""" wfuzz -c --hc=404 --hl {hidel} -w {wordlist} -u "{url}" -H "Host: FUZZ.{domain}" """], shell=True)
    else:
        print("Error: Invalid option")
        
else: 
    print("Error: Invalid option")
