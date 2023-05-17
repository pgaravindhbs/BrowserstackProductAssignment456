from browserstack.local import Local
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import selenium.webdriver.chrome.options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
import selenium.webdriver.safari.options
import selenium.webdriver.firefox.options
import time

def test_example(selenium):
    URL1 = "https://browserstack.com"
    selenium.get(url=URL1)
    selenium.maximize_window()

    def wait_click(xpath_location):
        WDW(selenium, 25).until(EC.visibility_of_element_located((By.XPATH, xpath_location))).click()

    wait_click("//*[@title = 'Sign In']")

    def login_bstack():
        WDW(selenium, 25).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='user_email_login']")))
        time.sleep(1)
        actions = AC(selenium)
        username_location = selenium.find_element(By.XPATH, "//*[@id='user_email_login']")
        username_location.clear()
        username_text = os.environ.get("browserstacktempusername1")
        actions.move_to_element(username_location).click().send_keys(username_text).perform()
        password_location = selenium.find_element(By.XPATH, "//*[@id='user_password']")
        password_location.clear()
        password_text = os.environ.get("browserstacktemppassword1")
        actions.move_to_element(password_location).click().send_keys(password_text).perform()
        selenium.find_element(By.XPATH, "//*[@value='Sign me in']").click()

    login_bstack()
    # wait_click("//*[@id='live_cross_product_explore']")
    wait_click("//*[@aria-label='Big Sur']")
    wait_click("//*[@aria-label='chrome 113 latest']")

    try:
        wait_click("//*[label[contains(text(),'Stop Session')]]")
        print("successfully logged into bstack live")
    except Exception as e:
        print("Error : {} ".format(e))
    selenium.quit()

#     except NoSuchElementException as err:
# message = "Exception: " + str(err.__class__) + str(err.msg)
# driver.execute_script(
#     'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(
#         message) + '}}')
# except Exception as err:
#     message = "Exception: " + str(err.__class__) + str(err.msg)
#     driver.execute_script(
#         'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')
# # Stop the driver
# driver.quit()
# selenium.quit()