import re
import time

import allure
from playwright.sync_api import expect, Page

from pages.UI._5_RoleMining.rm_settings_page import RMSettingsPage, RMSettingsSourcePage, RMSettingsCalcPage


@allure.step("Открыть страницу 'Настройки Role mining'")
def open_page_by_steps(browser: Page):
    page = RMSettingsPage(browser)

    with allure.step("Перейти в 'Настройки уведомлений'"):
        page.goto_page("/notification-center")
        page.page.wait_for_url(page.host + "/notification-center")

    with allure.step("Клик в боковом меню 'Role mining'"):
        page.SB_ROLE_MINING.click()

    with allure.step("Клик в меню 'Настройки'"):
        page.SB_RM_SETTINGS.click()

    with allure.step("Открыта страница 'Настройки Role mining'"):
        expect_reg = re.compile('^' + page.host + RMSettingsPage.page_path + '(/.*)?$')
        expect(browser).to_have_url(expect_reg)


def rm_settings_navigation_tabs(browser: Page):
    page = RMSettingsSourcePage(browser)

    with allure.step("Открыть страницу 'Настройки Role mining' (Источники)"):
        page.open()
        expect(page.page).to_have_url(page.host + RMSettingsSourcePage.page_path)

    with allure.step("Клик по вкладке 'Настройка расчета'"):
        page.TAB_CALC_SETTINGS.click()

    with allure.step("Открыта страница 'Настройки Role mining' (Настройка расчета)"):
        expect(page.page).to_have_url(page.host + RMSettingsCalcPage.page_path)

    with allure.step("Клик по вкладке 'Источники'"):
        page.TAB_SOURCES.click()

    with allure.step("Открыта страница 'Настройки Role mining' (Источники)"):
        expect(browser).to_have_url(page.host + RMSettingsSourcePage.page_path)
