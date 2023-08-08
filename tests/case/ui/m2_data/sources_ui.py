import time

import allure
from playwright.sync_api import expect

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

    def open_modal_w_actions_details(self):
        page = SourcesPage(self._page)

        with allure.step("Открыть страницу 'Источники Данных'"):
            page.open()

        # Должен быть хотя бы один источник данных
        with allure.step("Количество источников в таблице > 0"):
            expect(page.ACTION_DETAILS).not_to_have_count(0)

        with allure.step("Нажать на кнопку 'Детали' в колонке 'Действие'"):
            page.ACTION_DETAILS.first.click()

        with allure.step("Открылось модальное окно 'Детали'"):
            expect(page.MODAL_WINDOW).to_be_visible()

        with allure.step("[МО] Наличие заголовка 'Детали'"):
            expect(page.MW_TITLE).to_be_visible()
            expect(page.MW_TITLE).to_have_text("Детали")
        with allure.step("[МО] Наличие строки 'IP адрес'"):
            expect(page.MWR_IP_ADDRESS).to_be_visible()
        with allure.step("[МО] Наличие строки 'Версия ПО источника'"):
            expect(page.MWR_VERSION_SOFTWARE_SOURCE).to_be_visible()
        with allure.step("[МО] Наличие строки 'Время последнего получения данных'"):
            expect(page.MWR_TIME_GET_SOURCE).to_be_visible()
        with allure.step("[МО] Наличие строки 'Редактор'"):
            expect(page.MWR_EDITOR).to_be_visible()
        with allure.step("[МО] Наличие строки 'Интервал обновления данных'"):
            expect(page.MWR_INTERVAL).to_be_visible()

        with allure.step("[МО] Клик по 'Статус получения данных' (^)"):
            expect(page.MW_STATUS_DROPDOWN).to_be_visible()
            page.MW_STATUS_DROPDOWN.click()

        with allure.step("Есть строки в раскрытом списке 'Статус получения данных'"):
            expect(page.MW_SD_ROW).not_to_have_count(0)

        with allure.step("Модальное окно закрывается по нажатию [X]"):
            expect(page.MW_CLOSE).to_be_visible()
            page.MW_CLOSE.click()
            expect(page.MODAL_WINDOW).not_to_be_visible()
