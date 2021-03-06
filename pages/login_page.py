from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, 'url is not correct'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_enter = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_enter.send_keys(email)
        password_enter1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password_enter1.send_keys(password)
        password_enter2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        password_enter2.send_keys(password)
        registration_submit = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        registration_submit.click()
