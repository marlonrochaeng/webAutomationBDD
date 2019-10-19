from behave import given, when, then
from framework.webapp import WebBrowser

@given(u'I open the "{url}" url')
def step_impl_load_website(context, url):
    wb = WebBrowser(context)
    wb.go_to_page(url)