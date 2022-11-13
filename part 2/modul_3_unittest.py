"""Курс по селениуму, блок 3.2 step 13 unittest"""
import unittest
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestSelector(unittest.TestCase):
    def browser(self, url):
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service)
        browser.get(url)

        input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first_class .first')
        input1.send_keys("любой текст")
        input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .second_class .second')
        input1.send_keys("любой текст")
        input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .third_class .third')
        input2.send_keys("любой текст")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Unexeption selector")

    def test_url1(self):
        self.browser("http://suninjuly.github.io/registration1.html")

    def test_url2(self):
        self.browser("http://suninjuly.github.io/registration2.html")


if __name__ == "__main__":
    unittest.main()
