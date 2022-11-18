"""Селлекторы"""
from selenium.webdriver.common.by import By


class BasePageLocators():
    """Селекторы для страницы"""
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LINK_TO_BASKET = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")


class LoginPageLocators():
    """Селекторы для страницы авторизации"""
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    """Селекторы для страницы продукта"""
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    ALERT_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")

class BacketPageLocators():
    """Селекторы для корзины"""
    BASKET_FORMSET = (By.ID, "basket_formset")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner a")  #Селектор ссылки "Продолжить покупки"
    # (появляется, если корзина пуста)
