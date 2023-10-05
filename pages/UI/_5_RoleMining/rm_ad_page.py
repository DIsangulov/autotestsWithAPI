from playwright.sync_api import Page
from pages.Helpers.base_page import BasePage


class RMStateADPage(BasePage):

    page_path = "/role-mining/state-ad"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        self.TAB_STATISTICS = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Статистика')]")
        self.TAB_RECOMMENDATIONS = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Рекомендации')]")


class RMStateADStatisticsPage(RMStateADPage):

    page_path = "/role-mining/state-ad/statistics"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # self.SOMETHING = self.page.locator("//locator")


class RMStateADRecommendationsPage(RMStateADPage):

    page_path = "/role-mining/state-ad/recommendations"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # self.SOMETHING = self.page.locator("//locator")
