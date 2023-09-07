from constants.constants import (
    INSERT_AT_ONCE,
    MODEM_MANUFACTURER,
    MODEM_MODEL,
    TOTAL_LINES,
)
from functions.automation.login import authenticate
from functions.automation.openWanSettings import openWanSettings
from functions.automation.openWanStatus import openWanStatus
from functions.input_host import getHost
from functions.is_host_up import isHostUp
from utils.printer import printer


def main():
    print("\n")
    print(
        printer().info(
            "This script will automatically execute some actions on a target host, through HTTP"
        )
    )
    print(
        printer().info(
            f"This script is designed to work with the {MODEM_MANUFACTURER} {MODEM_MODEL}"
        )
    )
    print(
        printer().info(
            "The router should be configured for a CAMTEL Optical Fiber Subscription."
        )
    )
    print("\n")
    host = getHost()
    isHostUp(host)
    authenticate()
    print(printer().info(f"{TOTAL_LINES} detected in the numbers file."))
    print(
        printer().info(f"Which will make {int(TOTAL_LINES / INSERT_AT_ONCE)} batches")
    )
    for batchCount in range(int(TOTAL_LINES / INSERT_AT_ONCE)):
        openWanSettings(int(batchCount + 1))
        openWanStatus(int(batchCount + 1))


if __name__ == "__main__":
    main()
