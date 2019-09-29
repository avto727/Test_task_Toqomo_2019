from datetime import datetime
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    def open(self):
        self.driver.get(self.url)

    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def click_css(self, css):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))
        self.driver.find_element(By.CSS_SELECTOR, css).click()

    def input_css(self, css, txt):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))
        self.driver.find_element(By.CSS_SELECTOR, css).send_keys(txt)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except ('NoSuchElementException'):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
