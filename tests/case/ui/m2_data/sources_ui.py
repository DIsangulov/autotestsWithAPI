import time

import allure

from pages.Helpers.base_case import BaseCase
from pages.UI._2_Data.data_sources import SourcesPage


class DataSourcesCase(BaseCase):

    @allure.step("Открыть страницу Источники")
    def open_page_by_steps(self):
        page = SourcesPage(self._page)

        with allure.step("Перейти в 'Профиль пользователя'"):
            page.goto_page("/personal")
            page.page.wait_for_url(page.host + "/personal")

        with allure.step("Клик в боковом меню 'Данные'"):
            page.SB_DATA.click()

        with allure.step("Клик в меню 'Источники'"):
            page.SB_DATA_SOURCES.click()

        with allure.step("Переход на страницу 'Источники'"):
            page.page.wait_for_url(page.host + SourcesPage.page_path)
