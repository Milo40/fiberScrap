from time import sleep
from constants.constants import INSERT_AT_ONCE, WEB_DRIVER
from utils.printer import printer
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def openWanSettings(batch_no: int):
    newLineChar = "\n"
    # print(WEB_DRIVER.execute_script("document.body.children.indexpage.children.maincenter.children.content.children.menuIframe.contentDocument.children.Page.children.wanbody.children.length"))
    try:
        print(printer().info(f"Opening WAN Settings. Batch #{batch_no}"))
        WEB_DRIVER.find_element("id", "addconfig").click()
        WEB_DRIVER.find_element("id", "wanconfig").click()
        WebDriverWait(WEB_DRIVER, 15).until(
            # EC.visibility_of((By.ID, "wanInstTable_tbl"))
            EC.visibility_of((By.XPATH, "//table[@id='wanInstTable_tbl']"))
        )
        sleep(3)

        for x in range(INSERT_AT_ONCE + 1):
            print(printer().info(f"Inserting credentials for connection {int(x+1)}"))
            WebDriverWait(WEB_DRIVER, 15).until(
                EC.element_to_be_clickable((By.ID, f"wanInstTable_record_{x}"))
            )
            WEB_DRIVER.find_element("id", f"wanInstTable_record_{x}").click()
            sleep(1)
            WEB_DRIVER.find_element("id", "UserName").send_keys(
                f"{list(l.rstrip(newLineChar) for l in open('assets/numbers.txt', 'r', encoding='utf-8'))[int(int(f'{batch_no * INSERT_AT_ONCE}') - INSERT_AT_ONCE):int(f'{batch_no * INSERT_AT_ONCE}')][x]}@camnet.cm"
            )
            WEB_DRIVER.find_element("id", "Password").send_keys(
                f"{list(l.rstrip(newLineChar) for l in open('assets/numbers.txt', 'r', encoding='utf-8'))[int(int(f'{batch_no * INSERT_AT_ONCE}') - INSERT_AT_ONCE):int(f'{batch_no * INSERT_AT_ONCE}')][x]}"
            )
            WEB_DRIVER.find_element("id", "ButtonApply").click()
            sleep(15)
            print(printer().success(f"Inserted credentials for connection {int(x+1)}"))
    except:
        print(
            printer().error(
                "An error occurred while inserting the numbers. Could be due to a source code change."
            )
        )
        WEB_DRIVER.close()
        sleep(3)
        exit(1)
