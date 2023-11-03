import time

import allure
from playwright.sync_api import expect, Page

from pages.UI._4_xBA.xba_profiles_page import XbaProfilesListPage


@allure.step("Открыть страницу 'Профили xBA'")
def open_page_by_steps(browser: Page):
    page = XbaProfilesListPage(browser)

    with allure.step("Перейти в 'Настройки уведомлений'"):
        page.goto_page("/notification-center")
        browser.wait_for_url(page.host + "/notification-center")

    with allure.step("Клик в боковом меню 'xBA'"):
        page.SB_XBA.click()

    with allure.step("Клик в меню 'Профили'"):
        page.SB_XBA_PROFILES.click()

    with allure.step("Открылась страница 'Профили xBA'"):
        browser.wait_for_url(page.host + XbaProfilesListPage.page_path)
