from playwright.sync_api import Page
from pages.Helpers.base_page import BasePage


class StoragePage(BasePage):

    page_path = "/storage"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        self.TAB_STRUCTURE = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Структура')]")
        self.TAB_STATISTICS = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Статистика')]")
        self.TAB_SEARCH = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Поиск в хранилище')]")
        self.TAB_SEARCH_CONTENT = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'По содержимому')]")
        self.TAB_SEARCH_COLUMN = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'По столбцам')]")
        self.TAB_RULES = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Правила импорта')]")


class StorageStructurePage(StoragePage):

    page_path = "/storage/structure"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo: кнопка 'Создать базу данных'
        # todo: поля поиска и строки, и действия


class StorageStatisticPage(StoragePage):

    page_path = "/storage/statistic"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo: Выбор базы данных
        # todo: Статистика по бд
        # todo: Динамика изменения кол-ва строк


class StorageSearchContentPage(StoragePage):

    page_path = "/storage/search/content"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo: выбор бд
        # todo: выбор таблицы

        # todo: Столбцы для поиска + Столбцы для вывода


class StorageSearchColumnPage(StoragePage):

    page_path = "/storage/search/column"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo: выбор бд
        # todo: выражение для поиска содержимого


class StorageRulesPage(StoragePage):

    page_path = "/storage/rules"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo: список исключений для бд
        # todo: список исключений для таблиц
