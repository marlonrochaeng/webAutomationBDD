from behave import given, when, then
from pages.login_page import LoginPage

@when(u'I go to "{page}" page')
def step_impl_goto_page(context, page):
    login_page = LoginPage(context)
    login_page.select_from_menu(page)
    import time
    time.sleep(2)

@when(u'I do the valid login with credentials "{username}" and "{password}"')
def step_impl_valid_login(context, username, password):
    login_page = LoginPage(context)
    login_page.login(username, password)

@then(u'I should be logged in')
def step_impl_is_user_logged(context):
    login_page = LoginPage(context)
    assert login_page.is_logged()