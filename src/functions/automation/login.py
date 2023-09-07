from time import sleep
from constants.constants import (
    LOGIN_PASSWORD,
    LOGIN_USERNAME,
    ROUTER_DNS_ADDRESS_WITH_PROTOCOL,
    WEB_DRIVER,
)
from utils.printer import printer


def authenticate():
    print(printer().info("Authentication required. Authenticating..."))
    try:
        WEB_DRIVER.get(f"{ROUTER_DNS_ADDRESS_WITH_PROTOCOL}")
        WEB_DRIVER.find_element("id", "txt_Username").send_keys(f"{LOGIN_USERNAME}")
        WEB_DRIVER.find_element("id", "txt_Password").send_keys(f"{LOGIN_PASSWORD}")
        WEB_DRIVER.find_element("id", "loginbutton").click()
        sleep(5)
        print(printer().success("Authentication successful. Proceeding..."))
    except:
        print(
            printer().error(
                "An error occurred while Authenticating... Possibly due to a network variation or a change in the page source."
            )
        )
        print(printer().error("You may try again."))
        WEB_DRIVER.close()
        sleep(3)
        exit(1)
