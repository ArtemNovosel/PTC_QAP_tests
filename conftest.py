# файл с фикстурами
import time
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

BASE_URL = 'https://b2c.passport.rt.ru/'
EMAIL = 'a*'
PHONE = '902*'
LOGIN = 'rtkid_16*'
PASSWORD_EMAIL = 'I*'
PASSWORD_PHONE = 'I*'
PASSWORD_LOGIN = 'I*'


@pytest.fixture(scope='session')
def browser(request):
    # инициализируем драйвер
    driver = webdriver.Chrome(executable_path="./chromedriver")
    # выполняем тест
    yield driver
    # закрываем сессию
    driver.quit()
