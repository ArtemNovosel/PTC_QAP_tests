from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import BASE_URL


class BasePage:
    # принимаем драйвер
    def __init__(self, driver):
        # в переменной класса будет использоваться драйвер
        self.driver = driver
        # указываем стартовую страницу
        self.base_url = BASE_URL

    # описываем переход на сайт
    def go_to_site(self):
        return self.driver.get(self.base_url)

    # поиск элента с выводом сообщения если его не нашли
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Не найден {locator}')

    # поиск элементОВ на странице
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Не найдены {locator}')
