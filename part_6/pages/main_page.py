"""Объект главной страницы"""

from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    """Класс для работы с главной страницей"""

    def go_to_login_page(self):
        """Проверка ссылки на страницу логина"""
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
