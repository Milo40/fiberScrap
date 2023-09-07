from time import sleep
from constants.constants import WEB_DRIVER
from utils.printer import printer


def openWanStatus(batch_no: int):
    try:
        newLineChar = "\n"
        print(printer().info(f"Opening WAN Status. Batch #{batch_no}"))
        WEB_DRIVER.find_element("id", "Systeminfo").click()
        WEB_DRIVER.find_element("id", "waninfo").click()
        sleep(10)
        # for x in range(INSERT_AT_ONCE + 1):
        #     print(printer().info(f"Inserting credentials for connection #{int(x+1)}"))
        #     WEB_DRIVER.find_element("id", f"wanInstTable_record_{x}").click()
        #     sleep(1)
        #     WEB_DRIVER.find_element("id", "UserName").send_keys(
        #         f"{list(l.rstrip(newLineChar) for l in open('assets/numbers.txt', 'r', encoding='utf-8'))[int(int(f'{batch_no * INSERT_AT_ONCE}') - INSERT_AT_ONCE):int(f'{batch_no * INSERT_AT_ONCE}')][x]}@camnet.cm"
        #     )
        #     WEB_DRIVER.find_element("id", "Password").send_keys(
        #         f"{list(l.rstrip(newLineChar) for l in open('assets/numbers.txt', 'r', encoding='utf-8'))[int(int(f'{batch_no * INSERT_AT_ONCE}') - INSERT_AT_ONCE):int(f'{batch_no * INSERT_AT_ONCE}')][x]}"
        #     )
        #     WEB_DRIVER.find_element("id", "ButtonApply").click()
        #     sleep(15)
        #     print(printer().success(f"Inserted credentials for connection #{int(x+1)}"))
    except:
        print(
            printer().error(
                "An error occurred while checking connection statuses. Could be due to a source code change."
            )
        )
        WEB_DRIVER.close()
        sleep(3)
        exit(1)
