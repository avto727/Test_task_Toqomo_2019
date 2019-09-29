from .base_page import BasePage
from .locators import *
from selenium.webdriver.common.by import By
from time import sleep

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        print('Шаг 1 проверка на корректный url адрес')
        a_url = self.driver.current_url
        # print(a_url)
        assert 'https://app.jowi.online/auth/sign-in' == a_url, "Login link is wrong"

    def should_be_login_form(self):

        print('Шаг 2 проверка формы логина')
        title_text = self.driver.find_element(By.CSS_SELECTOR, loc('LOGIN_TITLE')).text
        assert "Авторизация" == title_text, "Title_text is wrong"
        forget_text = self.driver.find_element(By.CSS_SELECTOR, loc('BUTTON_FORGET')).text
        assert "Забыли пароль?" == forget_text, "Title_text is wrong"
        enter_text = self.driver.find_element(By.CSS_SELECTOR, loc('BUTTON_ENTER')).text
        assert "Войти" == enter_text, "Title_text is wrong"
        not_yet_text = self.driver.find_element(By.CSS_SELECTOR, loc('NOT_YET_TEXT')).text
        assert "Еще не зарегистрированы?" in not_yet_text, "not_yet_text is wrong"
        signup_text = self.driver.find_element(By.CSS_SELECTOR, loc('SIGNUP_LINK')).text
        assert "Зарегистрироваться в JShop" in signup_text, "signup_text is wrong"

    def input_data_user(self, user):
        phone = user.get('phone')
        pas = user.get('pass')
        print(phone, pas)
        super().input_css(loc('PHONE_SIGNIN'), phone)
        super().input_css(loc('PASS_SIGNIN'), pas)
        super().click_css(loc('BUTTON_ENTER'))
        sleep(1)

