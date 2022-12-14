"""Объект страницы авторизации"""
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """Класс для работы со страницей авторизации"""
    def should_be_login_page(self):
        """Проверка страницы на наличие подстроки 'login' в url, форм логина и регистрации"""
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

    def register_new_user(self, email, password):
        """Регистрация нового пользователя"""
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT).click()
