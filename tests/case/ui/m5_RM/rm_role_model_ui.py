import time

import allure
from playwright.sync_api import expect

from pages.Helpers.base_case import BaseCase
from pages.UI._5_RoleMining.rm_role_model_page import RMRoleModelPage


class RMRoleModelCase(BaseCase):

    @allure.step("Открыть страницу 'Ролевая модель'")
    def open_page_by_steps(self):
        page = RMRoleModelPage(self._page)

        # todo: остальные шаги
        ...
