import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base_page import BasePage


# класс локаторов на странице авторизации
class AuthPageLocators:
    # локаторы полей ввода
    LOCATOR_USERNAME = (By.XPATH, '//*[@id="username"]')
    LOCATOR_PASSWORD = (By.XPATH, '//*[@id="password"]')
    # локаторы кнопок
    LOCATOR_ENTER = (By.XPATH, '//*[@id="kc-login"]')
    LOCATOR_FORGOT_PASSWORD = (By.XPATH, '//*[@id="forgot_password"]')
    LOCATOR_REGISTER = (By.XPATH, '//*[@id="kc-register"]')
    LOCATOR_VK = (By.XPATH, '//*[@id="oidc_vk"]')
    LOCATOR_OK = (By.XPATH, '//*[@id="oidc_ok"]')
    LOCATOR_MAIL = (By.XPATH, '//*[@id="oidc_mail"]')
    LOCATOR_GOOGLE = (By.XPATH, '//*[@id="oidc_google"]')
    LOCATOR_YANDEX = (By.XPATH, '//*[@id="oidc_ya"]')
    # локаторы переключения режимов авторизации
    LOCATOR_TABS_PHONE = (By.XPATH, '//*[@id="t-btn-tab-phone"]')
    LOCATOR_TABS_EMAIL = (By.XPATH, '//*[@id="t-btn-tab-mail"]')
    LOCATOR_TABS_LOGIN = (By.XPATH, '//*[@id="t-btn-tab-login"]')
    LOCATOR_TABS_LS = (By.XPATH, '//*[@id="t-btn-tab-ls"]')
    LOCATOR_TABS_MODE = (By.XPATH, '// span[@class="rt-input__placeholder"]')
    # локаторы чекбоксов
    LOCATOR_REMEMMBER_ME = (
    By.XPATH, '//*[@class="rt-checkbox__shape rt-checkbox__shape--circular rt-checkbox__shape--orange"]')
    # локаторы инфо сообщений
    LOCATOR_ERROR_USERNAME = (By.XPATH, '//*[@class="rt-input-container__meta rt-input-container__meta--error"]')
    LOCATOR_ERROR_MESSAGE = (By.XPATH, '//*[@id="form-error-message"]')
    LOCATOR_AGE18 = (By.XPATH, '//*[@id="app-footer"]')
    # локаторы изображений
    LOCATOR_IMG_CAPTCHA = (By.XPATH, '//img[@class="rt-captcha__image"]')


# класс действий
class AuthPageHelper(BasePage):
    # вводит текст в юзернейм
    def enter_username(self, username):
        search_field = self.find_element(AuthPageLocators.LOCATOR_USERNAME)
        search_field.send_keys(Keys.CONTROL + "a")
        search_field.send_keys(Keys.DELETE)
        search_field.clear()
        search_field.send_keys(username)
        return search_field

    # вводит текст в поле пароля
    def enter_password(self, password):
        search_field = self.find_element(AuthPageLocators.LOCATOR_PASSWORD)
        search_field.send_keys(Keys.CONTROL + "a")
        search_field.send_keys(Keys.DELETE)
        search_field.clear()
        search_field.send_keys(password)
        return search_field

    # нажимает кнопку войти
    def click_enter(self):
        return self.find_element(AuthPageLocators.LOCATOR_ENTER, time=5).click()

    # нажимает кнопку Зарегистрироваться
    def click_register(self):
        return self.find_element(AuthPageLocators.LOCATOR_REGISTER, time=5).click()

    # нажимает кнопку
    def click_forgot_pass(self):
        return self.find_element(AuthPageLocators.LOCATOR_FORGOT_PASSWORD, time=5).click()

    # нажимает кнопку VK
    def click_VK(self):
        return self.find_element(AuthPageLocators.LOCATOR_VK, time=10).click()

    # нажимает кнопку Одноклассники
    def click_Ok(self):
        return self.find_element(AuthPageLocators.LOCATOR_OK, time=10).click()

    # нажимает кнопку Google
    def click_Google(self):
        return self.find_element(AuthPageLocators.LOCATOR_GOOGLE, time=10).click()

    # нажимает кнопку Mail
    def click_Mail(self):
        return self.find_element(AuthPageLocators.LOCATOR_MAIL, time=10).click()

    # нажимает кнопку яндекс
    def click_Ya(self):
        return self.find_element(AuthPageLocators.LOCATOR_YANDEX, time=10).click()

    # возвращает информацию в футере
    def text_footer_logo(self):
        return self.find_element(AuthPageLocators.LOCATOR_AGE18, time=10)

    # нажимает кнопку Почта
    def click_tab_email(self):
        return self.find_element(AuthPageLocators.LOCATOR_TABS_EMAIL, time=5).click()

    # нажимает кнопку Логин
    def click_tab_login(self):
        return self.find_element(AuthPageLocators.LOCATOR_TABS_LOGIN, time=5).click()

    # нажимает кнопку Лицевой счет
    def click_tab_ls(self):
        return self.find_element(AuthPageLocators.LOCATOR_TABS_LS, time=5).click()

    # нажимает кнопку Телефон
    def click_tab_phone(self):
        return self.find_element(AuthPageLocators.LOCATOR_TABS_PHONE, time=5).click()

    # возвращает текст поля username
    def text_username(self):
        return self.find_element(AuthPageLocators.LOCATOR_TABS_MODE, time=10)

    # возвращает ищет картинку капчи
    def img_captcha(self):
        return self.find_element(AuthPageLocators.LOCATOR_IMG_CAPTCHA, time=10)
