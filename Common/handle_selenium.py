import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BrowserDriver:
    def __init__(self, browser='chrome'):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'edge':
            self.driver = webdriver.Edge()
        else:
            raise ValueError(f"Invalid browser '{browser}' specified.")

    def navigate(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click(self, element):
        element.click()

    def enter_text(self, element, text):
        element.send_keys(text)

    def press_enter(self, element):
        element.send_keys(Keys.ENTER)

    def close(self):
        self.driver.quit()


# Example of using the BrowserDriver class
if __name__ == "__main__":
    driver = BrowserDriver(browser='chrome')
    driver.navigate('https://www.baidu.com')
    search_input = driver.find_element((By.ID,'kw'))
    search_su = driver.find_element((By.ID,'su'))
    driver.enter_text(search_input,"软件测试基础")
    driver.click(search_su)
    driver.close()
