"""Курс по селениуму, блок 2"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
import math
import os
import pyperclip


def captcha(browser):
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = str(math.log(abs(12 * math.sin(int(x)))))
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

    alert = browser.switch_to.alert
    addToClipBoard = alert.text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)  # копируем ответ из аллерта в буфер обмена


def test_1_5(browser):
    """Задание: кликаем по checkboxes и radiobuttons (капча для роботов)"""
    browser.get("https://suninjuly.github.io/math.html")

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = str(math.log(abs(12*math.sin(int(x)))))
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, '[value="robots"]')
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()
    time.sleep(4)


def test_1_7(browser):
    """Задание: поиск сокровища с помощью get_attribute"""
    browser.get("http://suninjuly.github.io/get_attribute.html")

    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = str(math.log(abs(12 * math.sin(int(x)))))
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, '[value="robots"]')
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()
    time.sleep(4)


def test_2_3(browser):
    """Задание: работа с выпадающим списком"""
    browser.get("https://suninjuly.github.io/selects1.html")

    x_element = browser.find_element(By.ID, "num1")
    x = int(x_element.text)
    y_element = browser.find_element(By.ID, "num2")
    y = int(y_element.text)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(x + y))

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()
    time.sleep(4)


def test_2_6(browser):
    """Задание на execute_script"""
    browser.get("http://suninjuly.github.io/execute_script.html")

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = str(math.log(abs(12 * math.sin(int(x)))))
    input1 = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, '[value="robots"]')
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()
    time.sleep(4)


def test_2_8(browser):
    """Задание: загрузка файла"""
    browser.get("http://suninjuly.github.io/file_input.html")

    input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    input1.send_keys("name")
    input2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    input2.send_keys("lastname")
    input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input3.send_keys("email")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file = browser.find_element(By.ID, "file")
    file_path = os.path.join(current_dir, file_name)
    file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()
    time.sleep(4)


def test_3_4(browser):
    """Задание: принимаем alert"""
    browser.get("http://suninjuly.github.io/alert_accept.html")

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    captcha(browser)


def test_3_6(browser):
    """Задание: переход на новую вкладку"""
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

    browser.switch_to.window(browser.window_handles[1])
    captcha(browser)


def test_4_6(browser):
    """Задание: Про Exceptions"""
    browser.get("http://suninjuly.github.io/cats.html")

    browser.find_element(By.ID, "button")


def test_4_8(browser):
    """Задание: ждем нужный текст на странице"""
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.ID, 'book')
    button.click()

    captcha(browser)
