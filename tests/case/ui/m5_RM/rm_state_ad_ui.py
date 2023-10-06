import re
import time

import allure
from playwright.sync_api import expect, Page

from pages.UI._5_RoleMining.rm_ad_page import RMStateADPage, RMStateADStatisticsPage, RMStateADRecommendationsPage


@allure.step("Открыть страницу 'Состояние Active Directory'")
def open_page_by_steps(browser: Page):
    page = RMStateADPage(browser)

    with allure.step("Перейти в 'Настройки уведомлений'"):
        page.goto_page("/notification-center")
        page.page.wait_for_url(page.host + "/notification-center")

    with allure.step("Клик в боковом меню 'Role mining'"):
        page.SB_ROLE_MINING.click()

    with allure.step("Клик в меню 'Состояние AD'"):
        page.SB_RM_STATE_AD.click()

    with allure.step("Открыта страница 'Состояние Active Directory'"):
        expect_reg = re.compile('^' + page.host + RMStateADPage.page_path + '(/.*)?$')
        expect(page.page).to_have_url(expect_reg)


def rm_state_ad_navigation_tabs(browser: Page):
    page = RMStateADStatisticsPage(browser)

    with allure.step("Открыть страницу 'Состояние Active Directory' (Статистика)"):
        page.open()
        expect(page.page).to_have_url(page.host + RMStateADStatisticsPage.page_path)

    with allure.step("Клик по вкладке 'Рекомендации'"):
        page.TAB_RECOMMENDATIONS.click()

    with allure.step("Открыта страница 'Состояние Active Directory' (Рекомендации)"):
        expect(page.page).to_have_url(page.host + RMStateADRecommendationsPage.page_path)

    with allure.step("Клик по вкладке 'Статистика'"):
        page.TAB_STATISTICS.click()

    with allure.step("Открыть страницу 'Состояние Active Directory' (Статистика)"):
        expect(page.page).to_have_url(page.host + RMStateADStatisticsPage.page_path)
