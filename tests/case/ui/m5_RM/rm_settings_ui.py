import time

import allure
from playwright.sync_api import expect

from pages.Helpers.base_case import BaseCase
from pages.UI._5_RoleMining.rm_settings_page import RMSettingsPage


class RMSettingsCase(BaseCase):

    @allure.step("Открыть страницу 'Настройки Role mining'")
    def open_page_by_steps(self):
        page = RMSettingsPage(self._page)

        # todo: остальные шаги
        ...
