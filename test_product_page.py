from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import pytest


# @pytest.mark.parametrize('number', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
# def test_guest_can_add_product_to_basket(driver, number):
"""
def test_guest_can_add_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    # link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer{number}"
    page = MainPage(driver, link)
    page.open()
    # page.go_to_product_page()  # выполняем метод страницы - переходим на страницу товара
    product_page = ProductPage(driver, driver.current_url)
    product_page.should_be_product_url()   #  "Шаг 1"
    product_text = product_page.should_be_product_text()   #  "Шаг 2"
    # product_page.should_not_be_success_message()   #  "Шаг 4"
    product_page.add_product_basket()   #  "Шаг 3"
    product_page.test_message_disappeared_after_adding()   #  "Шаг 4"
    # product_page.should_not_be_success_message()   #  "Шаг 4"
    product_page.solve_quiz_and_get_code()   #  "Шаг 5"
    basket_text = product_page.should_be_add_to_basket()   #  "Шаг 6"
    product_page.should_be_amount_basket()   #  "Шаг 7"
    product_page.should_be_equality_text(product_text, basket_text)   #  "Шаг 8"
"""
def test_guest_should_see_login_link_on_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link()
