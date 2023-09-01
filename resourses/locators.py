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


class AdminLocators:
    TITLE_MSG_NEW = "//div[@class='main-toolbar-left__text-title']"


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
