import time

import allure
from playwright.sync_api import expect

from pages.Helpers.base_case import BaseCase
from pages.UI._4_xBA.xba_profiles_page import XbaProfilesListPage


class XbaProfilesCase(BaseCase):

    @allure.step("Открыть страницу 'Профили xBA'")
    def open_page_by_steps(self):
        page = XbaProfilesListPage(self._page)

        with allure.step("Перейти в 'Настройки уведомлений'"):
            page.goto_page("/notification-center")
            page.page.wait_for_url(page.host + "/notification-center")

        with allure.step("Клик в боковом меню 'xBA'"):
            page.SB_XBA.click()

        with allure.step("Клик в меню 'Профили'"):
            page.SB_XBA_PROFILES.click()

        with allure.step("Открылась страница 'Профили xBA'"):
            page.page.wait_for_url(page.host + XbaProfilesListPage.page_path)
