# файл с фикстурами
import time
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

BASE_URL = 'https://b2c.passport.rt.ru/'
EMAIL = 'arteimn@mail.ru'
PHONE = '9024099791'
LOGIN = 'rtkid_1679990188472'
PASSWORD_EMAIL = 'Intqap1032'
PASSWORD_PHONE = 'INTqap1032'
PASSWORD_LOGIN = 'INTqap1032'


@pytest.fixture(scope='session')
def browser(request):
    # инициализируем драйвер
    driver = webdriver.Chrome(executable_path="./chromedriver")
    # выполняем тест
    yield driver
    # закрываем сессию
    driver.quit()
