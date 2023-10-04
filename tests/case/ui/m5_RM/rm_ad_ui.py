import time

import allure
from playwright.sync_api import expect

from pages.Helpers.base_case import BaseCase
from pages.UI._5_RoleMining.rm_ad_page import RMStateADPage


class RMStateADCase(BaseCase):

    @allure.step("Открыть страницу 'Состояние Active Directory'")
    def open_page_by_steps(self):
        page = RMStateADPage(self._page)

        # todo: остальные шаги
        ...
