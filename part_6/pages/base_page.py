"""Объект страницы"""
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from .locators import BasePageLocators


class BasePage():
    """Класс для работы с базовой страницей"""

    def __init__(self, browser, url, timeout=10):
        """Конструктор"""
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_basket(self):
        """Метод для перехода в корзину"""
        link = self.browser.find_element(*BasePageLocators.LINK_TO_BASKET)
        link.click()

    def go_to_login_page(self):
        """Метод для перехода на страницу авторизации"""
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def is_element_present(self, how, what):
        """Метод для проверки наличия элемента на странице"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_disappeared(self, how, what, timeout=4):
        """Метод для проверки исчезновения элемента со страницы"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_not_element_present(self, how, what, timeout=4):
        """Метод для проверки отсутствия элемента на странице"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def open(self):
        """Метод для открытия страницы"""
        self.browser.get(self.url)

    def should_be_login_link(self):
        """Метод для определения видимости ссылки на страницу авторизации"""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        """Метод для проверки, что пользователь авторизован"""
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def solve_quiz_and_get_code(self):
        """Метод для получения проверочного кода"""
        alert = self.browser.switch_to.alert
        x = alert.text.split()[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
