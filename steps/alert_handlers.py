from behave import given, then, when

from pages.login_page import LoginPage


@when(u'I click on the first alert')
def step_impl(context):
    login_page = LoginPage(context)
    login_page.click_on_first_alert()


@when(u'I accept the alert')
def step_impl(context):
    login_page = LoginPage(context)
    login_page.alert_handler()


@then(u'Should be possible to click on the second alert')
def step_impl(context):
    login_page = LoginPage(context)
    login_page.click_on_second_alert()


@then(u'I accept the alert')
def step_impl(context):
    login_page = LoginPage(context)
    login_page.alert_handler()
