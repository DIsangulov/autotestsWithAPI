import time

import allure
from playwright.sync_api import expect

from pages.Helpers.base_case import BaseCase
from pages.UI._4_xBA.metaprofiles_page import XbaMetaprofilesListPage


class XbaMetaprofilesCase(BaseCase):

    @allure.step("Открыть страницу 'Метапрофили'")
    def open_page_by_steps(self):
        page = XbaMetaprofilesListPage(self._page)

        with allure.step("Перейти в 'Настройки уведомлений'"):
            page.goto_page("/notification-center")
            page.page.wait_for_url(page.host + "/notification-center")

        with allure.step("Клик в боковом меню 'xBA'"):
            page.SB_XBA.click()

        with allure.step("Клик в меню 'Метапрофили'"):
            page.SB_XBA_METAPROFILES.click()

        with allure.step("Открылась страница 'Метапрофили'"):
            page.page.wait_for_url(page.host + XbaMetaprofilesListPage.page_path)
