"""Объект главной страницы"""

from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    """Класс для работы с главной страницей"""

    def go_to_login_page(self):
        """Проверка перехода на страницу логина"""
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        """Проверка наличия ссылки на страницу логина"""
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"
