import re
from time import sleep

from utils.printer import printer


def getHost():
    try:
        print(printer().question("Please, enter the target host IP"))
        input_string = str(input("> "))
        pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
        if re.match(pattern, input_string):
            octets = input_string.split(".")
            if all(0 <= int(octet) <= 255 for octet in octets):
                print(printer().info(f"Target host will be {input_string}"))
                print(printer().info(f"We will proceed through INSECURE HTTP."))
                return input_string
        else:
            print(printer().error("The provided IP address doesn't seems valid."))
            sleep(3)
            exit(1)
    except:
        print(printer().error("An error occurred. Did you cancel the process ?"))
        sleep(3)
        exit(1)
