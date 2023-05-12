from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Text 'login' is not contained in the current url"
        
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
    
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_ADDR_INPUT).send_keys(email)
        time.sleep(1)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        confirm_password = self.browser.find_element(*LoginPageLocators.CNFRM_PSSWRD_INPUT).send_keys(password)
        time.sleep(1)        
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN).click()
        time.sleep(5)
        