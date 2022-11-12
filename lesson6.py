"""Курс по селениуму, урок 6"""

from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/simple_form_find_task.html"
text = str(math.ceil(math.pow(math.pi, math.e)*10000))

def test_step4(browser):
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(30)


def test_step5(browser):
    browser.get("http://suninjuly.github.io/find_link_text")

    print(text)
    link2 = browser.find_element(By.LINK_TEXT, text)
    link2.click()
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(30)


def test_step7(browser):
    browser.get("http://suninjuly.github.io/huge_form.html")

    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(30)

# http://suninjuly.github.io/find_xpath_form
def test_step8(browser):
    browser.get("http://suninjuly.github.io/registration2.html")

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, '//button[contains(text(), "Submit")]')
    button.click()
    time.sleep(30)


def test_step10(browser):
    browser.get("http://suninjuly.github.io/registration2.html")
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
    input1.send_keys("любой текст")
    time.sleep(3)
    input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    input1.send_keys("любой текст")
    input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
    input2.send_keys("любой текст")
    time.sleep(5)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text