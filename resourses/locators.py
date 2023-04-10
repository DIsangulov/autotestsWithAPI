from selenium.webdriver.common.by import By


class MainLocators:
    PRE_ENTER = By.XPATH, "//*[contains(text(),'Дополнительные')]"
    PRE_ENTER_AGREE = By.XPATH, "//*[contains(text(),'Перейти на сайт')]"
    SUCCESS_ENTER = By.XPATH, "//a[@class='n-app-navigation__logo router-link-exact-active router-link-active']"
    VISIBLE_PASS = By.XPATH, "//input[@type='password']"
    SIDE_BAR = By.XPATH, "//div[@class='n-app-navigation__button']"
    DROPDOWN1 = By.XPATH, "//div[@class='options visible']/ul/li[1]"
    DROPDOWN2 = By.XPATH, "//div[@class='options visible']/ul/li[2]"


class AuthLocators:
    LOGIN_INPUT = By.XPATH, "//input[@type='email']"
    PAS_INPUT = By.XPATH, "//input[@type='password']"
    ENTER_BUT = By.XPATH, "//*[contains(text(),'Войти')]"
    PASS_VISIBLE = By.XPATH, "//span[@class='icon is-right has-text-primary is-clickable']"


class AdminLocators:
    ADMINISTRATION = By.XPATH, "//*[contains(text(),'Администрирование')]"
    ROLES = By.XPATH, "//*[contains(text(),'Роли')]"
    USERS = By.XPATH, "//*[contains(text(),'Пользователи')]"
    SESSIONS = By.XPATH, "//*[contains(text(),'Сессии')]"
    MONITORING = By.XPATH, "//*[contains(text(),'Мониторинг')]"
    LICENSES = By.XPATH, "//*[contains(text(),'Лицензии')]"
    UPDATE = By.XPATH, "//*[contains(text(),'Обновление')]"
    NOTIFICATION_LOG = By.XPATH, "//*[contains(text(),'Журнал уведомлений')]"
    NOTIFICATION_LOG_USER = By.XPATH, "//*[contains(text(),'Пользовательские')]"
    NOTIFICATION_LOG_ADMIN = By.XPATH, "//*[contains(text(),'Административные')]"
    SETTINGS = By.XPATH, "//*[contains(text(),'Настройки')]"
    TITLE_MSG_OLD = By.XPATH, "//div[@class='title-main']"
    TITLE_MSG_NEW = By.XPATH, "//div[@class='main-toolbar-left__text-title']"
    TITLE_MSG_NEW2 = By.XPATH, "//div[@class='main-toolbar-left__text-title']"
    ADMIN_NODE = By.XPATH, "//*[contains(text(),'Административный узел')]"
    DOMAIN_CONTROLLER = By.XPATH, "//*[contains(text(),'Контроллер домена')]"
    SERVICE_DB = By.XPATH, "//*[contains(text(),'Служебная БД')]"
    STORAGE = By.XPATH, "(//li[@class='ngr-tabs__item'])[3]"
    DATA_COLLECTION = By.XPATH, "(//li[@class='ngr-tabs__item'])[4]"
    DATA_ANALYSIS = By.XPATH, "(//li[@class='ngr-tabs__item'])[5]"
    POST = By.XPATH, "(//li[@class='ngr-tabs__item'])[6]"
    SYSLOG = By.XPATH, "(//li[@class='ngr-tabs__item'])[7]"
    SECRETS = By.XPATH, "(//li[@class='ngr-tabs__item'])[8]"


class DataLocators:
    DATAS = By.XPATH, "//*[contains(text(),'Данные')]"
    SOURCES = By.XPATH, "//*[contains(text(),'Источники')]"
    REGEX = By.XPATH, "//*[contains(text(),'Регулярные выражения')]"
    SCRIPTS = By.XPATH, "//*[contains(text(),'Скрипты')]"
    STORAGE = By.XPATH, "//*[contains(text(),'Хранилище')]"
    STRUCTURE = By.XPATH, "(//*[contains(text(),'Структура')])[2]"
    STATISTICS = By.XPATH, "(//li[@class='ngr-tabs__item'])[1]"
    STORAGE_SEARCH = By.XPATH, "(//li[@class='ngr-tabs__item'])[2]"
    STORAGE_SEARCH_CONTENT = By.XPATH, "//*[contains(text(),'По содержимому')]"
    STORAGE_SEARCH_COLUMN = By.XPATH, "//*[contains(text(),'По столбцам')]"
    IMPORT_RULES = By.XPATH, "(//li[@class='ngr-tabs__item'])[3]"

class AnalyticsLocators:
    MAILING_LISTS = By.XPATH, "//*[contains(text(),'Рассылки')]"
    REPORTS = By.XPATH, "//*[contains(text(),'Отчеты')]"
    VISUALIZATIONS = By.XPATH, "//*[contains(text(),'Визуализации')]"
    REQUESTS = By.XPATH, "//*[contains(text(),'Запросы')]"
    CREATE_MAILING_LIST = By.XPATH, "//*[contains(text(),'Создать рассылку')]"
    INPUT_MAILING_NAME = By.XPATH, "//input[@placeholder='Введите название рассылки']"
    DROPDOWN_MAILING_TYPE = By.XPATH, "//span[@class='ngr-dropdown__input-selected']"
    NEXT_BUTTON = By.XPATH, "//*[contains(text(),'Далее')]"


class XbaLocators:
    XBA = By.XPATH, "//*[contains(text(),'xBA')][1]"
    PROFILES = By.XPATH, "//*[contains(text(),'Профили')]"
    METAPROFILES = By.XPATH, "//*[contains(text(),'Метапрофили')]"
    XBA_STATISTIC = By.XPATH, "//*[contains(text(),'Статистика xBA')]"
    PUK = By.XPATH, "//button[@class='n-app-profile__ny n-app-button']"


class RoleMiningLocators:
    ROLE_MINING = By.XPATH, "//*[contains(text(),'Role mining')]"
    SETTINGS = By.XPATH, "//a[@href='/role-mining/settings']"
    ADSTATUS = By.XPATH, "//*[contains(text(),'Состояние AD')]"
    GROPES_AND_USERS = By.XPATH, "//*[contains(text(),'Группы и пользователи')]"
    ROLE_MODEL = By.XPATH, "//*[contains(text(),'Ролевая модель')]"
    CLEAR_BUTTON = By.XPATH, "//*[contains(text(),'Очистить')]"
    CLEAR_BUTTON_YES = By.XPATH, "//button[@class ='ngr-button ngr-promt__btn ngr-button_primary']"
    CLEAR_BUTTON_NO = By.XPATH, "//*[contains(text(),'Отмена')]"
    SELECT_DB = By.XPATH, "//input[@placeholder ='Выберите базу данных']"
    SELECT_DB_CHOISE = By.XPATH, "//div[@class ='options visible']/ul/li[1]"
    SELECT_TABLE = By.XPATH, "//input[@placeholder ='Выберите таблицу']"
    SAVE_BUTTON = By.XPATH, "//*[contains(text(),'Сохранить')]"
    SAVE_DROPDOWN_BUTTON = By.XPATH, "//div[@class ='ngr-button-dropdown__arrow']"
    RECALCULATE_BUTTON = By.XPATH, "//*[contains(text(),'Пересчитать')]"
    RERUN_BUTTON = By.XPATH, "//*[contains(text(),'Запустить')]"
    CALCULATION_SETTINGS = By.XPATH, "//*[contains(text(),'Настройка расчета')]"
    GEAR_BUTTON = By.XPATH, "//span[@class='ngr-icon icon-menu-setting']"
    CHECKBOX_SYSLOG = By.XPATH, "(//input[@class='ngr-checkbox__input'])[1]"
    CHECKBOX_EMAIL = By.XPATH, "(//input[@class='ngr-checkbox__input'])[2]"
    INPUT_EMAIL = By.XPATH, "//textarea[@placeholder='Введите E-mail получателей через «;»']"
    SERVER_ADDERESS = By.XPATH, "//input[@placeholder='Введите адрес сервера']"
    PORT = By.XPATH, "//input[@placeholder='Введите порт']"
    DROPDOWN_EXCHANGE_PROTOCOL = By.XPATH, "//*[contains(text(),'Выберите протокол обмена')]"
    ADD_BUTTON = By.XPATH, "//*[contains(text(),'Добавить')]"
    TRASH_ICON = By.XPATH, "(//span[@class='ngr-icon icon-trash-can'])[1]"
    DELETE_BUTTON = By.XPATH, "//button[@class='ngr-button ngr-promt__btn ngr-button_primary']"
