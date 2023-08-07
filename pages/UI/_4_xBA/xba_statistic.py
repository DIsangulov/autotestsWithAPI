from pages.Helpers.base_page import BasePage
from resourses.locators import MainLocators, XbaLocators, AdminLocators


class Statistic(BasePage):
    def open_xba_statistic(self):
        self.page.click(XbaLocators.XBA_STATISTIC)

    def should_enter_xba_statistic_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Статистика xBA" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.host + "/xBA-statistics/profiles", "URL's do not match"
