import allure
from conf import Links


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def navigate(self):
        with allure.step(f"Open {Links.HOST} page"):
            self.browser.get(Links.HOST)
