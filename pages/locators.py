from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_TITLE = (By.CSS_SELECTOR, "div.h2-title.align-center")

class MainPageLocators():
    SIGNUP_LINK = (By.CSS_SELECTOR, "div.offset-top.align-center > a")

class LoginPageLocators():
    BUTTON_FORGET = (By.CSS_SELECTOR, "div.align-right.offset-bottom > button")
    BUTTON_ENTER = (By.CSS_SELECTOR, "#sign-in-login-submit")
    NOT_YET_TEXT = (By.CSS_SELECTOR, "div.offset-top.align-center > div > span")
    PHONE_SIGNIN = (By.CSS_SELECTOR, "div.form-group.error > input")
    PASS_SIGNIN = (By.CSS_SELECTOR, "form > div:nth-child(2) > input")

class ProductPageLocators():
    ADD_PROD_1 = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    TEXT_ADD_BASKET = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    TEXT_PROD = (By.CSS_SELECTOR, '.col-sm-6.product_main > h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    AMOUNT_BASKET = (By.CSS_SELECTOR, '.alert-info.fade.in > div > p:nth-child(1) > strong')