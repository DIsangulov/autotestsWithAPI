

class MainLocators:
    PRE_ENTER = "//*[contains(text(),'Дополнительные')]"
    PRE_ENTER_AGREE = "//*[contains(text(),'Перейти на сайт')]"
    SUCCESS_ENTER = "//a[@class='n-app-navigation__logo router-link-exact-active router-link-active']"
    VISIBLE_PASS = "//input[@type='password']"
    LOCAL_CHECK_BOX = "//span[@class='check']"
    SIDE_BAR = "//div[@class='n-app-navigation__button']"
    DROPDOWN1 = "//div[@class='options visible']/ul/li[1]"
    DROPDOWN2 = "//div[@class='options visible']/ul/li[2]"
    X_BUTTON = "//span[@class='ngr-icon icon-close ngr-icon_none']"
    CLOSE_BUTTON = "//*[contains(text(),'Закрыть')]"
    SAVE_BUTTON = "//*[contains(text(),'Сохранить')]"
    HUMAN_ICON = "//button[@class='n-app-profile__ny n-app-button']"
    SIGN_OUT = "//*[contains(text(),'Выйти')]"
    OPTIONS_VISIBLE = "//div[@class='options visible']"
    ADD_BUTTON = "//*[text()='Добавить']"


class AuthLocators:
    LOGIN_INPUT = "//input[@type='email']"
    PAS_INPUT = "//input[@type='password']"
    CHECKBOX_LOCAL = "//input[@type='checkbox']/.."
    ENTER_BUT = "//*[contains(text(),'Войти')]"
    PASS_VISIBLE = "//span[@class='icon is-right has-text-primary is-clickable']"


class AdminLocators:
    ADMINISTRATION = "//*[contains(text(),'Администрирование')]"
    ROLES = "//*[contains(text(),'Роли')]"
    USERS = "//*[contains(text(),'Пользователи')]"
    SESSIONS = "//*[contains(text(),'Сессии')]"
    MONITORING = "//*[contains(text(),'Мониторинг')]"
    LICENSES = "//*[contains(text(),'Лицензии')]"
    UPDATE = "//*[contains(text(),'Обновление')]"
    NOTIFICATION_LOG = "//*[contains(text(),'Журнал уведомлений')]"
    NOTIFICATION_LOG_USER = "//*[contains(text(),'Пользовательские')]"
    NOTIFICATION_LOG_ADMIN = "//*[contains(text(),'Административные')]"
    SETTINGS = "//*[contains(text(),'Настройки')]"
    TITLE_MSG_OLD = "//div[@class='title-main']"
    TITLE_MSG_NEW = "//div[@class='main-toolbar-left__text-title']"
    ADMIN_NODE = "//*[contains(text(),'Административный узел')]"
    DOMAIN_CONTROLLER = "//*[contains(text(),'Контроллер домена')]"
    SERVICE_DB = "//*[contains(text(),'Служебная БД')]"
    STORAGE = "(//li[@class='ngr-tabs__item'])[3]"
    DATA_COLLECTION = "(//li[@class='ngr-tabs__item'])[4]"
    DATA_ANALYSIS = "(//li[@class='ngr-tabs__item'])[5]"
    POST = "(//li[@class='ngr-tabs__item'])[6]"
    SYSLOG = "(//li[@class='ngr-tabs__item'])[7]"
    SECRETS = "(//li[@class='ngr-tabs__item'])[8]"


class DataLocators:
    DATAS = "//*[contains(text(),'Данные')]"
    SOURCES = "//*[contains(text(),'Источники')]"
    REGEX = "//*[contains(text(),'Регулярные выражения')]"
    SCRIPTS = "//*[contains(text(),'Скрипты')]"
    STORAGE = "//*[contains(text(),'Хранилище')]"
    STRUCTURE = "(//*[contains(text(),'Структура')])[2]"
    STATISTICS = "(//li[@class='ngr-tabs__item'])[1]"
    STORAGE_SEARCH = "(//li[@class='ngr-tabs__item'])[2]"
    STORAGE_SEARCH_CONTENT = "//*[contains(text(),'По содержимому')]"
    STORAGE_SEARCH_COLUMN = "//*[contains(text(),'По столбцам')]"
    IMPORT_RULES = "(//li[@class='ngr-tabs__item'])[3]"


class AnalyticsLocators:
    ANALYTICS = "//*[contains(text(),'Аналитика')]"
    MAILING_LISTS = "//*[contains(text(),'Рассылки')]"
    MAILING_LISTS_REPORTS = "//*[contains(text(),'Отчетов')]"
    MAILING_LISTS_NEW_DATA = "//*[contains(text(),'Новых данных')]"
    REPORTS = "//*[contains(text(),'Отчеты')]"
    VISUALIZATIONS = "//*[contains(text(),'Визуализации')]"
    REQUESTS = "//*[contains(text(),'Запросы')]"
    CREATE_MAILING_LIST = "//*[contains(text(),'Создать рассылку')]"
    INPUT_MAILING_NAME = "//input[@placeholder='Введите название рассылки']"
    DROPDOWN_MAILING_TYPE = "//span[@class='ngr-dropdown__input-selected']"
    NEXT_BUTTON = "//*[contains(text(),'Далее')]"

    ADD_REPORT_BUTTON = "(//span[@class='icon btn-icon'])[2]"  # создание отчета и сохранение отчета
    REPORT_NAME_AREA_IN = "//input[@placeholder='Введите имя отчета']"
    REPORT_DESCRIPTION_IN = "//textarea[@placeholder='Введите описание отчета']"
    ACCESS_SETTINGS = "(//span[@class='icon btn-icon'])[1]"
    PUBLESHED_TOGLER_ON = "//*[contains(text(),'Не опубликован')]"
    PUBLESHED_TOGLER_OFF = "//*[contains(text(),'Опубликован')]"
    REPORT_CLOSED_TOGLER = "//*[contains(text(),'Закрыт')]"
    LAST_REPORT_IN_LIST = "//td[@data-label='Отчет']"

    ROLE = "//input[@placeholder='Выберите роль']"
    USERS = "//input[@placeholder='Выберите пользователя']"
    ACCESS = "(//div[@class='ngr-dropdown__dropdown-popover dropdown-container'])[2]"

    ROLE_SYSOP = "//*[contains(text(),'sysop')]"
    USER_DATAPLAN_QAA = "(//*[contains(text(),'dataplan_qaa')])[1]"

    ACCESS_READ = "//*[contains(text(),'Чтение')]"
    ACCESS_WRITE = "//*[contains(text(),'Запись')]"
    ACCESS_EXECUTE = "(//*[contains(text(),'Выполнение')])[1]"
    ACCESS_ACCESS_SETTINGS = "(//*[contains(text(),'Настройка доступа')])[2]"
    CHECKBOX_READ = "(//input[@type='checkbox'])[7]"
    CHECKBOX_WRITE = "(//input[@type='checkbox'])[8]"
    CHECKBOX_EXECUTE = "(//input[@type='checkbox'])[9]"
    CHECKBOX_ACCESS_SETTINGS = "(//input[@type='checkbox'])[10]"

    CHECKBOX_READ_FOR_USERS_TAB = "(//input[@type='checkbox'])[11]"
    CHECKBOX_WRITE_FOR_USERS_TAB = "(//input[@type='checkbox'])[12]"
    CHECKBOX_EXECUTE_FOR_USERS_TAB = "(//input[@type='checkbox'])[13]"
    CHECKBOX_ACCESS_SETTINGS_FOR_USERS_TAB = "(//input[@type='checkbox'])[14]"

    TRASH = "(//span[@class='icon btn-icon'])[6]"
    CONFIRM_TRASH = "//*[contains(text(),'Удалить отчет')]"

    USERS_TAB = "(//*[contains(text(),'Пользователи')])[2]"


class XbaLocators:
    XBA = "//*[contains(text(),'xBA')][1]"
    PROFILES = "//*[contains(text(),'Профили')]"
    METAPROFILES = "//*[contains(text(),'Метапрофили')]"
    XBA_STATISTIC = "//*[contains(text(),'Статистика xBA')]"



class RoleMiningLocators:
    ROLE_MINING = "//*[contains(text(),'Role mining')]"
    SETTINGS = "//a[@href='/role-mining/settings']"
    CALCULATION_SETTINGS = "//*[contains(text(),'Настройка расчета')]"
    ADSTATUS = "//*[contains(text(),'Состояние AD')]"
    RECOMMENDATION = "//*[contains(text(),'Рекомендации')]"
    GROPES_AND_USERS = "//*[contains(text(),'Группы и пользователи')]"
    ROLE_MODEL = "//*[contains(text(),'Ролевая модель')]"
    CLEAR_BUTTON = "//*[contains(text(),'Очистить')]"
    CLEAR_BUTTON_YES = "//button[@class ='ngr-button ngr-promt__btn ngr-button_primary']"
    CLEAR_BUTTON_NO = "//*[contains(text(),'Отмена')]"
    SELECT_DB = "//input[@placeholder ='Выберите базу данных']"
    SELECT_DB_CHOISE = "//div[@class ='options visible']/ul/li[1]"
    SELECT_TABLE = "//input[@placeholder ='Выберите таблицу']"
    SAVE_BUTTON = "//*[contains(text(),'Сохранить')]"
    SAVE_DROPDOWN_BUTTON = "//div[@class ='ngr-button-dropdown__arrow']"
    RECALCULATE_BUTTON = "//*[contains(text(),'Пересчитать')]"
    RERUN_BUTTON = "//*[contains(text(),'Запустить')]"
    GEAR_BUTTON = "//span[@class='ngr-icon icon-menu-setting']"
    CHECKBOX_SYSLOG = "(//input[@class='ngr-checkbox__input'])[1]"
    CHECKBOX_EMAIL = "(//input[@class='ngr-checkbox__input'])[2]"
    INPUT_EMAIL = "//textarea[@placeholder='Введите E-mail получателей через «;»']"
    SERVER_ADDERESS = "//input[@placeholder='Введите адрес сервера']"
    PORT = "//input[@placeholder='Введите порт']"
    DROPDOWN_EXCHANGE_PROTOCOL = "//*[contains(text(),'Выберите протокол обмена')]"
    ADD_BUTTON = "//*[contains(text(),'Добавить')]"
    TRASH_ICON = "(//span[@class='ngr-icon icon-trash-can'])[1]"
    DELETE_BUTTON = "//button[@class='ngr-button ngr-promt__btn ngr-button_primary']"
