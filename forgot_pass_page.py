import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base_page import BasePage


# класс локаторов на странице Восстановление пароля
class ForgPassPageLocators:
    # локаторы полей ввода
    LOCATOR_USERNAME = (By.XPATH, '//*[@id="username"]')
    LOCATOR_CAPTCHA = (By.XPATH, '//*[@id = "captcha"]')
    # локаторы скопок
    LOCATOR_GO = (By.XPATH, '//*[@id="reset"]')
    LOCATOR_BACK = (By.XPATH, '//*[@id="reset-back"]')
    # локаторы переключения режимов авторизации
    LOCATOR_TABS_PHONE = (By.XPATH, '//*[@id="t-btn-tab-phone"]')
    LOCATOR_TABS_EMAIL = (By.XPATH, '//*[@id="t-btn-tab-mail"]')
    LOCATOR_TABS_LOGIN = (By.XPATH, '//*[@id="t-btn-tab-login"]')
    LOCATOR_TABS_LS = (By.XPATH, '//*[@id="t-btn-tab-ls"]')
    LOCATOR_TABS_MODE = (By.XPATH, '// input[ @ name = "tab_type"]')

    # локаторы изображений
    LOCATOR_IMG_CAPTCHA = (By.XPATH, '//img[@class="rt-captcha__image"]')
    LOCATOR_IMG_LOGO = (By.XPATH, '//*[@class="rt-logo main-header__logo"]')
    LOCATOR_IMG_FOOTER_LINK = (By.XPATH, '//*[@id="rt-footer-agreement-link"]')
    # локатор всплывающих error сообщения Неверный логин или текст с картинки
    LOCATOR_ERROR_MESSAGES = (By.XPATH, '//*[@id="form-error-message"]')


# класс действий
class ForgPassPageHelper(BasePage):
    # вводит текст в юзернейм
    def enter_username(self, username):
        search_field = self.find_element(ForgPassPageLocators.LOCATOR_USERNAME)
        search_field.send_keys(Keys.CONTROL + "a")
        search_field.send_keys(Keys.DELETE)
        search_field.clear()
        search_field.send_keys(username)
        return search_field

    # вводит текст в поле капча
    def enter_captcha(self, username):
        search_field = self.find_element(ForgPassPageLocators.LOCATOR_CAPTCHA)
        search_field.send_keys(Keys.CONTROL + "a")
        search_field.send_keys(Keys.DELETE)
        search_field.clear()
        search_field.send_keys(username)
        return search_field

    # нажимает кнопку Продолжить
    def click_enter(self):
        return self.find_element(ForgPassPageLocators.LOCATOR_GO, time=5).click()

    # нажимает кнопку Вернуться назад
    def click_back(self):
        return self.find_element(ForgPassPageLocators.LOCATOR_BACK, time=5).click()

    # нажимает кнопку Почта
    def click_email(self):
        return self.find_element(ForgPassPageLocators.LOCATOR_TABS_EMAIL, time=5).click()

    # нажимает кнопку Логин
    def click_login(self):
        return self.find_element(ForgPassPageLocators.LOCATOR_TABS_LOGIN, time=5).click()

    # нажимает кнопку Лицевой счет
    def click_ls(self):
        return self.find_element(ForgPassPageLocators.LOCATOR_TABS_LS, time=5).click()

    # нажимает кнопку Телефон
    def click_phone(self):
        return self.find_element(ForgPassPageLocators.LOCATOR_TABS_PHONE, time=5).click()

    # возвращает error сообщения
    def text_error_messages(self):
        return self.find_element(ForgPassPageLocators.LOCATOR_ERROR_MESSAGES, time=10)
