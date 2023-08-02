from playwright.sync_api import Page


class Navigation:
    def __init__(self, page: Page):
        self.page = page

        self.HUMAN_ICON = self.page.locator("//button[@class='n-app-profile__ny n-app-button']")
        self.SIGN_OUT = self.page.locator("//*[contains(text(),'Выйти')]")

        self.SIDE_BAR = self.page.locator("//div[@class='n-app-navigation__button']")
