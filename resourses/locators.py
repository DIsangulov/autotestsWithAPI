class AuthLocators:
    LOGIN_INPUT = "//input[@type='email']"
    PASSWORD_INPUT = "//input[@id='password']"
    CHECKBOX_LOCAL = "//input[@type='checkbox']/.."
    ENTER_BUTTON = "//button[span[contains(text(), 'Войти')]]"
    PASS_VISIBLE = "//span[@class='icon is-right has-text-primary is-clickable']"
    WRONG_LOG_PASS_ALERT = "//div[@role='alert'][contains(text(), 'Неверный логин или пароль')]"


class MainLocators:
    HEADER_LOGO = "//div[@class='n-app-navigation__header']"
    DROPDOWN1 = "//div[@class='options visible']/ul/li[1]"
    DROPDOWN2 = "//div[@class='options visible']/ul/li[2]"
    X_BUTTON = "//span[@class='ngr-icon icon-close ngr-icon_none']"
    CLOSE_BUTTON = "//*[contains(text(),'Закрыть')]"
    SAVE_BUTTON = "//*[contains(text(),'Сохранить')]"
    HUMAN_ICON = "//button[@class='n-app-profile__ny n-app-button']"
    SIGN_OUT = "//*[contains(text(),'Выйти')]"
    ADD_BUTTON = "//*[text()='Добавить']"


class AdminLocators:
    TITLE_MSG_OLD = "//div[@class='title-main']"
    TITLE_MSG_NEW = "//div[@class='main-toolbar-left__text-title']"


class AnalyticsLocators:
    ANALYTICS = "//*[contains(text(),'Аналитика')]"
    MAILING_LISTS = "//*[contains(text(),'Рассылки')]"
    MAILING_LISTS_REPORTS = "//*[contains(text(),'Отчетов')]"
    REPORTS = "//*[contains(text(),'Отчеты')]"

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
