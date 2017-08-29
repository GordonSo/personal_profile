from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_browser(browser_name="Chrome"):

    # if browser_name == "Chrome":
    chrome_options = Options()
    chrome_options.add_argument('--disable-extensions --disable-extensions-file-access-check --disable-extensions-http-throttling')

    return webdriver.Chrome(
        executable_path='C:\\pyprojects\gordonso_test\gordonso\\resources\\drivers\\chromedriver.exe',
        chrome_options=chrome_options
    )
