"""
Конфигурация
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    """Обработчик опции выбора языка"""
    parser.addoption('--language', action='store', default="es",
                     help="Choose language: ru, en, es")


@pytest.fixture(scope="function")
def browser(request):
    """фикстура"""
    language = request.config.getoption("language")

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")  # открываем на полный экран
    # chrome_options.add_argument("--disable-infobars")  # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions")  # отключаем расширения
    # chrome_options.add_argument("--headless")  # режим "без браузера"
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': language})

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver
    driver.quit()
