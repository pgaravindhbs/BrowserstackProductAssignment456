try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium import webdriver
    import selenium.webdriver.chrome.options
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
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
    URL = "https://browserstack.com"
    driver.get(url=URL)
    print(driver.page_source)
    print ("logging into Browserstack")
    driver.find_element(By.LINK_TEXT,"Sign in").click()
    print("signed into browserstack")
    driver.find_element(By.LINK_TEXT,"Live").click()
    print("Sleeping now")
    time.sleep(20)
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

