from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .data.users import user

def test_user_valid_login(driver):
    link = "https://app.jowi.online/auth/sign-in"
    page = MainPage(driver, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_page()
    login_page.input_data_user(user.get('valid'))
