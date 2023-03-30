
from selenium.webdriver.common.by import By

from base_page import BasePage

# класс локаторов на странице авторизованного пользователя
class UserPageLocators:
    LOCATOR_EXIT = (By.XPATH, '//*[@id="logout-btn"]')

class UserPagesHelper(BasePage):
    # нажимает кнопку ВЫЙТИ
    def click_exit(self):
        return self.find_element(UserPageLocators.LOCATOR_EXIT, time=5).click()