from playwright.sync_api import Page


class Navigation:
    def __init__(self, page: Page):
        self.page = page

        self.PROFILE_BUTTON = self.page.locator("//button[@class='n-app-profile__ny n-app-button']")
        self.PB_USER_PROFILE = self.page.locator("//a[*[contains(text(),'Профиль пользователя')]]")
        self.PB_NOTIFICATION_SETTINGS = self.page.locator("//a[*[contains(text(),'Настройки уведомлений')]]")
        self.PB_SIGN_OUT = self.page.locator("//*[contains(text(),'Выйти')]")

        self.SIDE_BAR = self.page.locator("//div[@class='n-app-navigation__button']")
