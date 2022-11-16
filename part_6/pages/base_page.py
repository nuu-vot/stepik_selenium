"""Объект страницы"""
from selenium.common.exceptions import NoSuchElementException


class BasePage():
    """Класс для работы с базовой страницей"""

    def __init__(self, browser, url, timeout=10):
        """Конструктор"""
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """Метод для открытия страницы"""
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
