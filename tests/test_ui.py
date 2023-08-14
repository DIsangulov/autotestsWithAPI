import allure
import pytest

from resourses.credentials import TestUsers

from pages.UI._0_Auth.auth_page import AuthPage
from pages.UI._3_Analytics.an_mailing_lists import MailingLists
from pages.UI._3_Analytics.an_reports import Reports
from pages.UI._3_Analytics.an_requests import Requests
from pages.UI._3_Analytics.an_visualization import Visualisation
from pages.UI._4_xBA.xba_metaprofiles import Metaprofiles
from pages.UI._4_xBA.xba_profiles import Profiles
from pages.UI._4_xBA.xba_statistic import Statistic
from pages.UI._5_RoleMining.rm_settings import RmSettings
from pages.UI._5_RoleMining.rm_ad_status import AdStatus

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


class SuiteName:
    NAVIGATION = "Навигация"


@allure.suite("Страница Авторизации")
@allure.issue("https://tasks.ngrsoftlab.ru/browse/QA-198")
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


@allure.title("Администрирование > Роли")
class TestAdministrationRoles:
    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Роли'")
    def test_open_page_by_steps(self, browser):
        RolesCase(browser).open_page_by_steps()


@allure.title("Администрирование > Пользователи")
class TestAdministrationUsers:
    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Пользователи'")
    def test_open_page_by_steps(self, browser):
        UsersCase(browser).open_page_by_steps()


@allure.title("Администрирование > Сессии")
class TestAdministrationSessions:
    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Сессии'")
    def test_open_page_by_steps(self, browser):
        SessionsCase(browser).open_page_by_steps()


@allure.title("Администрирование > Мониторинг")
class TestAdministrationMonitoring:
    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Мониторинг'")
    def test_open_page_by_steps(self, browser):
        MonitoringCase(browser).open_page_by_steps()


@allure.title("Администрирование > Лицензии")
class TestAdministrationLicense:
    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Лицензии'")
    def test_open_page_by_steps(self, browser):
        LicenseCase(browser).open_page_by_steps()


@allure.title("Администрирование > Обновление")
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


@allure.title("Администрирование > Журнал уведомлений")
class TestAdministrationNotificationList:
    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Журнал уведомлений'")
    def test_open_page_by_steps(self, browser):
        AdmNotificationListCase(browser).open_page_by_steps()


@allure.title("Администрирование > Настройки")
class TestAdministrationSettings:
    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Настройки'")
    @allure.description("""
    Переход на страницу, используя UI элементы;
    Работа вкладок;
    """)
    def test_open_page_by_steps(self, browser):
        AdmSettingsCase(browser).open_page_by_steps()


@allure.suite("Данные > Источники")
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

    # todo: 301
    # todo: 316
    # todo: 459
    # todo: 549
    # todo: 159
    # todo: 531 ?

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


@allure.suite("Данные > Скрипты")
class TestDataScripts:

    @allure.suite(SuiteName.NAVIGATION)
    @allure.title("Переход на страницу 'Скрипты'")
    @allure.description("Открыть страницу через боковое меню")
    def test_open_page_by_steps(self, browser):
        DataScriptsCase(browser).open_page_by_steps()


@allure.suite("Данные > Хранилище")
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


@pytest.mark.skip
class TestAnalytics:  # Аналитика
    def test_open_an_mailing_lists_reports(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_should_enter_an_mailing_lists_reports_be_successful(self, browser):
        page = MailingLists(browser)
        page.should_enter_an_mailing_lists_reports_be_successful()

    def test_open_an_reports(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_should_enter_an_reports_be_successful(self, browser):
        page = Reports(browser)
        page.should_enter_an_reports_be_successful()

    def test_open_an_visualisation(self, browser):
        page = Visualisation(browser)
        page.open_an_visualisation()

    def test_should_enter_an_visualisation_be_successful(self, browser):
        page = Visualisation(browser)
        page.should_enter_an_visualisation_be_successful()

    def test_open_an_requests(self, browser):
        page = Requests(browser)
        page.open_an_requests()

    def test_should_enter_an_requests_be_successful(self, browser):
        page = Requests(browser)
        page.should_enter_an_requests_be_successful()


@pytest.mark.skip
class TestXBA:

    def test_open_xba_profiles(self, browser):
        page = Profiles(browser)
        page.open_xba_profiles()

    def test_should_enter_xba_profiles_be_successful(self, browser):
        page = Profiles(browser)
        page.should_enter_xba_profiles_be_successful()

    def test_open_xba_metaprofiles(self, browser):
        page = Metaprofiles(browser)
        page.open_xba_metaprofiles()

    def test_should_enter_xba_metaprofiles_be_successful(self, browser):
        page = Metaprofiles(browser)
        page.should_enter_xba_metaprofiles_be_successful()

    def test_open_xba_statistic(self, browser):
        page = Statistic(browser)
        page.open_xba_statistic()

    def test_should_enter_xba_statistic_be_successful(self, browser):
        page = Statistic(browser)
        page.should_enter_xba_statistic_be_successful()


@pytest.mark.skip
class TestRoleMining:

    def test_open_rm_ad_status_statistic(self, browser):
        page = AdStatus(browser)
        page.open_rm_ad_status_statistic()

    def test_should_enter_rm_ad_status_statistic_be_successful(self, browser):
        page = AdStatus(browser)
        page.should_enter_rm_ad_status_statistic_be_successful()

    def test_open_rm_ad_status_recommendation(self, browser):
        page = AdStatus(browser)
        page.open_rm_ad_status_recommendation()

    def test_should_enter_rm_ad_status_recommendation_be_successful(self, browser):
        page = AdStatus(browser)
        page.should_enter_rm_ad_status_recommendation_be_successful()


@pytest.mark.skip
class TestRoleMiningSettingsSources:

    def test_role_mining_settings_page(self, browser):
        page = RmSettings(browser)
        page.open_rm_settings_sources()
        page.clear_sources_rm_settings()
        page.not_confirm_cleaning_rm_settings()
        page.clear_sources_rm_settings()
        page.confirm_cleaning_rm_settings()
        page.selecting_values_from_dropdown_list()
        page.should_sources_saved()
        page.should_sources_recalculated()
        page.calculation_settings()


@pytest.mark.skip
class TestRoleMiningActiveDirectory:

    def test_mailing_anomaly_rm_tcp(self, browser):
        page = AdStatus(browser)
        page.open_rm_ad_status_statistic()
        page.should_enter_rm_ad_status_statistic_be_successful()
        page.open_rm_ad_status_recommendation()
        page.should_enter_rm_ad_status_recommendation_be_successful()
        page.configuring_anomaly_distribution()
        page.input_server_address_and_port()
        page.select_tcp_exchange_protocol()
        page.click_add_button()
        page.should_tcp_distribution_protocol_save_sucsess()
        page.delete_last_entry()
        page.close_window()

    def test_mailing_anomaly_rm_udp(self, browser):
        page = AdStatus(browser)
        page.configuring_anomaly_distribution()
        page.input_server_address_and_port()
        page.select_udp_exchange_protocol()
        page.click_add_button()
        page.should_udp_distribution_protocol_save_sucsess()
        page.delete_last_entry()
        page.close_window()


@pytest.mark.skip
@allure.title('Отчеты - проверка отображения отчета со статусом "Не опубликован+Закрыт"')
class TestAnalyticsReportsNotPublishedClosed:  # Отчеты - проверка отображения отчета со статусом "Не опубликован+Закрыт"

    def test_open_an_mailing_lists_reports(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_should_enter_an_reports_be_successful(self, browser):
        page = Reports(browser)
        page.should_enter_an_reports_be_successful()

    def test_create_new_report(self, browser):
        page = Reports(browser)
        page.create_new_report()

    def test_log_out(self, browser):
        page = AuthPage(browser)
        page.log_out()

    def test_enter_as_local_user(self, browser):
        page = AuthPage(browser)
        page.enter_as_local_user()

    def test_open_an_mailing_lists_reports_as_local_user(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports_as_local_user(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_should_report_not_visible(self, browser):
        page = Reports(browser)
        page.should_report_not_visible()


@pytest.mark.skip
@allure.title('Отчеты - проверка отображения отчета со статусом "Опубликован+Закрыт"')
class TestAnalyticsReportsPublishedClosed:  # Отчеты - проверка отображения отчета со статусом "Опубликован+Закрыт"

    def test_open_an_mailing_lists_reports(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_should_enter_an_reports_be_successful(self, browser):
        page = Reports(browser)
        page.should_enter_an_reports_be_successful()

    def test_create_new_report(self, browser):
        page = Reports(browser)
        page.create_new_report()

    def test_do_report_public(self, browser):
        page = Reports(browser)
        page.do_report_public()

    def test_log_out(self, browser):
        page = AuthPage(browser)
        page.log_out()

    def test_enter_as_local_user(self, browser):
        page = AuthPage(browser)
        page.enter_as_local_user()

    def test_open_an_mailing_lists_reports_as_local_user(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports_as_local_user(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_open_last_report(self, browser):
        page = Reports(browser)
        page.open_last_report()

    def test_should_edit_button_not_available(self, browser):
        page = Reports(browser)
        page.should_edit_button_not_available()

    def test_should_access_settings_not_available_for_public_report(self, browser):
        page = Reports(browser)
        page.should_access_settings_not_available_for_public_report()

    def test_should_role_added_not_available(self, browser):
        page = Reports(browser)
        page.should_role_added_not_available()


@pytest.mark.skip
@allure.title('Отчеты - проверка отображения отчета со статусом "Опубликован+Открыт"')
class TestAnalyticsReportsPublishedOpen:  # Отчеты - проверка отображения отчета со статусом "Опубликован+Открыт"

    def test_open_an_mailing_lists_reports(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_should_enter_an_reports_be_successful(self, browser):
        page = Reports(browser)
        page.should_enter_an_reports_be_successful()

    def test_create_new_report(self, browser):
        page = Reports(browser)
        page.create_new_report()

    def test_do_report_public(self, browser):
        page = Reports(browser)
        page.do_report_public()

    def test_do_report_open(self, browser):
        page = Reports(browser)
        page.do_report_open()

    def test_log_out(self, browser):
        page = AuthPage(browser)
        page.log_out()

    def test_enter_as_local_user(self, browser):
        page = AuthPage(browser)
        page.enter_as_local_user()

    def test_open_an_mailing_lists_reports_as_local_user(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports_as_local_user(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_open_last_report(self, browser):
        page = Reports(browser)
        page.open_last_report()

    def test_should_edit_button_not_available(self, browser):
        page = Reports(browser)
        page.should_edit_button_not_available()

    def test_should_access_settings_not_available_for_public_report(self, browser):
        page = Reports(browser)
        page.should_access_settings_not_available_for_public_report()

    def test_should_role_added_not_available(self, browser):
        page = Reports(browser)
        page.should_role_added_not_available()


@pytest.mark.skip
@allure.title('Отчеты - установка доступа к отчету для роли на "Чтение"')
class TestSettingReportAccessForRoleToRead:

    def test_open_an_mailing_lists_reports(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_should_enter_an_reports_be_successful(self, browser):
        page = Reports(browser)
        page.should_enter_an_reports_be_successful()

    def test_create_new_report(self, browser):
        page = Reports(browser)
        page.create_new_report()

    def test_role_add_read(self, browser):
        page = Reports(browser)
        page.role_add_read()

    def test_log_out(self, browser):
        page = AuthPage(browser)
        page.log_out()

    def test_enter_as_local_user(self, browser):
        page = AuthPage(browser)
        page.enter_as_local_user()

    def test_open_an_mailing_lists_reports_as_local_user(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports_as_local_user(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_open_last_report(self, browser):
        page = Reports(browser)
        page.open_last_report()

    def test_should_edit_button_not_available(self, browser):
        page = Reports(browser)
        page.should_edit_button_not_available()

    def test_should_access_settings_not_available(self, browser):
        page = Reports(browser)
        page.should_access_settings_not_available_for_not_public_report()

    def test_should_role_added_not_available(self, browser):
        page = Reports(browser)
        page.should_role_added_not_available()

    def test_should_checkbox_read_enable(self, browser):
        page = Reports(browser)
        page.should_checkbox_read_enable()


@pytest.mark.skip
@allure.title('Отчеты - установка доступа к отчету для роли на "Запись"')
class TestSettingReportAccessForRoleToWrite:

    def test_open_an_mailing_lists_reports(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_should_enter_an_reports_be_successful(self, browser):
        page = Reports(browser)
        page.should_enter_an_reports_be_successful()

    def test_create_new_report(self, browser):
        page = Reports(browser)
        page.create_new_report()

    def test_role_add_write(self, browser):
        page = Reports(browser)
        page.role_add_write()

    def test_log_out(self, browser):
        page = AuthPage(browser)
        page.log_out()

    def test_enter_as_local_user(self, browser):
        page = AuthPage(browser)
        page.enter_as_local_user()

    def test_open_an_mailing_lists_reports_as_local_user(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports_as_local_user(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_open_last_report(self, browser):
        page = Reports(browser)
        page.open_last_report()

    def test_should_edit_button_available(self, browser):
        page = Reports(browser)
        page.should_edit_button_available()

    def test_should_access_settings_not_available(self, browser):
        page = Reports(browser)
        page.should_access_settings_not_available_for_not_public_report()

    def test_should_role_added_not_available(self, browser):
        page = Reports(browser)
        page.should_role_added_not_available()

    def test_should_checkbox_write_enable(self, browser):
        page = Reports(browser)
        page.should_checkbox_write_enable()


@pytest.mark.skip
@allure.title('Отчеты - установка доступа к отчету для роли на "Выполнение"')
class TestSettingReportAccessForRoleToExecute:

    def test_open_an_mailing_lists_reports(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_should_enter_an_reports_be_successful(self, browser):
        page = Reports(browser)
        page.should_enter_an_reports_be_successful()

    def test_create_new_report(self, browser):
        page = Reports(browser)
        page.create_new_report()

    def test_role_add_execute(self, browser):
        page = Reports(browser)
        page.role_add_execute()

    def test_log_out(self, browser):
        page = AuthPage(browser)
        page.log_out()

    def test_enter_as_local_user(self, browser):
        page = AuthPage(browser)
        page.enter_as_local_user()

    def test_open_an_mailing_lists_reports_as_local_user(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports_as_local_user(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_open_last_report(self, browser):
        page = Reports(browser)
        page.open_last_report()

    def test_should_edit_button_not_available(self, browser):
        page = Reports(browser)
        page.should_edit_button_available()

    def test_should_access_settings_not_available(self, browser):
        page = Reports(browser)
        page.should_access_settings_not_available_for_not_public_report()

    def test_should_role_added_not_available(self, browser):
        page = Reports(browser)
        page.should_role_added_not_available()

    def test_should_checkbox_execute_enable(self, browser):
        page = Reports(browser)
        page.should_checkbox_execute_enable()


@pytest.mark.skip
@allure.title('Отчеты - установка доступа к отчету для роли на "Настройка доступа"')
class TestSettingReportAccessForRoleToAccessSettings:

    def test_open_an_mailing_lists_reports(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_should_enter_an_reports_be_successful(self, browser):
        page = Reports(browser)
        page.should_enter_an_reports_be_successful()

    def test_create_new_report(self, browser):
        page = Reports(browser)
        page.create_new_report()

    def test_role_add_access_settings(self, browser):
        page = Reports(browser)
        page.role_add_access_settings()

    def test_log_out(self, browser):
        page = AuthPage(browser)
        page.log_out()

    def test_enter_as_local_user(self, browser):
        page = AuthPage(browser)
        page.enter_as_local_user()

    def test_open_an_mailing_lists_reports_as_local_user(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports_as_local_user(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_open_last_report(self, browser):
        page = Reports(browser)
        page.open_last_report()

    def test_should_edit_button_available(self, browser):
        page = Reports(browser)
        page.should_edit_button_available()

    def test_should_access_settings_not_available(self, browser):
        page = Reports(browser)
        page.should_access_settings_not_available_for_not_public_report()

    def test_should_role_added_available(self, browser):
        page = Reports(browser)
        page.should_role_added_available()

    def test_should_checkbox_access_settings_enable(self, browser):
        page = Reports(browser)
        page.should_checkbox_access_settings_enable()


@pytest.mark.skip
@allure.title('Отчеты - установка доступа к отчету для пользователя на "Чтение"')
class TestSettingReportAccessForUserToRead:

    def test_open_an_mailing_lists_reports(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_should_enter_an_reports_be_successful(self, browser):
        page = Reports(browser)
        page.should_enter_an_reports_be_successful()

    def test_create_new_report(self, browser):
        page = Reports(browser)
        page.create_new_report()

    def test_switch_users_tab(self, browser):
        page = Reports(browser)
        page.switch_users_tab()

    def test_user_add_read(self, browser):
        page = Reports(browser)
        page.user_add_read()

    def test_log_out(self, browser):
        page = AuthPage(browser)
        page.log_out()

    def test_enter_as_local_user(self, browser):
        page = AuthPage(browser)
        page.enter_as_local_user()

    def test_open_an_mailing_lists_reports_as_local_user(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports_as_local_user(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_open_last_report(self, browser):
        page = Reports(browser)
        page.open_last_report()

    def test_should_edit_button_not_available(self, browser):
        page = Reports(browser)
        page.should_edit_button_not_available()

    def test_should_access_settings_not_available(self, browser):
        page = Reports(browser)
        page.should_access_settings_not_available_for_not_public_report()

    def test_should_user_added_not_available(self, browser):
        page = Reports(browser)
        page.should_user_added_not_available()

    def test_should_checkbox_read_enable_for_users_tab(self, browser):
        page = Reports(browser)
        page.should_checkbox_read_enable_for_users_tab()


@pytest.mark.skip
@allure.title('Отчеты - установка доступа к отчету для пользователя на "Запись"')
class TestSettingReportAccessForUserToWrite:

    def test_open_an_mailing_lists_reports(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_should_enter_an_reports_be_successful(self, browser):
        page = Reports(browser)
        page.should_enter_an_reports_be_successful()

    def test_create_new_report(self, browser):
        page = Reports(browser)
        page.create_new_report()

    def test_switch_users_tab(self, browser):
        page = Reports(browser)
        page.switch_users_tab()

    def test_user_add_write(self, browser):
        page = Reports(browser)
        page.user_add_write()

    def test_log_out(self, browser):
        page = AuthPage(browser)
        page.log_out()

    def test_enter_as_local_user(self, browser):
        page = AuthPage(browser)
        page.enter_as_local_user()

    def test_open_an_mailing_lists_reports_as_local_user(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports_as_local_user(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_open_last_report(self, browser):
        page = Reports(browser)
        page.open_last_report()

    def test_should_edit_button_available(self, browser):
        page = Reports(browser)
        page.should_edit_button_available()

    def test_should_access_settings_not_available(self, browser):
        page = Reports(browser)
        page.should_access_settings_not_available_for_not_public_report()

    def test_should_user_added_not_available(self, browser):
        page = Reports(browser)
        page.should_user_added_not_available()

    def test_should_checkbox_write_enable_for_users_tab(self, browser):
        page = Reports(browser)
        page.should_checkbox_write_enable_for_users_tab()


@pytest.mark.skip
@allure.title('Отчеты - установка доступа к отчету для пользователя на "Выполнение"')
class TestSettingReportAccessForUserToExecute:

    def test_open_an_mailing_lists_reports(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_should_enter_an_reports_be_successful(self, browser):
        page = Reports(browser)
        page.should_enter_an_reports_be_successful()

    def test_create_new_report(self, browser):
        page = Reports(browser)
        page.create_new_report()

    def test_switch_users_tab(self, browser):
        page = Reports(browser)
        page.switch_users_tab()

    def test_user_add_execute(self, browser):
        page = Reports(browser)
        page.user_add_execute()

    def test_log_out(self, browser):
        page = AuthPage(browser)
        page.log_out()

    def test_enter_as_local_user(self, browser):
        page = AuthPage(browser)
        page.enter_as_local_user()

    def test_open_an_mailing_lists_reports_as_local_user(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports_as_local_user(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_open_last_report(self, browser):
        page = Reports(browser)
        page.open_last_report()

    def test_should_edit_button_available(self, browser):
        page = Reports(browser)
        page.should_edit_button_available()

    def test_should_access_settings_not_available(self, browser):
        page = Reports(browser)
        page.should_access_settings_not_available_for_not_public_report()

    def test_should_user_added_not_available(self, browser):
        page = Reports(browser)
        page.should_user_added_not_available()

    def test_should_checkbox_execute_enable_for_users_tab(self, browser):
        page = Reports(browser)
        page.should_checkbox_execute_enable_for_users_tab()


@pytest.mark.skip
@allure.title('Отчеты - установка доступа к отчету для пользователя на "Настройку доступа"')
class TestSettingReportAccessForUserToAccessSettings:

    def test_open_an_mailing_lists_reports(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_should_enter_an_reports_be_successful(self, browser):
        page = Reports(browser)
        page.should_enter_an_reports_be_successful()

    def test_create_new_report(self, browser):
        page = Reports(browser)
        page.create_new_report()

    def test_switch_users_tab(self, browser):
        page = Reports(browser)
        page.switch_users_tab()

    def test_user_add_access_settings(self, browser):
        page = Reports(browser)
        page.user_add_access_settings()

    def test_log_out(self, browser):
        page = AuthPage(browser)
        page.log_out()

    def test_enter_as_local_user(self, browser):
        page = AuthPage(browser)
        page.enter_as_local_user()

    def test_open_an_mailing_lists_reports_as_local_user(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports_as_local_user(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_open_last_report(self, browser):
        page = Reports(browser)
        page.open_last_report()

    def test_should_edit_button_available(self, browser):
        page = Reports(browser)
        page.should_edit_button_available()

    def test_should_access_settings_not_available(self, browser):
        page = Reports(browser)
        page.should_access_settings_not_available_for_not_public_report()

    def test_should_user_added_available(self, browser):
        page = Reports(browser)
        page.should_user_added_available()

    def test_should_checkbox_access_settings_enable_for_users_tab(self, browser):
        page = Reports(browser)
        page.should_checkbox_access_settings_enable_for_users_tab()


@pytest.mark.skip
@allure.title('Отчеты - удаление доступа к отчету для пользователя, роль которого имеет доступ на "Выполнение"')
class TestDeleteAccessReportForUserWhoseRoleHasAccessExecute:

    def test_open_an_mailing_lists_reports(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_should_enter_an_reports_be_successful(self, browser):
        page = Reports(browser)
        page.should_enter_an_reports_be_successful()

    def test_create_new_report(self, browser):
        page = Reports(browser)
        page.create_new_report()

    def test_switch_users_tab(self, browser):
        page = Reports(browser)
        page.switch_users_tab()

    def test_user_add_execute(self, browser):
        page = Reports(browser)
        page.user_add_execute()

    def test_log_out(self, browser):
        page = AuthPage(browser)
        page.log_out()

    def test_enter_as_local_user(self, browser):
        page = AuthPage(browser)
        page.enter_as_local_user()

    def test_open_an_mailing_lists_reports_as_local_user(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports_as_local_user(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_open_last_report(self, browser):
        page = Reports(browser)
        page.save_last_report_name()
        page.open_last_report()

    def test_should_edit_button_not_available(self, browser):
        page = Reports(browser)
        page.should_edit_button_not_available()

    def test_should_access_settings_not_available(self, browser):
        page = Reports(browser)
        page.should_access_settings_not_available_for_not_public_report()

    def test_should_user_added_not_available(self, browser):
        page = Reports(browser)
        page.should_user_added_not_available()

    def test_should_checkbox_execute_enable_for_users_tab(self, browser):
        page = Reports(browser)
        page.should_checkbox_execute_enable_for_users_tab()

    def test_log_out_by_local_user(self, browser):
        page = AuthPage(browser)
        page.log_out()

    # def test_valid_auth_second_iteration_by_main_user(self, browser):
    #     page = AuthPage(browser)
    #     page.open()
    #     page.enter_as_user()

    def test_open_an_mailing_lists_reports_second_iteration(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports_second_iteration(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_save_last_report_name(self, browser):
        page = Reports(browser)
        page.save_last_report_name()

    def test_open_last_report_second_iteration(self, browser):
        page = Reports(browser)
        page.open_last_report()

    def test_open_access_settings_and_switch_to_user_tab(self, browser):
        page = Reports(browser)
        page.open_access_settings()
        page.switch_users_tab()

    def test_uncheck_checkboxes_r_w_e(self, browser):
        page = Reports(browser)
        page.uncheck_checkboxes_r_w_e()

    def test_log_out_second_iteration(self, browser):
        page = AuthPage(browser)
        page.log_out()

    def test_enter_as_local_user_second_iteration(self, browser):
        page = AuthPage(browser)
        page.enter_as_local_user()

    def test_open_an_mailing_lists_reports_as_local_user_second_iteration(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports_as_local_user_second_iteration(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_should_report_not_visible(self, browser):
        page = Reports(browser)
        page.should_report_not_visible_by_saved_name()


@pytest.mark.skip
@allure.title('Отчеты - проверка доступа к детализации, фильтрам и настройкам визуализации в отчете (для роли на ''Чтение)')
class TestCheckingReportElements:

    def test_open_an_mailing_lists(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_open_last_report(self, browser):
        page = Reports(browser)
        page.open_last_report()

    def test_should_elements_on_report_page_availible(self, browser):
        page = Reports(browser)
        page.should_elements_on_report_page_availible()

    def test_should_elements_on_report_page_editing_availible(self, browser):
        page = Reports(browser)
        page.should_elements_on_report_page_availible()
        page.should_elements_on_report_page_editing_availible()


@pytest.mark.skip
@allure.title('Отчеты - Удаление последнего отчета')
class TestAnalyticsReportsDeleteLast:

    def test_open_an_mailing_lists_reports(self, browser):
        page = MailingLists(browser)
        page.open_an_mailing_lists_reports()

    def test_open_an_reports(self, browser):
        page = Reports(browser)
        page.open_an_reports()

    def test_delete_last_report(self, browser):
        page = Reports(browser)
        page.delete_last_report()
