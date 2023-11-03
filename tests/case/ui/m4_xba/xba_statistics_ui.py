import re
import time

import allure
from playwright.sync_api import expect, Page

from pages.UI._4_xBA.xba_statistics_page import XbaStatisticsPage


@allure.step("Открыть страницу 'Статистика xBA'")
def open_page_by_steps(browser: Page):
    page = XbaStatisticsPage(browser)

    with allure.step("Перейти в 'Настройки уведомлений'"):
        page.goto_page("/notification-center")
        browser.wait_for_url(page.host + "/notification-center")

    with allure.step("Клик в боковом меню 'xBA'"):
        page.SB_XBA.click()

    with allure.step("Клик в меню 'Статистика xBA'"):
        page.SB_XBA_STATISTICS.click()

    with allure.step("Открылась страница 'Статистика xBA'"):
        expect_reg = re.compile('^' + page.host + XbaStatisticsPage.page_path + '(\\?.*)?$')
        expect(browser).to_have_url(expect_reg)
