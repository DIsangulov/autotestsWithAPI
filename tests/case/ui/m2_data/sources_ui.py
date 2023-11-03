import time

import allure
from playwright.sync_api import expect, Page

from pages.UI._2_Data.sources_page import SourcesPage, SourcesEditorPage
from pages.UI._2_Data.connectors_page import ConnectorsPage, LogoPage, ConnectorsCreatePage

UI_AUTO_TEST_ = "UI_AUTO_TEST_"


@allure.step("Открыть страницу Источники")
def open_page_by_steps(browser: Page):
    page = SourcesPage(browser)

    with allure.step("Перейти в 'Профиль пользователя'"):
        page.goto_page("/personal")
        browser.wait_for_url(page.host + "/personal")

    with allure.step("Клик в боковом меню 'Данные'"):
        page.SB_DATA.click()

    with allure.step("Клик в меню 'Источники'"):
        page.SB_DATA_SOURCES.click()

    with allure.step("Переход на страницу 'Источники'"):
        browser.wait_for_url(page.host + SourcesPage.page_path)


def open_modal_w_actions_details(browser: Page):
    page = SourcesPage(browser)

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

    with allure.step("Модальное окно закрывается по клику [X]"):
        expect(page.MW_CLOSE).to_be_visible()
        page.MW_CLOSE.click()
        expect(page.MODAL_WINDOW).not_to_be_visible()


def open_new_source_editor_by_steps(browser: Page):
    page = SourcesPage(browser)

    with allure.step("Открыть страницу 'Источники Данных'"):
        page.open()

    with allure.step("Клик по кнопке 'Подключить источник'"):
        page.NEW_SOURCE_BUTTON.click()

    with allure.step("Клик на дропдавн 'В редакторе'"):
        expect(page.NSB_IN_EDITOR).to_be_visible()
        page.NSB_IN_EDITOR.click()

    with allure.step("Открылась страница создания источника в редакторе"):
        browser.wait_for_url(page.host + SourcesEditorPage.page_path)


def open_new_source_connector_by_steps(browser: Page):
    page = SourcesPage(browser)

    with allure.step("Открыть страницу 'Источники Данных'"):
        page.open()

    with allure.step("Клик по кнопке 'Подключить источник'"):
        page.NEW_SOURCE_BUTTON.click()

    with allure.step("Клик на дропдавн 'Из коннектора'"):
        expect(page.NSB_FROM_CONNECTOR).to_be_visible()
        page.NSB_FROM_CONNECTOR.click()

    with allure.step("Открылась страница 'Подключение источника'"):
        browser.wait_for_url(page.host + "/datasource/create/connector")


def library_connectors_navigation(browser: Page):
    page = SourcesPage(browser)

    with allure.step("Открыть страницу 'Источники Данных'"):
        page.open()

    with allure.step("toolbar: Клик по кнопке 'Перейти в библиотеку шаблонов'"):
        page.TOOLBAR_GOTO_CONNECTORS_LIBRARY.click()
    with allure.step("Открылась страница Библиотека коннекторов"):
        browser.wait_for_url(ConnectorsPage.page_path)

    page = LogoPage(browser)

    with allure.step("Клик по вкладке 'Логотипы'"):
        page.TAB_LOGOS.click()
    with allure.step("Открылась страница 'Библиотека логотипов'"):
        browser.wait_for_url(page.host + LogoPage.page_path)

    with allure.step("Клик по кнопке 'Создать логотип'"):
        page.CREATE_LOGO_BUTTON.click()
    with allure.step("Открылось модальное окно 'Создать новый логотип'"):
        expect(page.MODAL_WINDOW).to_be_visible()
    with allure.step("[МО] Клик по [X]"):
        page.MW_CLOSE.click()
    with allure.step("Модальное окно закрылось"):
        expect(page.MODAL_WINDOW).not_to_be_visible()

    page = ConnectorsPage(browser)

    with allure.step("Клик по вкладке 'Коннекторы'"):
        page.TAB_CONNECTORS.click()
    with allure.step("Открылась страница 'Библиотека коннекторов'"):
        page.page.wait_for_url(page.host + ConnectorsPage.page_path)

    with allure.step("Клик по кнопке 'Создать коннектор'"):
        page.CREATE_CONNECTOR_BUTTON.click()
    with allure.step("Открылась страница 'Создание коннектора'"):
        page.page.wait_for_url(page.host + ConnectorsCreatePage.page_path)

    page = ConnectorsCreatePage(browser)

    with allure.step("Ввод текста в инпут для появления 'Вы уверены?'"):
        page.NAME_FILED.fill("Текст")

    with allure.step("Клик по кнопке <- назад"):
        page.BACK_BUTTON.click()

    with allure.step("Появилось модальное окно:'Вы уверены?'"):
        expect(page.YES_BUTTON).to_be_visible()
    with allure.step("В модалке 'Вы точно уверены?' Клик по кнопке ДА"):
        page.YES_BUTTON.click()

    page = ConnectorsPage(browser)

    with allure.step("Открылась страница 'Библиотека коннекторов'"):
        browser.wait_for_url(page.host + ConnectorsPage.page_path)

    with allure.step("Клик по кнопке <- назад"):
        page.BACK_BUTTON.click()
    with allure.step("Открылась страница 'Источники данных'"):
        browser.wait_for_url(page.host + SourcesPage.page_path)


def source_create_editor_syslog(browser: Page):
    page = SourcesEditorPage(browser)

    with allure.step("Открыть страницу 'Создание источника в редакторе'"):
        page.new_source()

    # todo: остальные шаги
