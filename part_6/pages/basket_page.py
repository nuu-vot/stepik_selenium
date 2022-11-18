"""Объект страницы корзины"""
from .base_page import BasePage
from .locators import BacketPageLocators


class BasketPage(BasePage):
    """Класс для работы со страницей корзины"""

    def should_not_be_goods_in_basket(self):
        """Проверка отсутствия товаров в корзине"""
        assert self.is_not_element_present(*BacketPageLocators.BASKET_FORMSET), \
            "В корзине есть товары, их быть не должно"

    def text_that_the_cart_is_empty(self):
        """Проверка наличия текста, что корзина пуста"""
        assert self.is_element_present(*BacketPageLocators.BASKET_EMPTY), "Нет сообщения, что корзина пуста"
