"""
Конфигурация
"""
import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.service import Service


@pytest.fixture(scope="session")
def browser():
    """фикстура"""
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    # driver.implicitly_wait(10)

    yield driver
    driver.quit()
