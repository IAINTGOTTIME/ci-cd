import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from conf import Links


class LoginPage(BasePage):

    def navigate(self):
        with allure.step(f"Open {Links.LOGIN_LINK} page"):
            self.browser.get(Links.LOGIN_LINK)

    @property
    @allure.step("find field username")
    def username_field(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, 'input[name="username"]')

    @username_field.setter
    @allure.step("input username")
    def username_field(self, value):
        self.username_field.send_keys(value)

    @property
    @allure.step("find field password")
    def password_field(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, 'input[name="password"]')

    @password_field.setter
    @allure.step("input password")
    def password_field(self, value):
        self.password_field.send_keys(value)

    @property
    @allure.step("click submit button")
    def submit_button(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

    @property
    @allure.step("find login error alert")
    def login_error_alert(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, 'div[class="oxd-alert-content oxd-alert-content--error"]')

    @property
    @allure.step("find empty field error message")
    def empty_field_error_message(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, 'span')
