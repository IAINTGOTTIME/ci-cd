import allure
import pytest

from conf import UserData
from urllib.parse import urlparse

from pages.login_page import LoginPage

"""
login page
positive:
    (valid login and pass) *
negative:
    (invalid login)
    (invalid pass)
    (empty login)
    (empty pass)
    (empty login and pass)
"""


@allure.feature("Login functionality")
class TestLoginPage:
    @allure.title("input valid login and password")
    @allure.severity("Critical")
    @pytest.mark.positive
    def test_login_page_valid_login_and_pass(self, browser):
        """
        (valid login and pass)
        """

        page = LoginPage(browser)
        page.navigate()

        page.username_field = UserData.LOGIN
        page.password_field = UserData.PASSWORD
        page.submit_button.click()

        assert urlparse(browser.current_url).path == "/web/index.php/dashboard/index"

    @allure.title("input invalid credentials")
    @allure.severity("Critical")
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password", [
        ("huesos", UserData.PASSWORD),
        (UserData.LOGIN, "huesos228"),
        ("azqxsw", "qsxfvqgb"),
    ])
    def test_login_page_invalid_credentials(self, username, password, browser):
        """
        (invalid login) or (invalid pass)
        """

        page = LoginPage(browser)
        page.navigate()

        page.username_field = username
        page.password_field = password
        page.submit_button.click()

        assert page.login_error_alert.is_displayed()
        assert page.login_error_alert.text == "Invalid credentials"

    @allure.title("input empty credentials")
    @allure.severity("Critical")
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password", [
        ("", "asdfgs"),
        ("asdasfa", ""),
        ("", ""),
        (" ", " ")
    ])
    def test_login_page_empty_credentials(self, username, password, browser):
        """
        (empty login)
        (empty pass)
        (empty login and pass)
        """

        page = LoginPage(browser)
        page.navigate()

        page.username_field = username
        page.password_field = password
        page.submit_button.click()

        assert page.empty_field_error_message.is_displayed()
