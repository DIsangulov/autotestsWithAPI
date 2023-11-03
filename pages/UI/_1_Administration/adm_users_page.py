import allure
from playwright.sync_api import expect, Page
from pages.Helpers.base_page import BasePage


class UsersPage(BasePage):
    page_path = "/users"

    def __init__(self, page: Page):
        self.add_user = UsersPageAddUserModalCard(page)

        super().__init__(page)
        self.page_path = self.__class__.page_path

        # TODO: self.TOOLBAR_Пригласить
        self.TOOLBAR_ADD_USER = page.locator("//div[@class='tooltip-content' and text()='Добавить вручную']/..")
        # TODO: self.TOOLBAR_Изменить роль группе

    def check_user_at_current_page(self, username: str, timeout: int = 300) -> bool:
        # FIXME: эта штука возвращает TimeoutError вместо bool
        return self.page.locator(f"//a[contains(text(), '{username}')]").is_enabled(timeout=timeout)

    def select_role(self, role_name: str, timeout: int = 300):
        with allure.step("Клик на выпадающее меню 'Выберите роль'"):
            self.add_user.SELECT_ROLE_DROPDOWN.click()

        # FIXME: тут может быть несколько совпадений -> зафиксировать под точное
        #  прокидываем имя 'testo', а матчится ['testo', 'testo123', 'o_testo']
        role_name_row = self.page.locator(f"//li[contains(text(), '{role_name}')]")
        with allure.step(f"Роль с именем '{role_name}' находится в выпадающем списке"):
            expect(role_name_row).to_be_visible(timeout=timeout)

        with allure.step(f"Клик на строку со значением {role_name}"):
            role_name_row.click()


class UsersPageAddUserModalCard(BasePage):

    def __init__(self, page: Page):
        super().__init__(page, auto_auth=False)

        self.MODAL_CARD = page.locator("//div[contains(@class, 'modal is-active')]")

        # TODO: MODAL_CARD_BUTTON_BACKGROUND_CORNER_CLOSE
        # TODO: MODAL_CARD_BUTTON_CORNER_CLOSE

        self.TAB_DOMAIN = page.locator("//li[.//span[contains(text(), 'Доменный')]]")
        self.TAB_LOCAL = page.locator("//li[.//span[contains(text(), 'Локальный')]]")

        self.DOMAIN_SECTION = page.locator("//div[contains(@class, 'modal is-active')]//section[@class='tab-content']/div[1]")

        self.INPUT_USERNAME_DOMAIN = self.DOMAIN_SECTION.locator("//input[contains(@placeholder, 'Логин')]")
        self.SELECT_ROLE_DROPDOWN = self.DOMAIN_SECTION.locator("//div[contains(@class, 'v-select') and .//input[@placeholder='Выберите роль']]")

        self.CHECKBOX_ADMIN = page.locator("//label[./span[text()='Администратор']]")
        self.CHECKBOX_SYSTEM_USER = page.locator("//label[./span[text()='Системная учетка']]")
        self.CHECKBOX_TECH_USER = page.locator("//label[./span[text()='Технологическая учeтка']]")  # В слове 'учетка' [e] - eng

        self.BUTTON_ADD_DOMAIN = self.DOMAIN_SECTION.locator("//button[./span[text()='Добавить']]")
        self.BUTTON_CLOSE_DOMAIN = self.DOMAIN_SECTION.locator("//button[./span[text()='Закрыть']]")

        self.LOCAL_SECTION = page.locator("//div[contains(@class, 'modal is-active')]//section[@class='tab-content']/div[2]")

        self.INPUT_RUSNAME = self.LOCAL_SECTION.locator("//input[contains(@placeholder, 'Имя, фамилия')]")
        self.INPUT_USERNAME = self.LOCAL_SECTION.locator("//input[contains(@placeholder, 'Логин')]")
        self.INPUT_PASSWORD = self.LOCAL_SECTION.locator("//input[contains(@placeholder, 'Пароль')]")
        self.INPUT_PASSWORD_IS_VISIBLE = self.LOCAL_SECTION.locator("//input[contains(@placeholder, 'Пароль')]/../span")
        self.INPUT_EMAIL = self.LOCAL_SECTION.locator("//div[label[text()='Почта *']]/div/input")
        self.INPUT_MOBILE = self.LOCAL_SECTION.locator("//div[label[text()='Телефон *']]/div/input")
        self.INPUT_DEPARTMENT = self.LOCAL_SECTION.locator("//input[contains(@placeholder, 'Отдел')]")
        self.INPUT_TITLE = self.LOCAL_SECTION.locator("//input[contains(@placeholder, 'Должность')]")

        self.BUTTON_ADD_LOCAL = self.LOCAL_SECTION.locator("//button[./span[text()='Добавить']]")
        self.BUTTON_CLOSE_LOCAL = self.LOCAL_SECTION.locator("//button[./span[text()='Закрыть']]")

    def open(self):
        assert False, f"Method not allowed for {self.__class__} class"
