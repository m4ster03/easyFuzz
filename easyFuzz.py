#By m4ster
#made with wfuzz

from os import *		
from colorama import *		
import subprocess

#Requeriments

subprocess.run(["sudo apt install wfuzz"],shell=True)
subprocess.run(["clear"],shell=True)

#Title

print (Fore.GREEN +"""
███████╗░█████╗░░██████╗██╗░░░██╗
██╔════╝██╔══██╗██╔════╝╚██╗░██╔╝
█████╗░░███████║╚█████╗░░╚████╔╝░
██╔══╝░░██╔══██║░╚═══██╗░░╚██╔╝░░
███████╗██║░░██║██████╔╝░░░██║░░░
╚══════╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░""" + "   " + "Version: 1.0.0" + "  " + "Autor: M4ster" + Fore.WHITE + """
███████╗██╗░░░██╗███████╗███████╗
██╔════╝██║░░░██║╚════██║╚════██║
█████╗░░██║░░░██║░░███╔═╝░░███╔═╝
██╔══╝░░██║░░░██║██╔══╝░░██╔══╝░░
██║░░░░░╚██████╔╝███████╗███████╗
╚═╝░░░░░░╚═════╝░╚══════╝╚══════╝""")	
print("")
print(Fore.WHITE + "Welcome to easyFuzz!!!, the best tool for easy fuzzing")
print("")

#Disclaimer

print("---DISCLAIMER-----------------------------------------------------------------------------")
print("")
print("I am not responsible for improper use of this tool. This tool is made for ethical purposes.")
print("")

#Tool

print("Selecciona el tipo de fuzzing:")
print(" ")
print("1. Subdomain")
print("2. Directory")
print(" ")
print(" ")
selection = input ("Select 1 or 2:")

if selection == "2":
	url = input ("What is the url that you wnat to fuzz: ")
	print("")
	wordlist = input ("What is the wordlist that you want to use: ")
	subprocess.run([f"wfuzz -c --hc=404 -w {wordlist} {url}FUZZ"],shell=True)

elif selection == "1":
	url = input ("What is the url that you want to fuzz: ")
	print("")
	domain = input ("Put only the domain: ")
	print("")
	wordlist = input ("What is the wordlist that you want to use: ")
	subprocess.run([f""" wfuzz -c --hc=404 -w {wordlist} -u "{url}" -H "Host: FUZZ.{domain}" """],shell=True)
else: 
	print("Error: Invalid option")
	


