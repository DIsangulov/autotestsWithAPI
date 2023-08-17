import re
import time

import allure
from playwright.sync_api import expect

from pages.Helpers.base_case import BaseCase
from pages.UI._3_Analytics.mailings_page import MailingsReportPage, MailingNewData


class MailingsCase(BaseCase):

    @allure.step("Открыть страницу 'Рассылки'")
    def open_page_by_steps(self):
        page = MailingsReportPage(self._page)

        with allure.step("Перейти в 'Профиль пользователя'"):
            page.goto_page("/personal")
            page.page.wait_for_url(page.host + "/personal")

        with allure.step("Клик в боковом меню 'Аналитика'"):
            page.SB_ANALYTICS.click()

        with allure.step("Клик в меню 'Рассылки'"):
            page.SB_ANALYTICS_MAILINGS.click()

        with allure.step("Открылась страница 'Рассылки'"):
            # ^host/page/path(\?.*)?$  <- reg для наличия или отсутствия query-параметров
            expect_reg = re.compile('^' + page.host + MailingsReportPage.page_path + "(\\?.*)?$")
            expect(page.page).to_have_url(expect_reg)

        with allure.step("Клик по вкладке 'Новых данных'"):
            page.TAB_NEW_DATA.click()
        with allure.step("Открылась страница 'Рассылки(новых данных)'"):
            expect_reg = re.compile('^' + page.host + MailingNewData.page_path + "(\\?.*)?$")
            expect(page.page).to_have_url(expect_reg)

        with allure.step("Клик по вкладке 'Отчетов'"):
            page.TAB_REPORTS.click()
        with allure.step("Открылась страница 'Рассылки(отчетов)'"):
            expect_reg = re.compile('^' + page.host + MailingsReportPage.page_path + "(\\?.*)?$")
            expect(page.page).to_have_url(expect_reg)
