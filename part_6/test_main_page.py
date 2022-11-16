"""Курс по селениуму, модуль 4"""

from selenium.webdriver.common.by import By


def test_guest_can_go_to_login_page(browser):
    """Проверка ссылки на страницу логина"""
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
