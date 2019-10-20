from selenium.webdriver.common.by import By


class LoginMap:
    # locators
    login_field = "//input[@id='username']"
    password_field = "//input[@id='password']"
    login_button = "//i[contains(text(),'Login')]"
    logout_button = "//i[@class='icon-2x icon-signout']"
    login_message = "//div[@id='flash']"
    select_login = "//a[@href='/login']"
    dropdown_link = "//a[@href='/dropdown']"
    dropdown_select = "//select[@id='dropdown']"
