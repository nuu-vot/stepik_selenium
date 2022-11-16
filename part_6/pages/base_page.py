"""Объект страницы"""


class BasePage():
    """Класс для работы с базовой страницей"""

    def __init__(self, browser, url):
        """Конструктор"""
        self.browser = browser
        self.url = url

    def open(self):
        """Метод для открытия страницы"""
        self.browser.get(self.url)
