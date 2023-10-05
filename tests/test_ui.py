import allure
import pytest

from resourses.credentials import TARGET_URL
from resourses.credentials import TestUsers
from tests.case.ui.auth_ui import AuthCase
from tests.case.ui.m1_administration.roles_ui import RolesCase
from tests.case.ui.m1_administration.sessions_ui import SessionsCase
from tests.case.ui.m1_administration.users_ui import UsersCase
from tests.case.ui.m1_administration.monitoring_ui import MonitoringCase
from tests.case.ui.m1_administration.license_ui import LicenseCase
from tests.case.ui.m1_administration.updates_ui import UpdatesCase
from tests.case.ui.m1_administration.adm_notification_list_ui import AdmNotificationListCase
from tests.case.ui.m1_administration.adm_settings_ui import AdmSettingsCase
from tests.case.ui.m2_data.scripts_ui import DataScriptsCase
from tests.case.ui.m2_data.sources_ui import DataSourcesCase
from tests.case.ui.m2_data.storage_ui import DataStorageCase
from tests.case.ui.m3_analytics.mailing_ui import MailingsCase
from tests.case.ui.m3_analytics.report_ui import ReportsCase
from tests.case.ui.m3_analytics.visualisation_ui import VisualisationCase
from tests.case.ui.m3_analytics.query_ui import QueriesCase
from tests.case.ui.m4_xba.xba_profiles_ui import XbaProfilesCase
from tests.case.ui.m4_xba.xba_metaprofiles_ui import XbaMetaprofilesCase
from tests.case.ui.m4_xba.xba_statistics_ui import XbaStatisticsCase
from tests.case.ui.m5_RM.rm_settings_ui import RMSettingsCase
from tests.case.ui.m5_RM.rm_ad_ui import RMStateADCase
from tests.case.ui.m5_RM.rm_groups_and_users_ui import RMGroupsAndUsersCase
from tests.case.ui.m5_RM.rm_role_model_ui import RMRoleModelCase


@pytest.fixture(autouse=True, scope='session')
def _print_debug_info():
    print("\n" + "="*42)
    print(f"TARGET_URL: {TARGET_URL}")
    print("="*42 + "\n")
    yield


class SuiteName:
    NAVIGATION = "Навигация"

    AUTH_PAGE = "Страница Авторизации"

    ADMINISTRATION_COMMON = "Раздел Администрирование"

    DATA_COMMON = "Раздел Данные"
    DATA_SOURCES = "Источники"
    DATA_SCRIPTS = "Скрипты"
    DATA_STORAGE = "Хранилище"

    ANALYTICS_COMMON = "Раздел Аналитика"

    XBA_COMMON = "Раздел xBA"

    ROLE_MINING_COMMON = "Раздел Role Mining"


@allure.suite(SuiteName.AUTH_PAGE)
class TestAuth:

    @allure.title("Авторизация valid")
    @allure.description("Самая обычная авторизация")
    @pytest.mark.parametrize('auth_data_ad', [TestUsers.DpQaa])
    def test_valid_auth(self, browser_without_auth, auth_data_ad):
        AuthCase(browser_without_auth).valid_auth(auth_data_ad)

    @allure.title("Авторизация | Чекбокс | invalid")
    @allure.description("Проставлен чекбокс 'локально' для неЛокального пользователя")
    @pytest.mark.parametrize('auth_data_invalid', [{
        "username": TestUsers.DpQaa.get("username"),
        "password": TestUsers.DpQaa.get("password"),
        "local": True   # <- будет клик на чекбокс 'локально'
    }])
    def test_invalid_checkbox_auth(self, browser_without_auth, auth_data_invalid):
        AuthCase(browser_without_auth).invalid_auth(auth_data_invalid)

    @allure.title("Авторизация | Неверный пароль | invalid")
    @allure.description("Попытка авторизации с неверным паролем")
    @pytest.mark.parametrize('auth_data_invalid', [{
        "username": TestUsers.DpQaa.get("username"),
        "password": TestUsers.DpQaa.get("password") + "mistake",
        "local": TestUsers.DpQaa.get("local")
    }])
    def test_invalid_password_auth(self, browser_without_auth, auth_data_invalid):
        AuthCase(browser_without_auth).invalid_auth(auth_data_invalid)

    # tit 203 323, 363
    @allure.title("Авторизация | Локальный пользователь | valid")
    @allure.description("Самая обычная авторизация Локальный пользователь")
    @pytest.mark.parametrize('auth_data_local', [TestUsers.DpQaaLocal])
    def test_valid_auth_local(self, browser_without_auth, auth_data_local):
        AuthCase(browser_without_auth).valid_auth(auth_data_local)

    # tit 240 332, 508, 861
    @allure.title("Авторизация | Локальный пользователь | invalid")
    @allure.description("Авторизация Локальный пользователь с неверными логином и паролем")
    @pytest.mark.parametrize('auth_data_invalid', [{
        "username": 'test_invalid_username',
        "password": 'also_invalid@password',
        "local": True
    }])
    def test_invalid_auth_local(self, browser_without_auth, auth_data_invalid):
        AuthCase(browser_without_auth).invalid_auth(auth_data_invalid)

    # tit 371
    @allure.title("Авторизация | Локальный пользователь | Неправильный пароль")
    @allure.description("Авторизация Локальный пользователь с неверным паролем")
    @pytest.mark.parametrize('auth_data_wrong_password', [{
        "username": TestUsers.DpQaaLocal.get("username"),
        "password": 'but_there_is@invalid@password',
        "local": True
    }])
    def test_invalid_pass_auth_local(self, browser_without_auth, auth_data_wrong_password):
        AuthCase(browser_without_auth).invalid_auth(auth_data_wrong_password)

    # todo: tit 532

    # tit 594
    @allure.title("Авторизация | Локальный пользователь | Без чекбокса")
    @allure.description("Локальный пользователь, не проставил чекбокс 'local'")
    @pytest.mark.parametrize('auth_data_no_checkbox', [{
        "username": TestUsers.DpQaaLocal.get("username"),
        "password": TestUsers.DpQaaLocal.get("password"),
        "local": False  # <--не будет клика на чекбокс
    }])
    def test_invalid_cuz_no_checkbox_auth_local(self, browser_without_auth, auth_data_no_checkbox):
        AuthCase(browser_without_auth).invalid_auth(auth_data_no_checkbox)

    # tit 638
    @allure.title("Авторизация | Локальный пользователь | Невалидный логин")
    @allure.description("Локальный пользователь, пароль верный, но не логин")
    @pytest.mark.parametrize('auth_data_no_checkbox', [{
        "username": TestUsers.DpQaaLocal.get("username") + "mistake",
        "password": TestUsers.DpQaaLocal.get("password"),
        "local": True
    }])
    def test_invalid_login_auth_local(self, browser_without_auth, auth_data_no_checkbox):
        AuthCase(browser_without_auth).invalid_auth(auth_data_no_checkbox)

    # tit 708
    @allure.title("Авторизация | Выход из профиля пользователя")
    @allure.description("Выход по кнопке 'Выйти'")
    @pytest.mark.parametrize('auth_data', [TestUsers.DpQaaLocal])
    def test_log_out(self, browser_without_auth, auth_data):
        AuthCase(browser_without_auth).log_out(auth_data)


@allure.suite(SuiteName.ADMINISTRATION_COMMON)
class TestAdministrationRoles:

    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Роли'")
    def test_open_page_by_steps(self, browser):
        RolesCase(browser).open_page_by_steps()


@allure.suite(SuiteName.ADMINISTRATION_COMMON)
class TestAdministrationUsers:

    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Пользователи'")
    def test_open_page_by_steps(self, browser):
        UsersCase(browser).open_page_by_steps()


@allure.suite(SuiteName.ADMINISTRATION_COMMON)
class TestAdministrationSessions:

    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Сессии'")
    def test_open_page_by_steps(self, browser):
        SessionsCase(browser).open_page_by_steps()


@allure.suite(SuiteName.ADMINISTRATION_COMMON)
class TestAdministrationMonitoring:

    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Мониторинг'")
    def test_open_page_by_steps(self, browser):
        MonitoringCase(browser).open_page_by_steps()


@allure.suite(SuiteName.ADMINISTRATION_COMMON)
class TestAdministrationLicense:

    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Лицензии'")
    def test_open_page_by_steps(self, browser):
        LicenseCase(browser).open_page_by_steps()


@allure.suite(SuiteName.ADMINISTRATION_COMMON)
class TestAdministrationUpdates:

    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Обновление'")
    @allure.description("""
    Переход на страницу, используя UI элементы;
    Работа вкладки 'Версии компонентов';
    Работа вкладки 'Дополнения'
    """)
    def test_open_page_by_steps(self, browser):
        UpdatesCase(browser).open_page_by_steps()


@allure.title(SuiteName.ADMINISTRATION_COMMON)
class TestAdministrationNotificationList:

    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Журнал уведомлений'")
    def test_open_page_by_steps(self, browser):
        AdmNotificationListCase(browser).open_page_by_steps()


@allure.title(SuiteName.ADMINISTRATION_COMMON)
class TestAdministrationSettings:

    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Настройки'")
    @allure.description("""
    Переход на страницу, используя UI элементы;
    Работа вкладок;
    """)
    def test_open_page_by_steps(self, browser):
        AdmSettingsCase(browser).open_page_by_steps()


@allure.suite(SuiteName.DATA_SOURCES)
class TestDataSources:

    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Источники'")
    @allure.description("Открыть страницу через боковое меню")
    def test_open_page_by_steps(self, browser):
        DataSourcesCase(browser).open_page_by_steps()

    @allure.title("Открыть модальное окно 'Детали'")
    @allure.description("""
    На странице 'Источники' в колонке 'Действие',
    при нажатии на кнопку 'Детали' должно раскрываться модальное окно
    с информацией по источнику
    """)
    @allure.issue("https://tasks.ngrsoftlab.ru/browse/DAT-5410")
    @allure.testcase("https://team-6wwm.testit.software/projects/3/tests/2866")
    def test_open_modal_w_actions_details(self, browser):
        DataSourcesCase(browser).open_modal_w_actions_details()

    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Создание источника в редакторе'")
    def test_open_new_source_editor_by_steps(self, browser):
        DataSourcesCase(browser).open_new_source_editor_by_steps()

    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Подключение источника'")
    @allure.description("Подключить источник из коннектора")
    def test_open_new_source_connector_by_steps(self, browser):
        DataSourcesCase(browser).open_new_source_connector_by_steps()

    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Элементы навигации библиотека Шаблонов/Коннекторов")
    @allure.description("""
    Переход на страницу 'Библиотека коннекторов' используя UI элементы, со страницы 'Источники данных';
    Работа вкладок 'Коннекторы', 'Логотипы';
    Работа кнопок 'Создать коннектор', 'Создать логотип'
    Работа кнопки '<- Возврат', ( вернуться к Источникам данных )
    """)
    def test_library_connectors_navigation(self, browser):
        DataSourcesCase(browser).library_connectors_navigation()

    @pytest.mark.skip   # todo: сделать
    @allure.title("Создание источника в редакторе")
    @allure.description("Источники - создание источника в редакторе (тип подключения: syslog)")
    @allure.testcase("https://team-6wwm.testit.software/projects/3/tests/320")
    def test_source_create_editor_syslog(self, browser):
        DataSourcesCase(browser).source_create_editor_syslog()

    # https://team-6wwm.testit.software/projects/3/tests?isolatedSection=1ab5e96c-fcad-4238-bd9f-bb78f7d0e094


@allure.suite(SuiteName.DATA_SCRIPTS)
class TestDataScripts:

    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Скрипты'")
    @allure.description("Открыть страницу через боковое меню")
    def test_open_page_by_steps(self, browser):
        DataScriptsCase(browser).open_page_by_steps()


@allure.suite(SuiteName.DATA_STORAGE)
class TestDataStorage:

    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Хранилище'")
    def test_open_page_by_steps(self, browser):
        DataStorageCase(browser).open_page_by_steps()

    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Хранилище > переход по вкладкам")
    @allure.description("Проверка работы верхних вкладок \
    [Структура, Статистика, Поиск в Хранилище|по содержимому|по столбцам, Правила импорта]")
    def test_storage_navigation_tabs(self, browser):
        DataStorageCase(browser).storage_navigation_tabs()


@allure.suite(SuiteName.ANALYTICS_COMMON)
class TestAnalyticsMailing:

    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Рассылки'")
    @allure.description("""
    Переход на страницу, используя UI элементы;
    Работа вкладки 'Отчетов';
    Работа вкладки 'Новых данных'
    """)
    def test_open_page_by_steps(self, browser):
        MailingsCase(browser).open_page_by_steps()


@allure.suite(SuiteName.ANALYTICS_COMMON)
class TestAnalyticsReports:

    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Отчеты'")
    def test_open_page_by_steps(self, browser):
        ReportsCase(browser).open_page_by_steps()


@allure.suite(SuiteName.ANALYTICS_COMMON)
class TestAnalyticsVisualisation:

    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Визуализации'")
    def test_open_page_by_steps(self, browser):
        VisualisationCase(browser).open_page_by_steps()


@allure.suite(SuiteName.ANALYTICS_COMMON)
class TestAnalyticsQuery:

    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Запросы'")
    def test_open_page_by_steps(self, browser):
        QueriesCase(browser).open_page_by_steps()


@allure.suite(SuiteName.XBA_COMMON)
class TestXbaProfiles:

    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Профили xBA'")
    def test_open_page_by_steps(self, browser):
        XbaProfilesCase(browser).open_page_by_steps()


@allure.suite(SuiteName.XBA_COMMON)
class TestXbaMetaprofiles:

    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Метапрофили'")
    def test_open_page_by_steps(self, browser):
        XbaMetaprofilesCase(browser).open_page_by_steps()


@allure.suite(SuiteName.XBA_COMMON)
class TestXbaStatistics:

    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Статистика xBA'")
    def test_open_page_by_steps(self, browser):
        XbaStatisticsCase(browser).open_page_by_steps()


@allure.suite(SuiteName.ROLE_MINING_COMMON)
class TestRoleMiningSettings:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Настройки Role mining'")
    def test_open_page_by_steps(self, browser):
        RMSettingsCase(browser).open_page_by_steps()


@allure.suite(SuiteName.ROLE_MINING_COMMON)
class TestRoleMiningAD:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Состояние Active Directory'")
    def test_open_page_by_steps(self, browser):
        RMStateADCase(browser).open_page_by_steps()

    # TODO: работа вкладок Статистика | Рекомендации


@allure.suite(SuiteName.ROLE_MINING_COMMON)
class TestRoleMiningGroupsAndUsers:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Группы и пользователи Active Directory'")
    def test_open_page_by_steps(self, browser):
        RMGroupsAndUsersCase(browser).open_page_by_steps()


@allure.suite(SuiteName.ROLE_MINING_COMMON)
class TestRoleMiningRoleModel:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Ролевая модель'")
    def test_open_page_by_steps(self, browser):
        RMRoleModelCase(browser).open_page_by_steps()
