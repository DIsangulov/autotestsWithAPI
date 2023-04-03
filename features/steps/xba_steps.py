from behave import *
import logging

from pages.UI._4_xBA.xba_metaprofiles import Metaprofiles
from pages.UI._4_xBA.xba_profiles import Profiles
from pages.UI._4_xBA.xba_statistic import Statistic

logging.getLogger('seleniumwire').setLevel(logging.WARNING)

host = "https://10.130.0.22"


@then('Переход в xBA - Профили')
def step_impl(context):
    context.page = Profiles(context.browser, host)
    context.page.open_xba_profiles()


@when('Осуществлен переход в xBA - Профили')
def step_impl(context):
    context.page = Profiles(context.browser, host)
    context.page.should_enter_xba_profiles_be_successful()


@then('Переход в xBA - Метапрофили')
def step_impl(context):
    context.page = Metaprofiles(context.browser, host)
    context.page.open_xba_metaprofiles()


@when('Осуществлен переход в xBA - Метапрофили')
def step_impl(context):
    context.page = Metaprofiles(context.browser, host)
    context.page.should_enter_xba_metaprofiles_be_successful()


@then('Переход в xBA - Статистика xBA')
def step_impl(context):
    context.page = Metaprofiles(context.browser, host)
    context.page.open_xba_metaprofiles()


@when('Осуществлен переход в xBA - Статистика xBA')
def step_impl(context):
    context.page = Statistic(context.browser, host)
    context.page.should_enter_xba_statistic_be_successful()


@then('Сохранить изображение')
def step_impl(context):
    context.page = Statistic(context.browser, host)
    context.page.save_xba_diagram_image()


@when('Сравнить изображения')
def step_impl(context):
    context.page = Statistic(context.browser, host)
    context.page.compare_images()
