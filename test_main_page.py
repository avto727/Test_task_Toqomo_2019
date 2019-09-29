from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_user_valid_login(driver):
    link = "https://app.jowi.online/auth/sign-in"
    page = MainPage(driver, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    # page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_page()


def est_guest_should_see_login_link(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, link)
    page.open()
    page.should_be_login_link()