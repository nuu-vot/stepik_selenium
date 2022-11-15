"""Курс по селениуму, модуль 3 [3-6-4] Авторизация на сайте"""

import time
import math
import pytest
import config
from selenium.webdriver.common.by import By

lessons = ['236895', '236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905']
"""Пока не разобрался почему первый тест падает("""


@pytest.mark.parametrize('lesson', lessons)
def test_find_hidden_text(browser, lesson):
    """Задание: параметризация тестов"""
    link = f'https://stepik.org/lesson/{lesson}/step/1'
    browser.get(link)

    answer = math.log(int(time.time()))
    browser.find_element(By.TAG_NAME, 'textarea').send_keys(str(answer))
    browser.find_element(By.CLASS_NAME, 'submit-submission').click()
    check_text = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text

    if check_text != 'Correct!':
        config.res_answer += check_text
    assert 'Correct!' == check_text, f'Ожидалось "Correct!", получили "{check_text}"'
