"""
Конфигурация
"""
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def browser():
    """
    фикстура
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")  # открываем на полный экран
    # chrome_options.add_argument("--disable-infobars")  # отключаем инфо сообщения
    # chrome_options.add_argument("--disable-extensions")  # отключаем расширения
    # chrome_options.add_argument("--headless")  # режим "без браузера"

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()
