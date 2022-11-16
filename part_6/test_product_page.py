"""Курс по селениуму, модуль 4.3"""
from .pages.product_page import PageObject


def test_guest_can_add_product_to_basket(browser):
    """Проверка добавления товара в корзину"""
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = PageObject(browser, link)
    page.open()
    page.add_to_basket()
