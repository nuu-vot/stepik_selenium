"""Объект страницы авторизации"""
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверка url на странице авторизации"""
        current_url = self.browser.current_url
        assert "login" in current_url, 'В урле нет построки "login"'

    def should_be_login_form(self):
        """Проверка наличия формы логина"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Неожиданная форма логина"

    def should_be_register_form(self):
        """Проверка наличия формы регистрации"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Неожиданная форма регистрации"
