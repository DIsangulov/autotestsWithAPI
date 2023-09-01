import time

import allure
from playwright.sync_api import expect

from pages.Helpers.base_case import BaseCase
from pages.UI._1_Administration.adm_notification_list_page import AdmNotificationListPage


class AdmNotificationListCase(BaseCase):

    @allure.step("Открыть страницу Журнал Уведомлений")
    def open_page_by_steps(self):
        page = AdmNotificationListPage(self._page)

        # шаг нужен, чтобы боковое меню было закрыто
        with allure.step("Перейти в 'Настройка уведомлений'"):
            page.goto_page("/notification-center")
            page.page.wait_for_url(page.host + "/notification-center")

        with allure.step("Клик в боковом меню 'Администрирование'"):
            page.SB_ADMINISTRATION.click()

        with allure.step("Клик в меню 'Журнал уведомлений'"):
            page.SB_ADM_NOTIFICATION_LIST.click()

        with allure.step("Открылась страница 'Журнал уведомлений'"):
            page.page.wait_for_url(page.host + AdmNotificationListPage.page_path)
