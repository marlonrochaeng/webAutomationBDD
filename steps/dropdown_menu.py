from behave import given, then, when

from pages.login_page import LoginPage


@when(u'I select the {item} from the menu')
def step_impl_select_item(context, item):
    login_page = LoginPage(context)
    login_page.dropdown_select_item(item)

@then(u'The selected {item} should be visible')
def step_impl_is_visible(context, item):
    login_page = LoginPage(context)
    login_page.is_text_visible(item) 
