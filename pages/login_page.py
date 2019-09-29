from .base_page import BasePage
from .locators import *

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
        title_text = self.driver.find_element(*BasePageLocators.LOGIN_TITLE).text
        assert "Авторизация" == title_text, "Title_text is wrong"
        forget_text = self.driver.find_element(*LoginPageLocators.BUTTON_FORGET).text
        assert "Забыли пароль?" == forget_text, "Title_text is wrong"
        enter_text = self.driver.find_element(*LoginPageLocators.BUTTON_ENTER).text
        assert "Войти" == enter_text, "Title_text is wrong"
        not_yet_text = self.driver.find_element(*LoginPageLocators.NOT_YET_TEXT).text
        assert "Еще не зарегистрированы?" in not_yet_text, "not_yet_text is wrong"
        signup_text = self.driver.find_element(*MainPageLocators.SIGNUP_LINK).text
        assert "Зарегистрироваться в JShop" in signup_text, "signup_text is wrong"

    def input_data_user(self, user):
        phone = user.get('phone')
        pas = user.get('pass')
        print(phone, pas)
        super().input_phone(phone)
        # super().input_css(*LoginPageLocators.PASS_SIGNIN, pas)
        # super().input_css(*LoginPageLocators.PHONE_SIGNIN, phone)
