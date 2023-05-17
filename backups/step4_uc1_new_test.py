import pytest
try:
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


@pytest.mark.parametrize('browser',[
    # each element of this list will provide values for the
    # topics "value_A" and "value_B" of the test and will
    # generate a stand-alone test case.
    ('chrome')
    ,('firefox')
    ,('safari')
])
def test_browsers(browser,capsys):
    desired_caps = {'browserName': browser}
    if browser == "chrome":
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',desired_capabilities=desired_caps)

    elif browser == "firefox":
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',desired_capabilities=desired_caps)
        print("This ", browser, " has been initiated")
    elif browser == "safari":
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',desired_capabilities=desired_caps)
        print("This ", browser, " has been initiated")
    else:
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                  desired_capabilities=DesiredCapabilities.CHROME)

    # driver = webdriver.Remote(
#     command_executor="http://localhost:4444/wd/hub",
#     desired_capabilities=DesiredCapabilities.CHROME,
# )
    with capsys.disabled():
        print("This ", browser, " has been initiated")
    URL = "https://browserstack.com"
    driver.get(url=URL)
    print(driver.page_source)
    print ("logging into Browserstack")
    driver.maximize_window()

    driver.find_element(By.LINK_TEXT,"Sign in").click()
    print("signed into browserstack")

    # driver.find_element(By.LINK_TEXT,"Live").click()
    # print("Sleeping now")
    time.sleep(2)
    with capsys.disabled():
        print("This ", browser, " has been quit")
    driver.quit()


