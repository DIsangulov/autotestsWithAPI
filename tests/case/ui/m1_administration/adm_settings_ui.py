import time

import allure
from playwright.sync_api import expect

from pages.Helpers.base_case import BaseCase
from pages.UI._1_Administration.adm_settings_page import AdmSettingsPage, AdmSettingsClusterPage, AdmSettingsDomainPage, AdmSettingsStoragePage, AdmSettingsCollectorPage, AdmSettingsMlPage, AdmSettingsMsPage, AdmSettingsSyslogPage, AdmSettingsSecretsPage, AdmSettingsCommonPage


class AdmSettingsCase(BaseCase):

    @allure.step("Открыть страницу Настройки")
    def open_page_by_steps(self):
        page = AdmSettingsPage(self._page)

        # шаг нужен, чтобы боковое меню было закрыто
        with allure.step("Перейти в 'Настройка уведомлений'"):
            page.goto_page("/notification-center")
            page.page.wait_for_url(page.host + "/notification-center")

        with allure.step("Клик в боковом меню 'Администрирование'"):
            page.SB_ADMINISTRATION.click()
        with allure.step("Клик в меню 'Настройки'"):
            page.SB_ADM_SETTINGS.click()
        with allure.step("Открылась страница 'Настройки'"):
            page.page.wait_for_url(page.host + AdmSettingsPage.page_path)

        with allure.step("Клик по вкладке 'Служебная БД'"):
            page.TAB_CLUSTER.click()
        with allure.step("Вкладка открылась"):
            page.page.wait_for_url(page.host + AdmSettingsClusterPage.page_path)

        with allure.step("Клик по вкладке 'Контроллер домена'"):
            page.TAB_DOMAIN.click()
        with allure.step("Вкладка открылась"):
            page.page.wait_for_url(page.host + AdmSettingsDomainPage.page_path)

        with allure.step("Клик по вкладке 'Хранилище'"):
            page.TAB_STORAGE.click()
        with allure.step("Вкладка открылась"):
            page.page.wait_for_url(page.host + AdmSettingsStoragePage.page_path)

        with allure.step("Клик по вкладке 'Сбор данных'"):
            page.TAB_COLLECTOR.click()
        with allure.step("Вкладка открылась"):
            page.page.wait_for_url(page.host + AdmSettingsCollectorPage.page_path)

        with allure.step("Клик по вкладке 'Анализ данных'"):
            page.TAB_ML.click()
        with allure.step("Вкладка открылась"):
            page.page.wait_for_url(page.host + AdmSettingsMlPage.page_path)

        with allure.step("Клик по вкладке 'Почта'"):
            page.TAB_MS.click()
        with allure.step("Вкладка открылась"):
            page.page.wait_for_url(page.host + AdmSettingsMsPage.page_path)

        with allure.step("Клик по вкладке 'Syslog'"):
            page.TAB_SYSLOG.click()
        with allure.step("Вкладка открылась"):
            page.page.wait_for_url(page.host + AdmSettingsSyslogPage.page_path)

        with allure.step("Клик по вкладке 'Secrets'"):
            page.TAB_SECRETS.click()
        with allure.step("Вкладка открылась"):
            page.page.wait_for_url(page.host + AdmSettingsSecretsPage.page_path)

        with allure.step("Клик по вкладке 'Административный узел'"):
            page.TAB_COMMON.click()
        with allure.step("Вкладка открылась"):
            page.page.wait_for_url(page.host + AdmSettingsCommonPage.page_path)
