"""Курс по селениуму, модуль 3 [3-6-10]"""

# import time
from selenium.webdriver.common.by import By


def test_add_to_basket(browser):
    """Задание: запуск автотестов для разных языков интерфейса"""
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")

    add_to_basket = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert len(add_to_basket) == 1, 'Неожиданное количество кнопок "Добавить в корзину"'
    # time.sleep(30) # для удобства проверки)
