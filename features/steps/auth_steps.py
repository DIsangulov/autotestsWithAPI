from behave import *

from pages.UI._0_Auth.auth_page import AuthPage
import logging

logging.getLogger('seleniumwire').setLevel(logging.WARNING)

host = "https://10.130.0.22"


@given('Открыли ссылку на тестовый стенд')
def step_impl(context):
    context.page = AuthPage(context.browser, host)
    context.page.open()


@then('Ввели логин и пароль')
def step_impl(context):
    context.page = AuthPage(context.browser, host)
    context.page.enter_as_user()


@when('Осуществлен переход на главную страницу')
def step_impl(context):
    context.page = AuthPage(context.browser, host)
    context.page.should_enter_be_successful()
