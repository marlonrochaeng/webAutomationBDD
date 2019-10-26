from behave import given, then, when

from pages.login_page import LoginPage


@then(u'I select the "{download}" file to download')
def step_impl_is_visible(context, download):
    login_page = LoginPage(context)
    login_page.download_file(download)
