import requests
from time import sleep
from constants.constants import ROUTER_DNS_ADDRESS

from utils.printer import printer

def isHostUp(host):
    print(printer().info("Checking target host availability..."))
    try:    
        if requests.get(f"http://{host}", headers={'Host': ROUTER_DNS_ADDRESS}, timeout=7).status_code == 200:
            print(printer().success("Host is UP and ACCESSIBLE"))
            print(printer().info("Proceeding..."))
        else:
            print(printer().error("Host is either DOWN or UNACCESSIBLE"))
            print(printer().info("Aborting..."))
            sleep(3)
            exit(1)
    except:
        print(printer().error(f"Couldn't connect to {host}. No response received !"))
        print(printer().info("Aborting..."))
        sleep(3)
        exit(1)
    
