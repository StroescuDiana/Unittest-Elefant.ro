import time

from selenium.webdriver import Keys

from page_objects.LoginPageObjects import LoginPageObjects
from pages.base_page import BasePage


class LoginPage(BasePage, LoginPageObjects):

    def check_if_redirected_to_login_page(self):
        return super().get_page_url()

    def login_with_invalid_credentials(self):
        super().input_text(super().email_field_locator, super().wrong_email_address)  #add wrong email address
        super().input_text(super().password_field_locator, super().wrong_password)  #add wrong password
        super().click(super().conectare_btn_locator)  #clicks "CONECTARE" button
        return super().get_text(super().error_alert_locator)  #returns the text error

    def invalid_email_login(self):
        super().input_text(super().email_field_locator, Keys.CONTROL + "a")  #Selects all text within the email field
        super().input_text(super().email_field_locator, Keys.BACKSPACE)  #Removes the entire text from email field
        super().input_text(super().email_field_locator, super().invalid_email_address)  #Adds the invalid email address in the email field

    def visibility_of_conectare_btn(self):
        return super().is_enabled(super().conectare_btn_locator)  #return a bool value for is_enabled() method