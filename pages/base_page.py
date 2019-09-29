from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException # в начале файла
from .locators import *
import math

class BasePage():
	# def __init__(self, driver, url):
	# 	self.driver = driver
	# 	self.url = url
		
		
	def open(self):
		self.driver.get(self.url)

	def __init__(self, driver, url, timeout=10):
		self.driver = driver
		self.url = url
		self.driver.implicitly_wait(timeout)

	def click_el(self):
		print()

	def input_phone(self, txt):
		WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(*LoginPageLocators.PHONE_SIGNIN))
		self.driver.find_element_by(*LoginPageLocators.PHONE_SIGNIN).send_keys(txt)

	def is_element_present(self, how, what):
		try:
			self.driver.find_element(how, what)
		except ('NoSuchElementException'):
			return False
		return True

	def is_not_element_present(self, how, what, timeout=14):
		try:
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return True

		return False


	def should_be_login_link(self):
		assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

	def go_to_product_page(self):
		self.driver.find_element(*BasePageLocators.PRODUCT_LINK).click()