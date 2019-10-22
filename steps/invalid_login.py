from behave import then

from pages.login_page import LoginPage


@then(u'I should not be logged in')
def step_impl_is_user_logged(context):
    login_page = LoginPage(context)
    assert not login_page.is_logged()
