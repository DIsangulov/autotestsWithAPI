from selenium.webdriver.common.by import By


class MainLocators:
    SUCCESS_ENTER = By.XPATH, "//*[contains(text(),'Общая сводка по состоянию системы')]"
    VISIBLE_PASS = By.XPATH, "//input[@type='password']"
    SIDE_BAR = By.XPATH, "//div[@class='n-app-navigation__button']"


class AuthLocators:
    LOGIN_INPUT = By.XPATH, "//input[@type='email']"
    PAS_INPUT = By.XPATH, "//input[@type='password']"
    ENTER_BUT = By.XPATH, "//*[contains(text(),'Войти')]"
    PASS_VISIBLE = By.XPATH, "//span[@class='icon is-right has-text-primary is-clickable']"


class AdminLocators:
    ADMINISTRATION = By.XPATH, "//*[contains(text(),'Администрирование')]"
    ROLES = By.XPATH, "//*[contains(text(),'Роли')]"
    USERS = By.XPATH, "//*[contains(text(),'Пользователи')]"
    MONITORING = By.XPATH, "//*[contains(text(),'Мониторинг')]"
    LICENSES = By.XPATH, "//*[contains(text(),'Лицензии')]"
    UPDATE = By.XPATH, "//*[contains(text(),'Обновление')]"
    NOTIFICATION_LOG = By.XPATH, "//*[contains(text(),'Журнал уведомлений')]"
    SETTINGS = By.XPATH, "//*[contains(text(),'Настройки')]"


class DataLocators:
    SOURCES = By.XPATH, "//*[contains(text(),'Источники')]"
    REGEX = By.XPATH, "//*[contains(text(),'Регулярные выражения')]"
    SCRIPTS = By.XPATH, "//*[contains(text(),'Скрипты')]"
    STORAGE = By.XPATH, "//*[contains(text(),'Хранилище')]"


class AnalyticsLocators:
    NEWSLETTERS = By.XPATH, "//*[contains(text(),'Рассылки')]"
    REPORTS = By.XPATH, "//*[contains(text(),'Отчеты')]"
    VISUALIZATIONS = By.XPATH, "//*[contains(text(),'Визуализации')]"
    REQUESTS = By.XPATH, "//*[contains(text(),'Запросы')]"


class XbaLocators:
    PROFILES = By.XPATH, "//*[contains(text(),'Профили')]"
    XBA_STATISTIC = By.XPATH, "//*[contains(text(),'Статистика xBA')]"


class RoleMiningLocators:
    ROLE_MINING = By.XPATH, "//*[contains(text(),'Role mining')]"
    SETTINGS = By.XPATH, "//a[@href='/role-mining/settings']"
    ADSTATUS = By.XPATH, "//*[contains(text(),'Состояние AD')]"
    GROPE_AND_USERS = By.XPATH, "//*[contains(text(),'Группы и пользователи')]"
    ROLE_MODEL = By.XPATH, "//*[contains(text(),'Ролевая модель')]"
