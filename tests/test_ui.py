import allure
import pytest

from resourses.credentials import TARGET_URL
from resourses.credentials import TestUsers
from resourses.constants import UI_AUTO_TEST_
from resourses.static_methods import get_str_random_num
from resourses.static_methods import get_random_string
from tests.case.api.peopler import PeoplerCase

from tests.case.ui import auth_ui
from tests.case.ui.m1_administration import roles_ui
from tests.case.ui.m1_administration import users_ui
from tests.case.ui.m1_administration import sessions_ui
from tests.case.ui.m1_administration import monitoring_ui
from tests.case.ui.m1_administration import license_ui
from tests.case.ui.m1_administration import updates_ui
from tests.case.ui.m1_administration import adm_notification_list_ui
from tests.case.ui.m1_administration import adm_settings_ui
from tests.case.ui.m2_data import scripts_ui
from tests.case.ui.m2_data import sources_ui
from tests.case.ui.m2_data import storage_ui
from tests.case.ui.m3_analytics import mailing_ui
from tests.case.ui.m3_analytics import report_ui
from tests.case.ui.m3_analytics import visualisation_ui
from tests.case.ui.m3_analytics import query_ui
from tests.case.ui.m4_xba import xba_profiles_ui
from tests.case.ui.m4_xba import xba_metaprofiles_ui
from tests.case.ui.m4_xba import xba_statistics_ui
from tests.case.ui.m5_RM import rm_groups_and_users_ui
from tests.case.ui.m5_RM import rm_settings_ui
from tests.case.ui.m5_RM import rm_state_ad_ui
from tests.case.ui.m5_RM import rm_role_model_ui


@pytest.fixture(autouse=True, scope='session')
def _print_debug_info():
    print("\n" + "="*42)
    print(f"TARGET_URL: {TARGET_URL}")
    print("="*42 + "\n")
    yield


class SuiteName:
    NAVIGATION = "Навигация"

    AUTH_PAGE_COMMON = "Страница Авторизации"
    AUTH_PAGE_AUTH = "Авторизация"
    AUTH_REGISTRATION = "Регистрация пользователя"

    ADMINISTRATION_COMMON = "Раздел Администрирование"
    ADMINISTRATION_USERS = "Пользователи"

    DATA_COMMON = "Раздел Данные"
    DATA_SOURCES = "Источники"
    DATA_SCRIPTS = "Скрипты"
    DATA_STORAGE = "Хранилище"

    ANALYTICS_COMMON = "Раздел Аналитика"

    XBA_COMMON = "Раздел xBA"

    ROLE_MINING_COMMON = "Раздел Role Mining"

    _SERVICE = "Служебные штуки"


@allure.suite(SuiteName.AUTH_PAGE_COMMON)
class TestAuth:

    @allure.sub_suite(SuiteName.AUTH_PAGE_AUTH)
    @allure.title("Авторизация valid")
    @allure.description("Самая обычная авторизация")
    @pytest.mark.parametrize('auth_data_ad', [TestUsers.DpQaa])
    def test_valid_auth(self, browser, auth_data_ad):
        auth_ui.valid_auth(browser, auth_data_ad)

    @allure.sub_suite(SuiteName.AUTH_PAGE_AUTH)
    @allure.title("Авторизация | Чекбокс | invalid")
    @allure.description("Проставлен чекбокс 'локально' для неЛокального пользователя")
    @pytest.mark.parametrize('auth_data_invalid', [{
        "username": TestUsers.DpQaa.get("username"),
        "password": TestUsers.DpQaa.get("password"),
        "local": True   # <- будет клик на чекбокс 'локально'
    }])
    def test_invalid_checkbox_auth(self, browser, auth_data_invalid):
        auth_ui.invalid_auth(browser, auth_data_invalid)

    @allure.sub_suite(SuiteName.AUTH_PAGE_AUTH)
    @allure.title("Авторизация | Неверный пароль | invalid")
    @allure.description("Попытка авторизации с неверным паролем")
    @pytest.mark.parametrize('auth_data_invalid', [{
        "username": TestUsers.DpQaa.get("username"),
        "password": TestUsers.DpQaa.get("password") + "mistake",
        "local": TestUsers.DpQaa.get("local")
    }])
    def test_invalid_password_auth(self, browser, auth_data_invalid):
        auth_ui.invalid_auth(browser, auth_data_invalid)

    @allure.sub_suite(SuiteName.AUTH_PAGE_AUTH)
    @allure.title("Авторизация | Локальный пользователь | valid")
    @allure.description("Самая обычная авторизация Локальный пользователь")
    @pytest.mark.parametrize('auth_data_local', [TestUsers.DpQaaLocal])
    def test_valid_auth_local(self, browser, auth_data_local):
        auth_ui.valid_auth(browser, auth_data_local)

    @allure.sub_suite(SuiteName.AUTH_PAGE_AUTH)
    @allure.title("Авторизация | Локальный пользователь | invalid")
    @allure.description("Авторизация Локальный пользователь с неверными логином и паролем")
    @pytest.mark.parametrize('auth_data_invalid', [{
        "username": 'test_invalid_username',
        "password": 'also_invalid@password',
        "local": True
    }])
    def test_invalid_auth_local(self, browser, auth_data_invalid):
        auth_ui.invalid_auth(browser, auth_data_invalid)

    @allure.sub_suite(SuiteName.AUTH_PAGE_AUTH)
    @allure.title("Авторизация | Локальный пользователь | Неправильный пароль")
    @allure.description("Авторизация Локальный пользователь с неверным паролем")
    @pytest.mark.parametrize('auth_data_wrong_password', [{
        "username": TestUsers.DpQaaLocal.get("username"),
        "password": 'but_there_is@invalid@password',
        "local": True
    }])
    def test_invalid_pass_auth_local(self, browser, auth_data_wrong_password):
        auth_ui.invalid_auth(browser, auth_data_wrong_password)

    @allure.sub_suite(SuiteName.AUTH_PAGE_AUTH)
    @allure.title("Авторизация | Локальный пользователь | Без чекбокса")
    @allure.description("Локальный пользователь, не проставил чекбокс 'local'")
    @pytest.mark.parametrize('auth_data_no_checkbox', [{
        "username": TestUsers.DpQaaLocal.get("username"),
        "password": TestUsers.DpQaaLocal.get("password"),
        "local": False  # <--не будет клика на чекбокс
    }])
    def test_invalid_cuz_no_checkbox_auth_local(self, browser, auth_data_no_checkbox):
        auth_ui.invalid_auth(browser, auth_data_no_checkbox)

    @allure.sub_suite(SuiteName.AUTH_PAGE_AUTH)
    @allure.title("Авторизация | Локальный пользователь | Невалидный логин")
    @allure.description("Локальный пользователь, пароль верный, но не логин")
    @pytest.mark.parametrize('auth_data_no_checkbox', [{
        "username": TestUsers.DpQaaLocal.get("username") + "mistake",
        "password": TestUsers.DpQaaLocal.get("password"),
        "local": True
    }])
    def test_invalid_login_auth_local(self, browser, auth_data_no_checkbox):
        auth_ui.invalid_auth(browser, auth_data_no_checkbox)

    @allure.sub_suite(SuiteName.AUTH_REGISTRATION)
    @allure.issue("https://tasks.ngrsoftlab.ru/browse/DAT-5762")
    @allure.testcase("http://testit.ngrsoftlab.ru/projects/2707/tests/2797")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Регистрация пользователя valid")
    @allure.description("Регистрация пользователя через форму регистрации на странице авторизации")
    @pytest.mark.parametrize('registration_data', [

        pytest.param(
            {
                "rusname":      "Прикольное Имя",
                "username":     f"{UI_AUTO_TEST_}{get_str_random_num()}",
                "password":     get_random_string(42, add_symbols="1234567809_-@"),
                "email":        "sample@liam.com",
                "mobile":       "9999999999",
                "department":   "Отдел",
                "title":        "Должность",
            },
            id = "sample",
        ),

        pytest.param(
            {
                "rusname":      "Прикольное Имя",
                "username":     f"{UI_AUTO_TEST_}{get_str_random_num()}",
                "password":     "a"*8,
                "email":        "sample@liam.com",
                "mobile":       "9999999999",
                "department":   "Отдел",
                "title":        "Должность",
            },
            id="min password length = 8",
        ),

        pytest.param(
            {
                "rusname":      "Прикольное Имя",
                "username":     f"{UI_AUTO_TEST_}{get_str_random_num()}",
                "password":     "m"*256,
                "email":        "sample@liam.com",
                "mobile":       "9999999999",
                "department":   "Отдел",
                "title":        "Должность",
            },
            id = "max password length = 256",
        ),

        pytest.param(
            {
                "rusname":      "Прикольное Имя",
                "username":     f"{UI_AUTO_TEST_}{get_str_random_num()}",
                "password":     get_random_string(42, add_symbols="_-@", uppercase=False, lowercase=False),
                "email":        "sample@liam.com",
                "mobile":       "9999999999",
                "department":   "Отдел",
                "title":        "Должность",
            },
            id="pass special symbols only '_-@'",
        ),

        pytest.param(
            {
                "rusname":      "Прикольное Имя",
                "username":     get_random_string(4),
                "password":     "12345678",
                "email":        "sample@liam.com",
                "mobile":       "9999999999",
                "department":   "Отдел",
                "title":        "Должность",
            },
            id="min username(login) length = 4",
        ),

        pytest.param(
            {
                "rusname":      "Прикольное Имя",
                "username":     get_random_string(256),
                "password":     "12345678",
                "email":        "sample@liam.com",
                "mobile":       "9999999999",
                "department":   "Отдел",
                "title":        "Должность",
            },
            id="max username(login) length = 256",
        ),

        pytest.param(
            {
                "rusname":      "Прикольное Имя",
                "username":     f"{UI_AUTO_TEST_}@._-" + get_random_string(10, add_symbols="._-@"),
                "password":     "12345678",
                "email":        "sample@liam.com",
                "mobile":       "9999999999",
                "department":   "Отдел",
                "title":        "Должность",
            },
            id="username(login) contains special symbols = '._-@'",
        ),
    ])
    def test_valid_registration(self, browser, registration_data):
        auth_ui.valid_registration(browser, registration_data)

    @allure.title("Авторизация | Выход из профиля пользователя")
    @allure.description("Выход по кнопке 'Выйти'")
    def test_log_out(self, browser):
        auth_ui.log_out(browser)


@allure.suite(SuiteName.ADMINISTRATION_COMMON)
class TestAdministrationRoles:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Роли'")
    def test_open_page_by_steps(self, browser):
        roles_ui.open_page_by_steps(browser)


@allure.suite(SuiteName.ADMINISTRATION_COMMON)
class TestAdministrationUsers:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Пользователи'")
    def test_open_page_by_steps(self, browser):
        users_ui.open_page_by_steps(browser)

    add_domain_user_test_rolename = "Офицер ИБ"

    @allure.sub_suite(SuiteName.ADMINISTRATION_USERS)
    @allure.title("Пользователи - добавление доменного пользователя")
    @allure.description("""
        Добавление доменного пользователя 
        через форму 'Добавить вручную'
        в разделе Администрирование > Пользователи
        """)
    @allure.issue("https://tasks.ngrsoftlab.ru/browse/DAT-5762")
    @allure.testcase("http://testit.ngrsoftlab.ru/projects/2707/tests/2787")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('registration_data', [

        pytest.param(
            {
                "username":     f"{UI_AUTO_TEST_}inner_add_{get_str_random_num()}",
                "role_name":    add_domain_user_test_rolename,
                "is_admin":     False,
                "is_system":    False,
                "is_tech":      False
            },
            id = "sample",
        ),

        pytest.param(
            {
                "username":     f"{UI_AUTO_TEST_}inner_add_{get_str_random_num()}",
                "role_name":    add_domain_user_test_rolename,
                "is_admin":     True,
                "is_system":    False,
                "is_tech":      False
            },
            id="checkbox 'is_admin' = True",
        ),

        pytest.param(
            {
                "username":     f"{UI_AUTO_TEST_}inner_add_{get_str_random_num()}",
                "role_name":    add_domain_user_test_rolename,
                "is_admin":     False,
                "is_system":    True,
                "is_tech":      False
            },
            id="checkbox 'is_system' = True",
        ),

        pytest.param(
            {
                "username":     f"{UI_AUTO_TEST_}inner_add_{get_str_random_num()}",
                "role_name":    add_domain_user_test_rolename,
                "is_admin":     False,
                "is_system":    False,
                "is_tech":      True
            },
            id="checkbox 'is_tech' = True",
        ),

        pytest.param(
            {
                "username":     f"{UI_AUTO_TEST_}inner_add_{get_str_random_num()}",
                "role_name":    add_domain_user_test_rolename,
                "is_admin":     True,
                "is_system":    True,
                "is_tech":      True
            },
            id="checkboxes 'is_admin,is_system,is_tech' = True",
        ),

        pytest.param(
            {
                "username":     f"{UI_AUTO_TEST_}inner_add_{get_str_random_num()}",
                "role_name":    add_domain_user_test_rolename,
                "is_admin":     True,
                "is_system":    True,
                "is_tech":      True
            },
            id="checkboxes 'is_admin,is_system,is_tech' = True",
        ),

        pytest.param(
            {
                "username":     get_random_string(4),
                "role_name":    add_domain_user_test_rolename,
                "is_admin":     False,
                "is_system":    False,
                "is_tech":      False
            },
            id="min username(login) length = 4"
        ),

        pytest.param(
            {
                "username":     get_random_string(256),
                "role_name":    add_domain_user_test_rolename,
                "is_admin":     False,
                "is_system":    False,
                "is_tech":      False
            },
            id="max username(login) length = 256",
            # marks=pytest.mark.skip  # look = no limits for max value
        ),

        pytest.param(
            {
                "username":     f"{UI_AUTO_TEST_}@._-" + get_random_string(10, add_symbols="._-@"),
                "role_name":    add_domain_user_test_rolename,
                "is_admin":     False,
                "is_system":    False,
                "is_tech":      False
            },
            id="username(login) contains special symbols = '._-@'",
        ),

    ])
    def test_add_domain_user(self, browser, registration_data):
        users_ui.add_domain_user(browser, registration_data)

        try:
            with allure.step("Удаление созданного пользователя"):
                parameter_username = dict(registration_data).get("username")
                expecting_username = users_ui.transform_username_to_domain_name(parameter_username)
                user_id = PeoplerCase().get_user_id_by_username(expecting_username)
                PeoplerCase().case_peopler_users_delete(user_id)
        except Exception as e:
            print(f"Exception: {e}")

    @allure.sub_suite(SuiteName.ADMINISTRATION_USERS)
    @allure.title("Пользователи - создание локального пользователя")
    @allure.description("""
        Добавление локального пользователя 
        через форму 'Добавить вручную'
        в разделе Администрирование > Пользователи
        """)
    @allure.issue("https://tasks.ngrsoftlab.ru/browse/DAT-5762")
    @allure.testcase("http://testit.ngrsoftlab.ru/projects/2707/tests/2778")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('registration_data', [

        pytest.param(
            {
                "rusname":      "Неприкольное Имя",
                "username":     f"{UI_AUTO_TEST_}inner_add_{get_str_random_num()}",
                "password":     get_random_string(42, add_symbols="1234567809_-@"),
                "email":        "sample@liam.com",
                "mobile":       "9999999999",
                "department":   "Отдел",
                "title":        "Должность",
            },
            id="sample",
        ),

        pytest.param(
            {
                "rusname":      "Неприкольное Имя",
                "username":     f"{UI_AUTO_TEST_}inner_add_{get_str_random_num()}",
                "password":     "b" * 8,
                "email":        "sample@liam.com",
                "mobile":       "9999999999",
                "department":   "Отдел",
                "title":        "Должность",
            },
            id="min password length = 8",
        ),

        pytest.param(
            {
                "rusname":      "Неприкольное Имя",
                "username":     f"{UI_AUTO_TEST_}inner_add_{get_str_random_num()}",
                "password":     "w" * 256,
                "email":        "sample@liam.com",
                "mobile":       "9999999999",
                "department":   "Отдел",
                "title":        "Должность",
            },
            id="max password length = 256",
        ),

        pytest.param(
            {
                "rusname":      "Неприкольное Имя",
                "username":     f"{UI_AUTO_TEST_}inner_add_{get_str_random_num()}",
                "password":     get_random_string(42, add_symbols="_-@", uppercase=False, lowercase=False),
                "email":        "sample@liam.com",
                "mobile":       "9999999999",
                "department":   "Отдел",
                "title":        "Должность",
            },
            id="pass special symbols only '_-@'",
        ),

        pytest.param(
            {
                "rusname":      "Неприкольное Имя",
                "username":     get_random_string(4),
                "password":     "12345678",
                "email":        "sample@liam.com",
                "mobile":       "9999999999",
                "department":   "Отдел",
                "title":        "Должность",
            },
            id="min username(login) length = 4",
        ),

        pytest.param(
            {
                "rusname":      "Неприкольное Имя",
                "username":     get_random_string(256),
                "password":     "12345678",
                "email":        "sample@liam.com",
                "mobile":       "9999999999",
                "department":   "Отдел",
                "title":        "Должность",
            },
            id="max username(login) length = 256",
        ),

        pytest.param(
            {
                "rusname":      "Прикольное Имя",
                "username":     f"{UI_AUTO_TEST_}inner_add_@._-" + get_random_string(10, add_symbols="._-@"),
                "password":     "12345678",
                "email":        "sample@liam.com",
                "mobile":       "9999999999",
                "department":   "Отдел",
                "title":        "Должность",
            },
            id="username(login) contains special symbols = '._-@'",
        ),

    ])
    def test_add_local_user(self, browser, registration_data):
        users_ui.add_local_user(browser, registration_data)

        try:
            with allure.step("Удаление созданного пользователя"):
                expecting_username = dict(registration_data).get("username")
                user_id = PeoplerCase().get_user_id_by_username(expecting_username)
                PeoplerCase().case_peopler_users_delete(user_id)
        except Exception as e:
            print(f"Exception: {e}")


@allure.suite(SuiteName.ADMINISTRATION_COMMON)
class TestAdministrationSessions:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Сессии'")
    def test_open_page_by_steps(self, browser):
        sessions_ui.open_page_by_steps(browser)


@allure.suite(SuiteName.ADMINISTRATION_COMMON)
class TestAdministrationMonitoring:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Мониторинг'")
    def test_open_page_by_steps(self, browser):
        monitoring_ui.open_page_by_steps(browser)


@allure.suite(SuiteName.ADMINISTRATION_COMMON)
class TestAdministrationLicense:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Лицензии'")
    def test_open_page_by_steps(self, browser):
        license_ui.open_page_by_steps(browser)


@allure.suite(SuiteName.ADMINISTRATION_COMMON)
class TestAdministrationUpdates:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Обновление'")
    @allure.description("""
    Переход на страницу, используя UI элементы;
    Работа вкладки 'Версии компонентов';
    Работа вкладки 'Дополнения'
    """)
    def test_open_page_by_steps(self, browser):
        updates_ui.open_page_by_steps(browser)


@allure.suite(SuiteName.ADMINISTRATION_COMMON)
class TestAdministrationNotificationList:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Журнал уведомлений'")
    def test_open_page_by_steps(self, browser):
        adm_notification_list_ui.open_page_by_steps(browser)


@allure.suite(SuiteName.ADMINISTRATION_COMMON)
class TestAdministrationSettings:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Настройки'")
    @allure.description("""
    Переход на страницу, используя UI элементы;
    Работа вкладок;
    """)
    def test_open_page_by_steps(self, browser):
        adm_settings_ui.open_page_by_steps(browser)


@allure.suite(SuiteName.DATA_COMMON)
class TestDataSources:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Источники'")
    @allure.description("Открыть страницу через боковое меню")
    def test_open_page_by_steps(self, browser):
        sources_ui.open_page_by_steps(browser)

    @allure.sub_suite(SuiteName.DATA_SOURCES)
    @allure.title("Открыть модальное окно 'Детали'")
    @allure.description("""
    На странице 'Источники' в колонке 'Действие',
    при нажатии на кнопку 'Детали' должно раскрываться модальное окно
    с информацией по источнику
    """)
    @allure.issue("https://tasks.ngrsoftlab.ru/browse/DAT-5410")
    @allure.testcase("http://testit.ngrsoftlab.ru/projects/2707/tests/2711")
    def test_open_modal_w_actions_details(self, browser):
        sources_ui.open_modal_w_actions_details(browser)

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Создание источника в редакторе'")
    def test_open_new_source_editor_by_steps(self, browser):
        sources_ui.open_new_source_editor_by_steps(browser)

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Подключение источника'")
    @allure.description("Подключить источник из коннектора")
    def test_open_new_source_connector_by_steps(self, browser):
        sources_ui.open_new_source_connector_by_steps(browser)

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Элементы навигации библиотека Шаблонов/Коннекторов")
    @allure.description("""
    Переход на страницу 'Библиотека коннекторов' используя UI элементы, со страницы 'Источники данных';
    Работа вкладок 'Коннекторы', 'Логотипы';
    Работа кнопок 'Создать коннектор', 'Создать логотип'
    Работа кнопки '<- Возврат', ( вернуться к Источникам данных )
    """)
    def test_library_connectors_navigation(self, browser):
        sources_ui.library_connectors_navigation(browser)

    @pytest.mark.skip   # todo: сделать
    @allure.sub_suite(SuiteName.DATA_SOURCES)
    @allure.title("Создание источника в редакторе")
    @allure.description("Источники - создание источника в редакторе (тип подключения: syslog)")
    @allure.testcase("")
    def test_source_create_editor_syslog(self, browser):
        sources_ui.source_create_editor_syslog(browser)


@allure.suite(SuiteName.DATA_COMMON)
class TestDataScripts:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Скрипты'")
    @allure.description("Открыть страницу через боковое меню")
    def test_open_page_by_steps(self, browser):
        scripts_ui.open_page_by_steps(browser)


@allure.suite(SuiteName.DATA_COMMON)
class TestDataStorage:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Хранилище'")
    def test_open_page_by_steps(self, browser):
        storage_ui.open_page_by_steps(browser)

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Хранилище > переход по вкладкам")
    @allure.description("Проверка работы верхних вкладок \
    [Структура, Статистика, Поиск в Хранилище|по содержимому|по столбцам, Правила импорта]")
    def test_storage_navigation_tabs(self, browser):
        storage_ui.storage_navigation_tabs(browser)


@allure.suite(SuiteName.ANALYTICS_COMMON)
class TestAnalyticsMailing:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Рассылки'")
    @allure.description("""
    Переход на страницу, используя UI элементы;
    Работа вкладки 'Отчетов';
    Работа вкладки 'Новых данных'
    """)
    def test_open_page_by_steps(self, browser):
        mailing_ui.open_page_by_steps(browser)


@allure.suite(SuiteName.ANALYTICS_COMMON)
class TestAnalyticsReports:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Отчеты'")
    def test_open_page_by_steps(self, browser):
        report_ui.open_page_by_steps(browser)


@allure.suite(SuiteName.ANALYTICS_COMMON)
class TestAnalyticsVisualisation:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Визуализации'")
    def test_open_page_by_steps(self, browser):
        visualisation_ui.open_page_by_steps(browser)


@allure.suite(SuiteName.ANALYTICS_COMMON)
class TestAnalyticsQuery:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Запросы'")
    def test_open_page_by_steps(self, browser):
        query_ui.open_page_by_steps(browser)


@allure.suite(SuiteName.XBA_COMMON)
class TestXbaProfiles:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Профили xBA'")
    def test_open_page_by_steps(self, browser):
        xba_profiles_ui.open_page_by_steps(browser)


@allure.suite(SuiteName.XBA_COMMON)
class TestXbaMetaprofiles:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Метапрофили'")
    def test_open_page_by_steps(self, browser):
        xba_metaprofiles_ui.open_page_by_steps(browser)


@allure.suite(SuiteName.XBA_COMMON)
class TestXbaStatistics:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Статистика xBA'")
    def test_open_page_by_steps(self, browser):
        xba_statistics_ui.open_page_by_steps(browser)


@allure.suite(SuiteName.ROLE_MINING_COMMON)
class TestRoleMiningSettings:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Настройки Role mining'")
    def test_open_page_by_steps(self, browser):
        rm_settings_ui.open_page_by_steps(browser)

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Настройки Role mining - работа вкладок навигации")
    @allure.description("Работа вкладок 'Источники' | 'Настройка расчета'")
    def test_rm_settings_navigation_tabs(self, browser):
        rm_settings_ui.rm_settings_navigation_tabs(browser)


@allure.suite(SuiteName.ROLE_MINING_COMMON)
class TestRoleMiningStateAD:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Состояние Active Directory'")
    def test_open_page_by_steps(self, browser):
        rm_state_ad_ui.open_page_by_steps(browser)

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Состояние Active Directory - работа вкладок навигации")
    @allure.description("Работа вкладок 'Статистика'|'Рекомендации'")
    def test_rm_state_ad_navigation_tabs(self, browser):
        rm_state_ad_ui.rm_state_ad_navigation_tabs(browser)


@allure.suite(SuiteName.ROLE_MINING_COMMON)
class TestRoleMiningGroupsAndUsers:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Группы и пользователи Active Directory'")
    def test_open_page_by_steps(self, browser):
        rm_groups_and_users_ui.open_page_by_steps(browser)

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Группы и пользователи Active Directory - работа вкладок навигации")
    @allure.description("Работа вкладок 'Группы'|'Пользователи'")
    def test_rm_groups_and_users_navigation_tabs(self, browser):
        rm_groups_and_users_ui.navigation_tabs(browser)


@allure.suite(SuiteName.ROLE_MINING_COMMON)
class TestRoleMiningRoleModel:

    @allure.sub_suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Ролевая модель'")
    def test_open_page_by_steps(self, browser):
        rm_role_model_ui.open_page_by_steps(browser)


@allure.suite(SuiteName._SERVICE)
class TestGarbageCollector2:

    def test_delete_my_right_leg(self):
        # удаление пользователей с приставкой в имени
        PeoplerCase().all_users_with_prefix_delete(UI_AUTO_TEST_)
