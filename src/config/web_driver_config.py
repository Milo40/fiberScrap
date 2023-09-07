import os
from time import sleep
from requests import options
from utils.printer import printer
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions


def driverConfig():
    try:
        if os.name == "nt":
            options = EdgeOptions()
            options.use_chromium = True
            # options.headless = True
            options.add_argument("no-sandbox")
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            driver = webdriver.Edge(
                service=EdgeService(
                    executable_path=EdgeChromiumDriverManager().install()
                ),
                options=options,
            )
            return driver
    except:
        print(
            printer().error(
                "Something went wrong while launching Edge. You may want to check your Internet and try again."
            )
        )
        sleep(3)
        exit(1)

    try:
        if os.name == "posix":
            options = FirefoxOptions()
            # options.headless = True
            options.add_argument("no-sandbox")

            if os.path.exists("/usr/bin/firefox"):
                options.binary_location = "/usr/bin/firefox"
            elif os.path.exists("/usr/bin/firefox-esr"):
                options.binary_location = "/usr/bin/firefox-esr"
            elif os.path.exists("/opt/firefox/firefox"):
                options.binary_location = "/opt/firefox/firefox"
            elif os.path.exists("/opt/firefox-esr/firefox"):
                options.binary_location = "/opt/firefox-esr/firefox"
            else:
                print(
                    printer().error(
                        "We meant to use Firefox, but it doesn't seem to be installed, exiting..."
                    )
                )
                sleep(3)
                exit(1)

            driver = webdriver.Firefox(
                service=FirefoxService(executable_path=GeckoDriverManager().install()),
                options=options,
            )
            return driver
    except:
        print(
            printer().error(
                "Something went wrong... Check your Internet and Firefox installation ?"
            )
        )
        sleep(3)
        exit(1)

    if not os.name == "posix" or os.name == "nt":
        print(printer().error("Your OS is not yet supported, exiting..."))
        sleep(3)
        exit(1)
