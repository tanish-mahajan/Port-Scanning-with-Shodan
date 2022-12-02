import requests,sys,socket
import ipaddress

def getipaddr(ip_str):
    ip_str = socket.gethostbyname(ip_str)
    try:
       ip_obj = ipaddress.ip_address(ip_str)
       checkwithshodan(ip_str)
    except ValueError:
        print("Invalid Ip address or Domain name")

def validate_ip(ip_str):
   try:
       ip_obj = ipaddress.ip_address(ip_str)
       checkwithshodan(ip_str)
   except ValueError:
       getipaddr(ip_str)

def checkwithshodan(ip_str):
    host = requests.get("https://internetdb.shodan.io/"+ip_str).json()
    for i,r in host.items():
        print("\033[1m" + i + "\033[0m","\n",r,"\n")

tocheck = sys.argv[1]
validate_ip(tocheck)
