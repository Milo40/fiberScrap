from config.web_driver_config import driverConfig


ROUTER_DNS_ADDRESS = "www.router.local"
ROUTER_DNS_ADDRESS_WITH_PROTOCOL = "http://router.local/"
LOGIN_USERNAME = "telecomadmin"
LOGIN_PASSWORD = "admintelecom"
MODEM_MANUFACTURER = "HUAWEI"
MODEM_MODEL = "EchoLife HG8245H5"
INSERT_AT_ONCE = 7
WEB_DRIVER = driverConfig()
TOTAL_LINES = len(open("assets/numbers.txt", "r", encoding="utf-8").readlines())
