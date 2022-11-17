"""Курс по селениуму, модуль 4.3"""
import pytest

from .pages.product_page import ProductPage

links = [str(i) for i in range(10) if i != 7] + \
        [pytest.param("7", marks=pytest.mark.xfail(reason="mistake on page"))]


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    """Проверка добавления товара в корзину"""
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()


@pytest.mark.xfail(reason="все правильно, сообщение должно отображаться")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Сообщение об успешном добавлении товара в корзину не отображается"""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    """Сообщение об успешном добавлении товара в корзину отображается"""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="все правильно, сообщение не должно пропадать")
def test_message_disappeared_after_adding_product_to_basket(browser):
    """Сообщение исчезает после добавления товара в корзину"""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    """Проверка видимости ссылки на страницу авторизации"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    """Проверка перехода на страницу авторизации"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
