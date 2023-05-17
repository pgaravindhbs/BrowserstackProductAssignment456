try:
    import os
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium import webdriver
    import selenium.webdriver.chrome.options
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    from selenium.webdriver.support.ui import WebDriverWait as WDW
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.common.action_chains import ActionChains as AC
    from selenium.webdriver.common.by import By
    import selenium.webdriver.safari.options
    import selenium.webdriver.firefox.options
    import time
    print("All Modules are loaded")
except Exception as e:
    print("Error : {} ".format(e))

def test_chrome():
    options = selenium.webdriver.chrome.options.Options()
    options.add_experimental_option("detach", True)
    options.add_argument(r"--user-data-dir=/Users/aravindhpg/python-selenium-browserstack/tests/C:/Users/aravindhpg/Library/Application Support/Google/Chrome/Profile 2")
    options.add_argument(r"--profile-directory=Profile 2")
    options.add_argument(r"--command_executor='http://localhost:4444/wd/hub'")
    options.add_argument(r"--desired_capabilities=DesiredCapabilities.CHROME")
    driver = webdriver.Remote(options = options)
    URL1 = "https://www.browserstack.com"
    driver.get(url=URL1)
    driver.maximize_window()

    WDW(driver, 25).until(EC.visibility_of_element_located((By.XPATH, "//*[@title = 'Sign In']"))).click()
    WDW(driver, 25).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='user_email_login']")))
    time.sleep(1)
    actions = AC(driver)
    username_location = driver.find_element(By.XPATH, "//*[@id='user_email_login']")
    username_location.clear()
    username_text = os.environ.get("browserstacktempusername1")
    actions.move_to_element(username_location).click().send_keys(username_text).perform()
    password_location = driver.find_element(By.XPATH, "//*[@id='user_password']")
    password_location.clear()
    password_text = os.environ.get("browserstacktemppassword1")
    actions.move_to_element(password_location).click().send_keys(password_text).perform()
    driver.find_element(By.XPATH, "//*[@value='Sign me in']").click()
    WDW(driver, 25).until(EC.visibility_of_element_located((By.XPATH, "//*[div[contains(text(),'Live')]]"))).click()

    driver.get("https://live.browserstack.com/dashboard")
    WDW(driver, 25).until(EC.visibility_of_element_located((By.XPATH, "//*[div[contains(text(),'mac')]]"))).click()
    WDW(driver, 25).until(EC.visibility_of_element_located((By.XPATH, "//*[@aria-label='Big Sur']"))).click()
    WDW(driver, 25).until(EC.visibility_of_element_located((By.XPATH, "//*[@aria-label='chrome 112 ']"))).click()
    WDW(driver, 25).until(
        EC.visibility_of_element_located((By.XPATH, "//*[label[contains(text(),'Stop Session')]]"))).click()
    print("successfully logged into bstack live")
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Yaay! my sample test passed"}}')

    driver.quit()

def test_safari():
    options = selenium.webdriver.safari.options.Options()
    options.add_argument(r"--command_executor='http://localhost:4444/wd/hub'")
    options.add_argument(r"--desired_capabilities=DesiredCapabilities.SAFARI")
    driver = webdriver.Remote(options = options)
# driver = webdriver.Remote(
#     command_executor="http://localhost:4444/wd/hub",
#     desired_capabilities=DesiredCapabilities.CHROME,
# )
    URL = "https://browserstack.com"
    driver.get(url=URL)
    print(driver.page_source)
    print ("logging into Browserstack")
    driver.maximize_window()

    driver.find_element(By.LINK_TEXT,"Sign in").click()
    print("signed into browserstack")

    # driver.find_element(By.LINK_TEXT,"Live").click()
    # print("Sleeping now")
    time.sleep(20)
    driver.quit()


def test_firefox():
    options = selenium.webdriver.firefox.options.Options()
    # options.add_argument(r"--browser_profile='/Users/aravindhpg/Library/Application Support/Firefox/Profiles/gj9o1pz6.aravindhpg'")
    options.add_argument("-profile")
    options.add_argument("/Users/aravindhpg/Library/Application Support/Firefox/Profiles/gj9o1pz6.aravindhpg")

    # options.add_argument(r"--user-data-dir=/Users/aravindhpg/Library/Application Support/Firefox/Profiles/gj9o1pz6.aravindhpg")
    # options.add_argument(r"--profile-directory=/Users/aravindhpg/Library/Application Support/Firefox/Profiles/gj9o1pz6.aravindhpg")
    # options.add_argument(r"--FirefoxProfile=/Users/aravindhpg/Library/Application Support/Firefox/Profiles/gj9o1pz6.aravindhpg")
    options.add_argument(r"--command_executor='http://localhost:4444/wd/hub'")
    options.add_argument(r"--desired_capabilities=DesiredCapabilities.FIREFOX")
    driver = webdriver.Remote(options=options)

    # driver = webdriver.Remote(
    #     command_executor="http://localhost:4444/wd/hub",
    #     desired_capabilities=DesiredCapabilities.CHROME,
    # )

    URL = "https://browserstack.com"
    driver.get(url=URL)
    print(driver.page_source)
    print("logging into Browserstack")

    driver.find_element(By.LINK_TEXT, "Sign in").click()
    print("signed into browserstack")

    driver.find_element(By.LINK_TEXT, "Live").click()
    print("Sleeping now")
    time.sleep(20)
    driver.quit()

