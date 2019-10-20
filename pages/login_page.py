from werkzeug.security import safe_str_cmp

from framework.webapp import WebBrowser
from maps.login_map import LoginMap
import time


class LoginPage(WebBrowser):

    def __init__(self, context):
        super().__init__(context)
        self.login_map = LoginMap()

    def login(self, username, password):
        self.send_keys(self.login_map.login_field, username)
        self.send_keys(self.login_map.password_field, password)
        self.TakeScreenshot('Login')
        self.click_on(self.login_map.login_button)

    def select_from_menu(self, menu_option):
        if safe_str_cmp(menu_option, "Login"):
            self.click_on(self.login_map.select_login)
        elif safe_str_cmp(menu_option, "Dropdown"):
            self.click_on(self.login_map.dropdown_link)
            

    def is_logged(self):
        message = self.wait_element(self.login_map.login_message, timeout=50)
        self.TakeScreenshot('Check if is logged')
        return "You logged into a secure area!" in message.text
    
    def dropdown_select_item(self, item):
        self.send_keys(self.login_map.dropdown_select, item)
    
    def is_text_visible(self, item):
        assert item in self.get_element(self.login_map.dropdown_select).text

