import re
import time

import allure
from playwright.sync_api import expect, Page

from pages.UI._4_xBA.metaprofiles_page import XbaMetaprofilesListPage


@allure.step("Открыть страницу 'Метапрофили'")
def open_page_by_steps(browser: Page):
    page = XbaMetaprofilesListPage(browser)

    with allure.step("Перейти в 'Настройки уведомлений'"):
        page.goto_page("/notification-center")
        browser.wait_for_url(page.host + "/notification-center")

    with allure.step("Клик в боковом меню 'xBA'"):
        page.SB_XBA.click()

    with allure.step("Клик в меню 'Метапрофили'"):
        page.SB_XBA_METAPROFILES.click()

    with allure.step("Открылась страница 'Метапрофили'"):
        expect_reg = re.compile('^' + page.host + XbaMetaprofilesListPage.page_path + '(\\?.*)?$')
        expect(browser).to_have_url(expect_reg)
