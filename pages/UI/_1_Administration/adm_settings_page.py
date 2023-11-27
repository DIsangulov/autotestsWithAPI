from playwright.sync_api import Page
from pages.Helpers.base_page import BasePage


class AdmSettingsPage(BasePage):

    page_path = "/administration/settings/common"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        self.TAB_COMMON = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Административный узел')]")
        self.TAB_CLUSTER = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Служебная БД')]")
        self.TAB_DOMAIN = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Контроллер домена')]")
        self.TAB_STORAGE = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Хранилище')]")
        self.TAB_COLLECTOR = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Сбор данных')]")
        self.TAB_ML = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Анализ данных')]")
        self.TAB_MS = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Почта')]")
        self.TAB_SYSLOG = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Syslog')]")
        self.TAB_SECRETS = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Secrets')]")


class AdmSettingsCommonPage(AdmSettingsPage):

    page_path = "/administration/settings/common"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo:


class AdmSettingsClusterPage(AdmSettingsPage):

    page_path = "/administration/settings/cluster"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo:


class AdmSettingsDomainPage(AdmSettingsPage):

    page_path = "/administration/settings/domain"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo:


class AdmSettingsStoragePage(AdmSettingsPage):

    page_path = "/administration/settings/storage"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo:


class AdmSettingsCollectorPage(AdmSettingsPage):

    page_path = "/administration/settings/collector"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo:


class AdmSettingsMlPage(AdmSettingsPage):

    page_path = "/administration/settings/ml"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo:


class AdmSettingsMsPage(AdmSettingsPage):

    page_path = "/administration/settings/ms"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo:


class AdmSettingsSyslogPage(AdmSettingsPage):

    page_path = "/administration/settings/sys"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo:


class AdmSettingsSecretsPage(AdmSettingsPage):

    page_path = "/administration/settings/secrets"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo:
