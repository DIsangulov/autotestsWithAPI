import time

from behave import *

from pages.UI._5_RoleMining.rm_ad_status import AdStatus
from pages.UI._5_RoleMining.rm_groups_and_users import GroupsAndUsers
from pages.UI._5_RoleMining.rm_role_model import RoleModel
from pages.UI._5_RoleMining.rm_settings import Settings
import logging

logging.getLogger('seleniumwire').setLevel(logging.WARNING)

host = "https://10.130.0.22"


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


@then('Нажать кнопку Очистить')
def step_impl(context):
    page = Settings(context.browser, host)
    page.clear_sources_rm_settings()


@then('Отменить очистку')
def step_impl(context):
    page = Settings(context.browser, host)
    page.not_confirm_cleaning_rm_settings()


@then('Подтвердить очистку')
def step_impl(context):
    page = Settings(context.browser, host)
    page.confirm_cleaning_rm_settings()


@then('Выбрать источники данных Active Directory')
def step_impl(context):
    page = Settings(context.browser, host)
    page.selecting_values_from_dropdown_list()


@when('Источники сохранены')
def step_impl(context):
    page = Settings(context.browser, host)
    page.should_sources_saved()


@when('Перерасчет выполнен')
def step_impl(context):
    page = Settings(context.browser, host)
    page.should_sources_recalculated()


@then('Переход в подраздел Настройки расчета')
def step_impl(context):
    page = Settings(context.browser, host)
    page.calculation_settings()


@then('Нажать на шестеренку Настройка')
def step_impl(context):
    page = Settings(context.browser, host)
    page.configuring_anomaly_distribution()


@then('Ввести адрес и порт сервера')
def step_impl(context):
    page = Settings(context.browser, host)
    page.input_server_address_and_port()


@then('Выбрать протокол обмена TCP')
def step_impl(context):
    page = Settings(context.browser, host)
    page.select_tcp_exchange_protocol()


@then('Выбрать протокол обмена UDP')
def step_impl(context):
    page = Settings(context.browser, host)
    page.select_udp_exchange_protocol()


@then('Нажать на кнопку Добавить')
def step_impl(context):
    page = Settings(context.browser, host)
    page.click_add_button()


@when('Проверить успешность сохранения рассылки по протоколу TCP')
def step_impl(context):
    page = Settings(context.browser, host)
    page.should_tcp_distribution_protocol_save_sucsess()


@when('Проверить успешность сохранения рассылки по протоколу UDP')
def step_impl(context):
    page = Settings(context.browser, host)
    page.should_udp_distribution_protocol_save_sucsess()


@then('Выбрать чек-бокс Email и добавить адрес')
def step_impl(context):
    page = Settings(context.browser, host)
    page.enter_email()


@when('Проверить успешность сохранения рассылки по Email')
def step_impl(context):
    page = Settings(context.browser, host)
    page.should_email_save_sucsess()


@then('Удалить рассылку')
def step_impl(context):
    page = Settings(context.browser, host)
    page.delete_last_entry()


@when('Проверка удаления рассылки')
def step_impl(context):
    page = Settings(context.browser, host)
    page.should_last_entry_deleted()
