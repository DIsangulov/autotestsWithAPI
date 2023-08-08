from playwright.sync_api import Page

from pages.Helpers.base_page import BasePage


class SourcesPage(BasePage):

    page_path = "/datasource"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = SourcesPage.page_path

    # todo: кнопка перейти в библиотеку шаблонов
    # todo: кнопка импорт драйвера
    # todo: импорт файла паттернов
    # todo: кнопка подключить источник
    # > Из коннектора
    # > В редакторе

    # todo: локатор на поле ввода "Источник"
    # > тип подключения
    # > статус
    # > изменено

    # todo: на кнопки в поле "Действие
    # > редактировать
    # > Удалить
    # > Детали
    # >> Модальное окно детали поля
    # >> МОД > Статус получения данных раскрывашка
    # >> МОД > Закрыть МОД
