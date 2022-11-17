"""Селлекторы"""
from selenium.webdriver.common.by import By


class BasePageLocators():
    """Селекторы для страницы"""
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


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
