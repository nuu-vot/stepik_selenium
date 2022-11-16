"""Объект страницы продукта"""
from .base_page import BasePage
from .locators import ProductPageLocators


class PageObject(BasePage):
    """Класс для работы со страницей товара"""

    def add_to_basket(self):
        """Проверка добавления товара в корзину"""
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        self.solve_quiz_and_get_code()
        self.check_product_name()
        self.check_price()

    def check_product_name(self):
        """Проверка названия добавленного товара"""
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        alert_product_name = self.browser.find_elements(*ProductPageLocators.ALERT_PRODUCT_NAME)[0].text
        assert product_name == alert_product_name, \
            f'Неожиданное название товара в корзине "{alert_product_name}", вместо "{product_name}"'

    def check_price(self):
        """Проверка стоимости добавленного товара"""
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        alert_price = self.browser.find_element(*ProductPageLocators.ALERT_PRICE).text
        assert price == alert_price, \
            f'Неожиданная стоимость товара в корзине "{alert_price}", вместо "{price}"'
