"""Курс по селениуму, модуль 4.3"""
import pytest

from .pages.product_page import PageObject

links = [str(i) for i in range(10) if i != 7] + \
        [pytest.param("7", marks=pytest.mark.xfail(reason="mistake on page"))]


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    """Проверка добавления товара в корзину"""
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = PageObject(browser, link)
    page.open()
    page.add_product_to_basket()
