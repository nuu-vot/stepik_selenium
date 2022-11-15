"""
Конфигурация
"""
import config
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def browser():
    """фикстура"""
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")  # открываем на полный экран
    # chrome_options.add_argument("--disable-infobars")  # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions")  # отключаем расширения
    # chrome_options.add_argument("--headless")  # режим "без браузера"

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)

    driver.get("https://stepik.org/")
    button = driver.find_element(By.CLASS_NAME, 'navbar__auth_login')
    button.click()

    driver.find_element(By.CSS_SELECTOR, '[name="login"]').send_keys(config.LOGIN)
    driver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(config.PASSWORD)
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    yield driver
    driver.quit()
    print(config.res_answer)
