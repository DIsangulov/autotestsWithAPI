import re
import time

import allure
from playwright.sync_api import expect

from pages.Helpers.base_case import BaseCase
from pages.UI._5_RoleMining.rm_settings_page import RMSettingsPage


class RMSettingsCase(BaseCase):

    @allure.step("Открыть страницу 'Настройки Role mining'")
    def open_page_by_steps(self):
        page = RMSettingsPage(self._page)

        with allure.step("Перейти в 'Настройки уведомлений'"):
            page.goto_page("/notification-center")
            page.page.wait_for_url(page.host + "/notification-center")

        with allure.step("Клик в боковом меню 'Role mining'"):
            page.SB_ROLE_MINING.click()

        with allure.step("Клик в меню 'Настройки'"):
            page.SB_RM_SETTINGS.click()

        with allure.step("Открыта страница 'Настройки Role mining'"):
            expect_reg = re.compile('^' + page.host + RMSettingsPage.page_path + '(/.*)?$')
            expect(page.page).to_have_url(expect_reg)
