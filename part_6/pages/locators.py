"""Селлекторы"""
from selenium.webdriver.common.by import By


class MainPageLocators():
    """Селекторы для главной страницы"""
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    """Селекторы для страницы авторизации"""
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
