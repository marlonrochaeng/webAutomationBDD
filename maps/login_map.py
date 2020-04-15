from selenium.webdriver.common.by import By


class LoginMap:
    # locators
    login_field = "//input[@id='username']a"
    password_field = "//input[@id='password']"
    login_button = "//i[contains(text(),'Login')]"
    logout_button = "//i[@class='icon-2x icon-signout']"
    login_message = "//div[@id='flash']"
    select_login = "//a[@href='/login']"
    dropdown_link = "//a[@href='/dropdown']"
    dropdown_select = "//select[@id='dropdown']"
    alerts_link = "//a[@href='/javascript_alerts']"
    first_alert = "//button[contains(text(),'Click for JS Alert')]"
    second_alert = "//button[contains(text(),'Click for JS Confirm')]"
    download_select = "//a[@href='/download']"

    def file_to_download(self, text):
        return "//a[@href='download/"+text+"']"
