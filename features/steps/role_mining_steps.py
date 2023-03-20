from behave import *

from pages.Helpers.base_page import BasePage
from pages.UI._0_Auth.auth_page import AuthPage
from pages.UI._5_RoleMining.rm_ad_status import AdStatus
from pages.UI._5_RoleMining.rm_groups_and_users import GroupsAndUsers
from pages.UI._5_RoleMining.rm_role_model import RoleModel
from pages.UI._5_RoleMining.rm_settings import Settings
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


@then('Переход в Roleminig - Настройки')
def step_impl(context):
    context.page = Settings(context.browser, host)
    context.page.open_rm_settings()


@when('Осуществлен переход в Rolemining - Настройки')
def step_impl(context):
    context.page = Settings(context.browser, host)
    context.page.should_enter_rm_settings_be_successful()


@then('Переход в Roleminig - Состояние AD')
def step_impl(context):
    page = AdStatus(context.browser, host)
    page.open_rm_ad_status()


@when('Осуществлен переход в Rolemining - Состояние AD')
def step_impl(context):
    page = AdStatus(context.browser, host)
    page.should_enter_rm_ad_status_be_successful()


@then('Переход в Roleminig - Группы и пользователи')
def step_impl(context):
    page = GroupsAndUsers(context.browser, host)
    page.open_rm_groups_and_users()


@when('Осуществлен переход в Rolemining - Группы и пользователи')
def step_impl(context):
    page = GroupsAndUsers(context.browser, host)
    page.should_enter_rm_roups_and_users_be_successful()


@then('Переход в Roleminig - Ролевая модель')
def step_impl(context):
    page = RoleModel(context.browser, host)
    page.open_rm_role_model()


@when('Осуществлен переход в Rolemining - Ролевая модель')
def step_impl(context):
    page = RoleModel(context.browser, host)
    page.should_enter_rm_role_model_successful()
