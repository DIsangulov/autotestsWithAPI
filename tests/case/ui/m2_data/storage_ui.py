import time

import allure
from playwright.sync_api import expect

from pages.Helpers.base_case import BaseCase
from pages.UI._2_Data.storage_page import *


class DataStorageCase(BaseCase):

    @allure.step("Открыть страницу 'Хранилище'")
    def open_page_by_steps(self):
        page = StoragePage(self._page)

        with allure.step("Перейти в 'Профиль пользователя'"):
            page.goto_page("/personal")
            page.page.wait_for_url(page.host + "/personal")

        with allure.step("Клик в боковом меню 'Данные'"):
            page.SB_DATA.click()

        with allure.step("Клик в меню 'Хранилище'"):
            page.SD_DATA_STORAGE.click()

        with allure.step("Переход на страницу 'Хранилище'"):
            page.page.wait_for_url(page.host + StorageStructurePage.page_path)

    def storage_navigation_tabs(self):
        page = StoragePage(self._page)

        with allure.step("Открыть страницу 'Хранилища' (tab Струкрура)"):
            page.open()

        with allure.step("Клик по вкладке 'Статистика'"):
            page.TAB_STATISTICS.click()
        with allure.step("Открылась страница 'Хранилище > Статистика'"):
            page.page.wait_for_url(page.host + StorageStatisticPage.page_path)

        with allure.step("Клик по вкладке 'Поиск в хранилище'"):
            page.TAB_SEARCH.click()
        with allure.step("Открылась страница 'Хранилище > Поиск в хранилище(по содержимому)'"):
            page.page.wait_for_url(page.host + StorageSearchContentPage.page_path)
        with allure.step("Клик по вкладке 'Поиск в хранилище > По столбцам'"):
            page.TAB_SEARCH_COLUMN.click()
        with allure.step("Открылась страница 'Хранилище > Поиск в хранилище(по столбцам)'"):
            page.page.wait_for_url(page.host + StorageSearchColumnPage.page_path)

        with allure.step("Клик по кладке 'Поиск в хранилище > По содержимому'"):
            page.TAB_SEARCH_CONTENT.click()
        with allure.step("Открылась страница 'Хранилище > Поиск в хранилище(по содержимому)'"):
            page.page.wait_for_url(page.host + StorageSearchContentPage.page_path)

        with allure.step("Клик по кладке 'Хранилище > Правила импорта'"):
            page.TAB_RULES.click()
        with allure.step("Открылась страница 'Хранилище > Правила импорта'"):
            page.page.wait_for_url(page.host + StorageRulesPage.page_path)

        with allure.step("Клик по вкладке 'Хранилище > Структура'"):
            page.TAB_STRUCTURE.click()
        with allure.step("Открылась страница 'Хранилище > Структура'"):
            page.page.wait_for_url(page.host + StorageStructurePage.page_path)
