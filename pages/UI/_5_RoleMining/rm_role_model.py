from pages.Helpers.base_page import BasePage
from resourses.locators import RoleMiningLocators, MainLocators, AdminLocators


class RoleModel(BasePage):

    def open_rm_role_model(self):
        self.page.click(RoleMiningLocators.ROLE_MODEL)

    def should_enter_rm_role_model_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Ролевая модель" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.host + "/role-mining/role-model/byAD", "URL's do not match"
