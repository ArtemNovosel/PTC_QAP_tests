import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base_page import BasePage


# класс локаторов на странице авторизации
class RegisterPageLocators:
    # локаторы полей ввода
    LOCATOR_NAME = (By.XPATH, '//*[@name="firstName"]')
    LOCATOR_LASTNAME = (By.XPATH, '//*[@name = "lastName"]')
    LOCATOR_PHONE_EMAIL = (By.XPATH, '//*[@id="address"]')
    LOCATOR_PASSWORD = (By.XPATH, '//*[@id="password"]')
    LOCATOR_PASS_CONFIRM = (By.XPATH, '//*[@id="password-confirm"]')
    # локаторы кнопок
    LOCATOR_REGISTER = (By.XPATH, '//*[@name="register"]')
    # локатор всплывающих error сообщений
    LOCATOR_ERROR_MESSAGES = (By.XPATH, '//*[@class="rt-input-container__meta rt-input-container__meta--error"]')


class RegisterPageHelper(BasePage):
    # вводит текст в Имя
    def enter_name(self, username):
        search_field = self.find_element(RegisterPageLocators.LOCATOR_NAME)
        search_field.send_keys(Keys.CONTROL + "a")
        search_field.send_keys(Keys.DELETE)
        search_field.clear()
        search_field.send_keys(username)
        return search_field

    # вводит текст в Фамилия
    def enter_lastname(self, username):
        search_field = self.find_element(RegisterPageLocators.LOCATOR_LASTNAME)
        search_field.send_keys(Keys.CONTROL + "a")
        search_field.send_keys(Keys.DELETE)
        search_field.clear()
        search_field.send_keys(username)
        return search_field

    # вводит текст в email/телефон
    def enter_phone_email(self, username):
        search_field = self.find_element(RegisterPageLocators.LOCATOR_PHONE_EMAIL)
        search_field.send_keys(Keys.CONTROL + "a")
        search_field.send_keys(Keys.DELETE)
        search_field.clear()
        search_field.send_keys(username)
        return search_field

    # вводит текст в Пароль
    def enter_password(self, username):
        search_field = self.find_element(RegisterPageLocators.LOCATOR_PASSWORD)
        search_field.send_keys(Keys.CONTROL + "a")
        search_field.send_keys(Keys.DELETE)
        search_field.clear()
        search_field.send_keys(username)
        return search_field

    # вводит текст в Подтверждение пароля
    def enter_pass_confirm(self, username):
        search_field = self.find_element(RegisterPageLocators.LOCATOR_PASS_CONFIRM)
        search_field.send_keys(Keys.CONTROL + "a")
        search_field.send_keys(Keys.DELETE)
        search_field.send_keys(username)
        return search_field

    # нажимает кнопку Зарегистрироваться
    def click_register(self):
        return self.find_element(RegisterPageLocators.LOCATOR_REGISTER, time=5).click()

    # возвращает error сообщения
    def text_error_messages(self):
        return self.find_elements(RegisterPageLocators.LOCATOR_ERROR_MESSAGES, time=10)
