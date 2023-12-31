import json
import random
import re
import time

from req.Helpers.user_session import UserSession
from req.Api.req_xba_cook import XbaCook
from resourses.constants import QA_SPAM_EMAIL, DB_picker_tables, DB_Shallow, API_AUTO_TEST_
from resourses.static_methods import get_datetime_now_z, get_str_random_num
from tests.case.api.permitter import PermitterCase

xba_profile_id = set()  # 'id' профиля xBA
xba_group_id = set()    # 'id' метапрофиля // API_AUTO_TEST_x


class XbaStatType:
    """Виды статистики xba-профилей, xba-метапрофилей"""
    default = "ind_and_group_stats"
    ind_stats = "ind_stats"
    group_stats = "group_stats"
    ind_and_group_stats = "ind_and_group_stats"


class XbaIdFunction:
    """Функция построения xba-профиля"""
    count = 1
    count_distinct = 2

    min_log_time = 5
    max_log_time = 6
    delta_log_time = 7
    len_distinct_hour = 8
    avg = 9
    min = 10
    max = 11
    sum = 12
    avg_not_zero = 13
    min_not_zero = 14
    max_not_zero = 15
    sum_not_zero = 16
    log_avg = 17
    log_min = 18
    log_max = 19
    log_sum = 20
    novelty = 21
    chi_squared_distance = 22


"""
    xBA profile: id_category:
    
    "id": 1,"name": "Другое"
    "id": 2,"name": "Выявление инсайдера"
    "id": 3,"name": "Выявление компрометации"
    "id": 4,"name": "Нецелевое использование ресурсов"
    "id": 5,"name": "Ошибки конфигурации"
    "id": 6,"name": "Нарушение политик ИБ"
    "id": 7,"name": "Работа вредоносного ПО"
    "id": 8,"name": "Эффективность ИС"
    "id": 9,"name": "Непрерывность бизнес-процессов"
    "id": 10,"name": "Прогнозирование загрузки"
    "id": 11,"name": "Эффективность персонала"
"""


def _get_sample_xba_profile_data(u_session: UserSession) -> dict:

    self_user_id = u_session.get_self_user_id()

    # fixme: доступ к таблицам, если нет доступа, то не создаст
    db_name = DB_Shallow.name
    db_table_name = DB_Shallow.tab_boulder_general
    db_time_column = DB_Shallow.col_timestamp

    u_session.asserts_check_db_and_table_is_exists(db_name, db_table_name)

    db_id = u_session.get_db_id_by_name(db_name)

    db_es_entity_column = DB_Shallow.col_name
    db_es_entity_type = DB_Shallow.col_item_group
    db_es_additional_column = DB_Shallow.col_price

    sample_data = {
        "name": API_AUTO_TEST_ + get_str_random_num(),
        # "description": "xba_profile_desc",
        "published": False,
        "opened": False,
        "author_id": self_user_id,
        # "author": "self_user_id",
        # "editor_id": self_user_id,
        # "editor": "self_user_id",
        # "created": "2023-02-15T07:55:02.631066Z",
        # "modified": "2023-02-15T07:55:02.631066Z",
        "db_id": db_id,
        "db_name": db_name,
        "table_name": db_table_name,
        # >> status: 1 -> запущен
        # >> status: 2 -> выполнен
        # >> status: 3 -> выполнен с ошибками
        # "status": 3,
        "profile_type": "median",
        "id_function": XbaIdFunction.log_sum,
        "id_category": 3,
        "time_settings":
            {
                "time_column": db_time_column,
                "time_start": get_datetime_now_z(day_delta=-3),
                "time_end": get_datetime_now_z(),
                "discretization_period": "hour",    # "minute",
                # "stat_period": ""
            },
        "entity_settings":
            {
                "entity_column": db_es_entity_column,
                "entity_column_name": "other",  # Категория сущности ( user|..|other
                "entity_type": db_es_entity_type,
                "obj_column": "",
                "obj_column_name": "",
                "additional_column": db_es_additional_column,
                "levels":
                    {
                        "level1": 2,
                        "level2": 4,
                        "level3": 6,
                        "level4": 8
                    }
            },
        "filter_settings": [],
        # "time_last_executed": "2023-07-20T12:50:32.074704Z",
        # "log_last_executed": "",
        "group_info": None,  # настройка метапрофиля
        "stat_type": XbaStatType.default
    }

    return sample_data.copy()


def _xba_profile_info_checklist(xba_profile_info: dict):
    _full_assertion_message = []

    def _check_key_in_dict(key_, dict_: dict):
        if key_ not in dict_:
            _full_assertion_message.append(f"\nDict: {dict_}\n doesn't have a key: {key_}")

    def _check_key_value_in_list(key_, values_list, dict_: dict):
        if key_ not in dict_:
            _full_assertion_message.append(f"\nDict: {dict_}\n doesn't have a key: {key_}")
            return
        if dict_[key_] not in values_list:
            _full_assertion_message.append(f"\nDict: {xba_profile_info}\n key: {key_}, key_value: {dict_[key_]} not in {values_list}")

    _check_key_in_dict('stat_type', xba_profile_info)   # DAT-5856  # DAT-5824
    _check_key_value_in_list('stat_type', ('ind_and_group_stats', 'group_stats', 'ind_stats'), xba_profile_info)

    _check_key_in_dict('author', xba_profile_info)
    _check_key_in_dict('author_id', xba_profile_info)
    _check_key_in_dict('created', xba_profile_info)
    _check_key_in_dict('db_id', xba_profile_info)
    _check_key_in_dict('db_name', xba_profile_info)
    _check_key_in_dict('description', xba_profile_info)
    _check_key_in_dict('editor', xba_profile_info)
    _check_key_in_dict('editor_id', xba_profile_info)
    _check_key_in_dict('entity_settings', xba_profile_info)
    _check_key_in_dict('entity_settings', xba_profile_info)
    _check_key_in_dict('entity_column', xba_profile_info['entity_settings'])
    _check_key_in_dict('entity_column_name', xba_profile_info['entity_settings'])
    _check_key_in_dict('entity_type', xba_profile_info['entity_settings'])
    _check_key_in_dict('obj_column', xba_profile_info['entity_settings'])
    _check_key_in_dict('obj_column_name', xba_profile_info['entity_settings'])
    _check_key_in_dict('additional_column', xba_profile_info['entity_settings'])
    _check_key_in_dict('levels', xba_profile_info['entity_settings'])
    _check_key_in_dict('level1', xba_profile_info['entity_settings']['levels'])
    _check_key_in_dict('level2', xba_profile_info['entity_settings']['levels'])
    _check_key_in_dict('level3', xba_profile_info['entity_settings']['levels'])
    _check_key_in_dict('level4', xba_profile_info['entity_settings']['levels'])
    _check_key_in_dict('filter_settings', xba_profile_info)
    _check_key_in_dict('func_name', xba_profile_info)
    _check_key_in_dict('group_info', xba_profile_info)
    _check_key_in_dict('id', xba_profile_info)
    _check_key_in_dict('id_category', xba_profile_info)
    _check_key_in_dict('id_function', xba_profile_info)
    _check_key_in_dict('log_last_executed', xba_profile_info)
    _check_key_in_dict('modified', xba_profile_info)
    _check_key_in_dict('name', xba_profile_info)
    _check_key_in_dict('opened', xba_profile_info)
    _check_key_in_dict('profile_type', xba_profile_info)
    _check_key_in_dict('published', xba_profile_info)
    _check_key_in_dict('status', xba_profile_info)
    _check_key_in_dict('table_name', xba_profile_info)
    _check_key_in_dict('time_last_executed', xba_profile_info)
    _check_key_in_dict('time_settings', xba_profile_info)
    _check_key_in_dict('time_column', xba_profile_info['time_settings'])
    _check_key_in_dict('time_start', xba_profile_info['time_settings'])
    _check_key_in_dict('time_end', xba_profile_info['time_settings'])
    _check_key_in_dict('discretization_period', xba_profile_info['time_settings'])
    _check_key_in_dict('stat_period', xba_profile_info['time_settings'])

    assert len(_full_assertion_message) == 0, "".join(_full_assertion_message)


class XbaCookCase(UserSession):

    def _collect_test_xba_group_id(self):
        resp = XbaCook(self.sess, self.host).xba_cook_profiles_groups_get()
        assert resp.status_code == 200, f"assert::xba_cook_profiles_groups_get, failed. status_code: {resp.status_code}, resp.text: {resp.text}"

        _group_id_rows = json.loads(resp.text)['res']
        for _row in _group_id_rows:
            if str(_row['name']).startswith(API_AUTO_TEST_):                # фильтрация по шаблону > добавление в group_id
                xba_group_id.add(int(_row['id']))

    def get_test_xba_group_id(self) -> int:
        """Get from global xba_group_id : API_AUTO_TEST_x
        Получение id тестового Метапрофиля
        """
        if len(xba_group_id) == 0:
            self._collect_test_xba_group_id()

        if len(xba_group_id) == 0:
            # запрос на создание нового метапрофиля
            req = XbaCook(self.sess, self.host)
            new_xba_group_data = {
                "name": API_AUTO_TEST_ + get_str_random_num(),
                "stat_type": XbaStatType.default
            }
            resp_new_group_id = req.xba_cook_profiles_groups_post(new_xba_group_data)
            assert resp_new_group_id.status_code == 200, \
                f"""Ошибка,
                post_data: {new_xba_group_data}
                resp_code: {resp_new_group_id.status_code}
                resp_text: {resp_new_group_id.text}
                """
            new_group_id = json.loads(resp_new_group_id.text)['res']
            return int(new_group_id)

        return xba_group_id.pop()

    def _collect_xba_profile_id_(self):
        resp = XbaCook(self.sess, self.host).xba_cook_profiles_get()
        assert resp.status_code == 200, f"assert::xba_cook_profiles_get, failed. status_code: {resp.status_code}, resp.text: {resp.text}"

        _profile_id_rows = json.loads(resp.text)['res']
        for _row in _profile_id_rows:
            if str(_row['name']).startswith(API_AUTO_TEST_):                # фильтр по шаблону > добавление в profile_id
                xba_profile_id.add(int(_row['id']))

    def get_test_xba_profile_id(self) -> int:
        """Get from global profile_id : API_AUTO_TEST_x
        Получение id тестового xba-Профиля"""
        if len(xba_profile_id) == 0:
            self._collect_xba_profile_id_()

        if len(xba_profile_id) == 0:
            resp_new_profile_id = self.case_xba_cook_profiles_post()        # запрос на создание нового профиля xBA
            new_profile_id = json.loads(resp_new_profile_id.text)['res']
            return int(new_profile_id)                                      # вернуть 'id' нового профиля xBA

        return xba_profile_id.pop()

    def _wait_for_profile_status(self,
                                 *,
                                 profile_id: int,
                                 not_equal: bool = False,
                                 expect_status_id: int = 2,
                                 timeout_sec: int = 15
                                 ) -> bool:
        """
        status: 1 -> запущен \n
        status: 2 -> выполнен \n
        status: 3 -> выполнен с ошибками\n
        :param profile_id xba_profile_id
        :param not_equal Передать 'True' для ожидания статуса не равного expect_status_id
        :param expect_status_id Ожидаемый статус профиля:
        :param timeout_sec сколько времени ждать
        """

        _wait_time_sec = abs(timeout_sec) / 4
        if _wait_time_sec > 5:
            _wait_time_sec = 5

        _start_time = time.time()
        while True:
            resp = XbaCook(self.sess, self.host).xba_cook_profiles_id_get(profile_id)
            assert resp.status_code == 200, f"Ошибка при получении профиля, code: {resp.status_code}, {resp.text}"

            _current_status_id = int(json.loads(resp.text)['res']['status'])
            if not_equal ^ (_current_status_id == expect_status_id):
                return True
            else:
                time_rest = timeout_sec - (time.time() - _start_time)
                if time_rest < 0:
                    break
                if _wait_time_sec > time_rest:
                    time.sleep(time_rest)
                    continue    # последняя итерация
                time.sleep(_wait_time_sec)
        return False

    def case_xba_cook_anomalies_get(self):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_anomalies_get()
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_anomalies_picker_max_min_get(self):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_anomalies_picker_max_min_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_check_entity_type_post(self):
        # look: "column": неверные параметры/null в поле, возвращают неочевидный тип ошибки
        # {"error":{"code":400,"description":"too many distinct values in column","msg":"Неверные параметры"}}

        db_name = DB_Shallow.name
        db_table = DB_Shallow.tab_boulder_general
        db_table_col = DB_Shallow.col_name

        self.asserts_check_db_and_table_is_exists(db_name, db_table)

        db_id = self.get_db_id_by_name(db_name)

        req = XbaCook(self.sess, self.host)
        data = {
            "db_id": db_id,
            "table": db_table,
            "column": db_table_col
        }
        resp = req.xba_cook_check_entity_type_post(data)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_dashboard_entities_post(self, post_data: dict):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_dashboard_entities_post(post_data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_dashboard_entities_more_post(self, post_data: dict):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_dashboard_entities_more_post(post_data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # 200: {"res":{"entities_for_top":[]}}

    def case_xba_cook_dashboard_groups_post(self):
        # DAT-5252
        req = XbaCook(self.sess, self.host)

        data_keyless = {
            "start": get_datetime_now_z(day_delta=-1),
            "end": get_datetime_now_z(),
            "time_zone": "Europe/Moscow"
        }
        resp = req.xba_cook_dashboard_groups_post(data_keyless)
        # print(resp.text)
        assert resp.status_code == 400, f"1.Ошибка, код {resp.status_code}, {resp.text}"
        # 400: {"error":{"code":400,"msg":"Добавьте хотя бы одну категорию"}}
        assert resp.text == '{"error":{"code":400,"msg":"Добавьте хотя бы одну категорию"}}\n', f"resp.text: {resp.text}"

        d_keys = ["department", "user", "host", "process", "other"]

        for key in d_keys:
            data = data_keyless.copy()
            data.update({key: True})

            resp = req.xba_cook_dashboard_groups_post(data)
            # print(resp.text)
            assert resp.status_code == 200, f"c.key: {key}\npost_data:{data}\n Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_dashboard_groups_more_post(self):
        # DAT-5252
        req = XbaCook(self.sess, self.host)

        data_keyless = {
            "start": get_datetime_now_z(day_delta=-1),
            "end": get_datetime_now_z(),
            "time_zone": "Europe/Moscow"
        }
        resp = req.xba_cook_dashboard_groups_more_post(data_keyless)
        # print(resp.text)
        assert resp.status_code == 200, f"1.Ошибка, код {resp.status_code}, {resp.text}"
        # 200: {"res":{"groups_for_top":[]}}

        d_keys = ["department", "user", "host", "process", "other"]

        for key in d_keys:
            data = data_keyless.copy()
            data.update({key: True})

            resp = req.xba_cook_dashboard_groups_post(data)
            # print(resp.text)
            assert resp.status_code == 200, f"c.key: {key}. Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_dashboard_profiles_post(self, post_data: dict):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_dashboard_profiles_post(post_data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # {"res":{"top_profiles_table":null,"profile_categories_chart":null,"entity_categories_chart":null,"risky_profiles_graph":null}}

    def case_xba_cook_dashboard_profiles_more_post(self, post_data: dict):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_dashboard_profiles_more_post(post_data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # {"res":{"top_profiles_table":null}}

    def case_xba_cook_entity_post(self):
        req = XbaCook(self.sess, self.host)
        data = {
            "end": "",
            "name": "user",
            "start": "",
            "type": ""
        }
        resp = req.xba_cook_entity_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_entity_details_post(self):
        req = XbaCook(self.sess, self.host)
        data = {
            "end": "",
            "name": "user",
            "start": "",
            "type": ""
        }
        resp = req.xba_cook_entity_details_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # todo: пока возвращает заглушку DAT-5186, пункт 6
    # type"user" > возвращает {"res":{"name":"","type":""}}
    def case_xba_cook_entity_info_post(self):
        req = XbaCook(self.sess, self.host)
        # entity_name <- summary <- xba_prof_id
        data = {
            "name": "Ефремов Максим",
            "type": "user"
        }
        resp = req.xba_cook_entity_info_post(data)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_entity_info_settings_get(self):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_entity_info_settings_get()
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_entity_info_settings_post(self):
        # front: /profiles > Настройка справочников - заполнить + [сохранить]
        req = XbaCook(self.sess, self.host)

        db_name = DB_picker_tables.name
        db_table = "ad_groups_imported"

        self.asserts_check_db_and_table_is_exists(db_name, db_table)

        db_id = self.get_db_id_by_name(db_name)

        data = {
            "user_settings": {
                "db_id": db_id,
                "table_name": db_table,
                "fields_mapping": {
                        "mapping_key_field": "sAMAccountName",
                        "full_name": "name",
                        "phone": "mobile",
                        "email": "mail",
                        "department": "department",
                        "position": "description",
                        "manager": "objectClass"
                    }
            }
        }

        resp = req.xba_cook_entity_info_settings_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        assert resp.text == '{"res":"ok"}\n', f"Ошибка, текст ответа {resp.text}"

    def case_xba_cook_entity_info_settings_entity_type_delete(self, entity_type):
        # front: /profiles - настройка справочников - [очистить] + [сохранить]
        # entity_type: user|department|process|other. 'all' to delete everything
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_entity_info_settings_entity_type_delete(entity_type)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_entity_picker_max_min_post(self):
        # front: /entity/<type>/<name>  # max-min для карточки сущности
        req = XbaCook(self.sess, self.host)
        data = {
            "name": "emerald",
            "type": "other"
        }
        resp = req.xba_cook_entity_picker_max_min_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_entity_risks_description_post(self):
        req = XbaCook(self.sess, self.host)
        data = {
            "name":     "emerald",
            "type":     "other",
            "start":    get_datetime_now_z(day_delta=-4),
            "end":      get_datetime_now_z(day_delta=-1)
        }
        resp = req.xba_cook_entity_risks_description_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_max_min_post(self):
        req = XbaCook(self.sess, self.host)

        db_name = DB_Shallow.name
        db_table = DB_Shallow.tab_boulder_general
        db_table_col = DB_Shallow.col_timestamp

        self.asserts_check_db_and_table_is_exists(db_name, db_table)

        db_id = self.get_db_id_by_name(db_name)

        data = {
            "db_id": db_id,
            "table": db_table,
            "column": db_table_col
        }
        resp = req.xba_cook_max_min_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_get(self):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_profiles_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # Брать случайный результат(профиль) и проверять наличие обязательных полей
        xba_profile_list = json.loads(resp.text)['res']
        xba_profile_info: dict = random.choice(xba_profile_list)
        _xba_profile_info_checklist(xba_profile_info)

    def case_xba_cook_profiles_post(self):
        # создать xba_профиль
        req = XbaCook(self.sess, self.host)

        data = _get_sample_xba_profile_data(self)

        resp = req.xba_cook_profiles_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        return resp

    def validation_xba_cook_profiles_post(self, validation_fields: dict, expected_code: int, expected_message: str | re.Pattern):
        # check validation for post: /back/dp.xba_cook/profiles
        req = XbaCook(self.sess, self.host)

        data = _get_sample_xba_profile_data(self)
        data.update(validation_fields)

        resp = req.xba_cook_profiles_post(data)

        match type(expected_message):
            case re.Pattern:
                assert resp.status_code == expected_code and len(re.findall(expected_message, resp.text)) != 0, \
                    f"""
                    expected_code: {expected_code}
                    current_code_: {resp.status_code}
                    expected_regexp: {expected_message.pattern}
                    actual_response: {resp.text}
                    """
            case _:
                assert resp.status_code == expected_code and resp.text == expected_message, \
                    f"""
                    expected_code: {expected_code}
                    current_code_: {resp.status_code}
                    expected_resp__: {expected_message}
                    actual_response: {resp.text}
                    """

    def case_xba_cook_profiles_categories_get(self):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_profiles_categories_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_export_profiles_post(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self.get_test_xba_profile_id()
        data = {"profile_ids": [prof_id]}
        resp = req.xba_cook_profiles_export_profiles_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_functions_get(self):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_profiles_functions_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_graph_drilldown_statement_id_post(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self.get_test_xba_profile_id()
        data = {
            "columns": [
                ""
            ],
            "name": "",
            "time": get_datetime_now_z()
        }
        resp = req.xba_cook_profiles_graph_drilldown_statement_id_post(prof_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_graph_drilldown_id_post(self, profile_id, post_data):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_profiles_graph_drilldown_id_post(profile_id, post_data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # DAT-5184
        # Проверка наличия ключа "description" в ответе
        try:
            # отсутствие ключа на любом узле бросит ошибку "KeyError"
            json.loads(resp.text)['res']['info']['description']
        except KeyError:
            assert False, f"Ошибка, отсутствует ключ res>info>description в ответе, {resp.text}"

    def case_xba_cook_profiles_max_min_id_get(self):
        req = XbaCook(self.sess, self.host)

        prof_id = self.get_test_xba_profile_id()

        # запустить профиль прежде чем получить max_min:
        # новый профиль может ещё рассчитываться -> 400: нет данных

        resp = req.xba_cook_profiles_max_min_id_get(prof_id)
        # print(f"prof_id: {prof_id}, resp: {resp.text}")
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # профиль 'prof_id' не запускался >> 400: {"error":{"code":400,"msg":"Нет данных"}}
        # профиль запускался; выполнен с ошибками >> 200: {"res":{"max":null,"min":null}}

    def case_xba_cook_profiles_graph_personal_id_post(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self.get_test_xba_profile_id()
        data = {
            "end": "2023-02-14T00:00:00Z",
            "name": "",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        resp = req.xba_cook_profiles_graph_personal_id_post(prof_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_groups_get(self):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_profiles_groups_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_groups_put(self, _group_id: int, ch_name: str, ch_stat_type: str):
        req = XbaCook(self.sess, self.host)
        data = {
            "id": _group_id,
            "name": ch_name,
            # "weight": ""
            "stat_type": ch_stat_type
        }
        resp = req.xba_cook_profiles_groups_put(data)
        assert resp.status_code == 200, \
            f"""Ошибка,
            post_data: {data}
            resp_code: {resp.status_code}
            resp_text: {resp.text}
            """

    def case_xba_cook_profiles_groups_post(self, new_xba_group_name: str, stat_type: str):
        # Создание метапрофиля
        req = XbaCook(self.sess, self.host)
        data = {
            # "id": str_rand_num,
            "name": new_xba_group_name,
            # "weight": "",
            "stat_type": stat_type
        }
        resp = req.xba_cook_profiles_groups_post(data)
        assert resp.status_code == 200, \
            f"""Ошибка,
            post_data: {data}
            resp_code: {resp.status_code}
            resp_text: {resp.text}
            """
        # 400: {"error":{"code":0,"msg":"StatType: stat_type must be one of [ind_stats group_stats ind_and_group_stats]; "}}

    def case_xba_cook_profiles_groups_info_get(self):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_profiles_groups_info_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_groups_id_delete(self):
        req = XbaCook(self.sess, self.host)
        _group_id = self.get_test_xba_group_id()
        resp = req.xba_cook_profiles_groups_id_delete(_group_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_groups_group_id_profiles_get(self):
        req = XbaCook(self.sess, self.host)
        _group_id = self.get_test_xba_group_id()
        resp = req.xba_cook_profiles_groups_group_id_profiles_get(_group_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_groups_id_post(self):
        # нужен group_id хотя бы с одним профилем
        req = XbaCook(self.sess, self.host)

        group_id = self.get_test_xba_group_id()

        # todo: вынести метод привязки метапрофиля к профилю
        # Получить данные профиля, для изменения
        prof_id = self.get_test_xba_profile_id()
        prof_id_data_resp = req.xba_cook_profiles_id_get(prof_id)
        assert prof_id_data_resp.status_code == 200, \
            f"3.Ошибка при получении данных профиля, code: {prof_id_data_resp.status_code}, text: {prof_id_data_resp.text}"

        prof_id_data: dict = json.loads(prof_id_data_resp.text)['res']
        # Привязать метапрофиль 'group_id' к профилю 'prof_id'
        prof_id_data.update({
            # fixme: получить group_info, потом .append into, cuz group info may be not [empty]
            "group_info": [
                {
                    "id": group_id,
                    # "name": "group_name",
                    "weight": 5
                },
            ]
        })

        assert self._wait_for_profile_status(profile_id=prof_id, timeout_sec=30), \
            f"2.Статус профиля не перешел в состояние 'выполнен' за отведенное время"

        prof_change_resp = req.xba_cook_profiles_id_post(prof_id, prof_id_data)
        assert prof_change_resp.status_code == 200, \
            f"1.Ошибка при изменении профиля, code: {prof_change_resp.status_code}, text: {prof_change_resp.text}"

        data = {
            "end": "2023-02-14T00:00:00Z",
            "name": "",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        resp = req.xba_cook_profiles_groups_id_post(group_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_groups_id_max_min_get(self):
        req = XbaCook(self.sess, self.host)

        # нужен метапрофиль с профилем
        _group_id = self.get_test_xba_group_id()

        resp = req.xba_cook_profiles_groups_id_max_min_get(_group_id)
        print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # {"error":{"code":400,"description":"no completed profiles in this group","msg":"Нет данных"}}

    def case_xba_cook_profiles_groups_profile_id_group_id_delete(self):
        req = XbaCook(self.sess, self.host)
        prof_id = None
        group_id = None
        resp = req.xba_cook_profiles_groups_profile_id_group_id_delete(prof_id, group_id)
        print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_groups_profile_id_group_id_weight_get(self):
        # изменить вес профиля в метапрофиле
        req = XbaCook(self.sess, self.host)

        prof_id = 2077
        group_id = 1553
        weight = 20

        resp = req.xba_cook_profiles_groups_profile_id_group_id_weight_get(prof_id, group_id, weight)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_import_profiles_post(self):
        req = XbaCook(self.sess, self.host)

        sdata: dict = _get_sample_xba_profile_data(self)
        sdata.update({
            "name": API_AUTO_TEST_ + "import_" + get_str_random_num(),
            # "db_name": DbName.picker_tables,    # без имени бд не принимает
        })
        # print(sdata)

        data = {
            "profile_list": [
                sdata,
                # data1
                # data2
            ]
        }
        resp = req.xba_cook_profiles_import_profiles_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_start_id_get(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self.get_test_xba_profile_id()
        resp = req.xba_cook_profiles_start_id_get(prof_id)
        if resp.status_code == 400:
            assert resp.text == '{"error":{"code":400,"msg":"Задание уже запустили"}}\n', f"Ошибка, код {resp.status_code}, {resp.text}"
        else:
            assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # {"error":{"code":400,"msg":"Задание уже запустили"}}

    def case_xba_cook_profiles_stop_id_get(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self.get_test_xba_profile_id()
        resp = req.xba_cook_profiles_stop_id_get(prof_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_id_get(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self.get_test_xba_profile_id()
        resp = req.xba_cook_profiles_id_get(prof_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        xba_profile_info = json.loads(resp.text)['res']
        _xba_profile_info_checklist(xba_profile_info)

    def case_xba_cook_profiles_id_post(self, prof_id: int, prof_changes: dict):
        # изменить xba_профиль
        req = XbaCook(self.sess, self.host)

        assert self._wait_for_profile_status(profile_id=prof_id, not_equal=True, expect_status_id=1), \
            "Профиль не вышел из статуса 'запущен' за отведенное время"

        # забрать текущие настройки по xba-профилю
        actual_profile_resp = req.xba_cook_profiles_id_get(prof_id)
        assert actual_profile_resp.status_code == 200, f"Ошибка, код {actual_profile_resp.status_code}, {actual_profile_resp.text}"

        # post_data = _get_sample_xba_profile_data(self)
        # добавить текущие настройки xba-профиля к запросу, изменить значения полей, которые хотим поменять
        post_data = json.loads(actual_profile_resp.text)['res']
        post_data.update(prof_changes)

        resp = req.xba_cook_profiles_id_post(prof_id, post_data)
        assert resp.status_code == 200, \
            f"""Ошибка, 
            xba_profile_id: {prof_id}
            expected_changes: {prof_changes}
            result_post_data: {post_data}
            response_code: {resp.status_code}
            response_text: {resp.text}"""
        # 400: {"error":{"code":400,"msg":"Пожалуйста, дождитесь окончания расчета профиля"}}

    def case_xba_cook_profiles_id_delete(self):
        req = XbaCook(self.sess, self.host)

        prof_id = self.get_test_xba_profile_id()

        assert self._wait_for_profile_status(profile_id=prof_id), \
            "Статус профиля не перешел в состояние 'выполнен' за отведенное время"

        xba_db_name = f"XBA_{prof_id}"
        # выдать права на изменение хранилища 'xba_db_name'
        PermitterCase().add_role_permission_to_change_db(self.get_self_role_id(), xba_db_name)

        resp = req.xba_cook_profiles_id_delete(prof_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_id_graph_post(self):
        req = XbaCook(self.sess, self.host)

        prof_id = self.get_test_xba_profile_id()    # status: запущен | выполнен

        # entity <- [post] /summary <- prof_id
        data = {
            "start": get_datetime_now_z(day_delta=-1),
            "end": get_datetime_now_z(),
            # "entity": "?",
            # "entity_group": "?str(int)"
        }
        resp = req.xba_cook_profiles_id_graph_post(prof_id, data)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_id_log_last_get(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self.get_test_xba_profile_id()
        resp = req.xba_cook_profiles_id_log_last_get(prof_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_id_summary_post(self):

        req = XbaCook(self.sess, self.host)
        prof_id = self.get_test_xba_profile_id()
        data = {
            # "entity_group": "string", # optional,
            "start": get_datetime_now_z(day_delta=-1),    # <- get| graph/max_min
            "end": get_datetime_now_z()
        }
        # data = {}
        resp = req.xba_cook_profiles_id_summary_post(prof_id, data)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_id_whitelist_post(self):
        # !!api заменяет существующий список >> добавлять к существующему списку
        req = XbaCook(self.sess, self.host)

        str_rand_num = str(random.randint(1000, 9999))
        prof_id = self.get_test_xba_profile_id()

        cur_whitelist_resp = req.xba_cook_profiles_id_form_whitelist_get(prof_id, "list")
        assert cur_whitelist_resp.status_code == 200, f"Ошибка, код {cur_whitelist_resp.status_code}, {cur_whitelist_resp.text}"
        cur_whitelist: list = json.loads(cur_whitelist_resp.text)['res']
        # print(f"cur_wl: {cur_whitelist}") # print(type(cur_whitelist)) >> list
        cur_whitelist.append({"name": API_AUTO_TEST_ + str_rand_num})

        assert self._wait_for_profile_status(profile_id=prof_id), \
            "Статус профиля не перешел в состояние 'выполнен' за отведенное время"

        data = {"data": cur_whitelist}
        resp = req.xba_cook_profiles_id_whitelist_post(prof_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # 400: {"error":{"code":102,"msg":"Запущен перерасчёт профиля, изменение состояния недоступно"}}

    def case_xba_cook_profiles_id_whitelist_element_post(self):
        req = XbaCook(self.sess, self.host)

        str_random_num = str(random.randint(100, 999))
        prof_id = self.get_test_xba_profile_id()

        assert self._wait_for_profile_status(profile_id=prof_id, not_equal=True, expect_status_id=1), \
            "Статус профиля 'запущен' и не изменился за отведенное время"

        data = {"data": API_AUTO_TEST_ + str_random_num}
        resp = req.xba_cook_profiles_id_whitelist_element_post(prof_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # {"error":{"code":102,"msg":"Запущен перерасчёт профиля, изменение состояния недоступно"}}

    def case_xba_cook_profiles_id_zones_post(self):
        # фильтрация по зонам риска
        zone = ["red", "green", "yellow"]

        req = XbaCook(self.sess, self.host)

        data = {
            "start": get_datetime_now_z(day_delta=-7),
            "end": get_datetime_now_z(),
            # todo: проверку на entity_group > отдельным кейсом
            # "entity_group": "other",  # str(int)  # optional
            "zone": "all",
            # "zones": {
            #     "red_high": 3,
            #     "red_low": 3,
            #     "yellow_high": 2,
            #     "yellow_low": 2,
            #     "green_high": 1,
            #     "green_low": 1,
            # }
        }

        prof_id = self.get_test_xba_profile_id()
        resp = req.xba_cook_profiles_id_zones_post(prof_id, data)
        # print(resp.text)
        assert resp.status_code == 200, f"1.Ошибка, код {resp.status_code}, {resp.text}"
        # 400: {"error":{"code":0,"msg":"Code: 81, Message: Database XBA_$prof_id doesn't exist"}}

        resp_res = json.loads(resp.text)['res']

        for _z in zone:
            data.update({"zone": _z})

            assert f"{_z}_count" in resp_res, f"Отсутствует поле '{_z}_count' в 'res':{resp_res}"

            resp = req.xba_cook_profiles_id_zones_post(prof_id, data)
            assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

            resp_res_entities = json.loads(resp.text)['res']['entities']
            if resp_res[f"{_z}_count"] > 0:
                assert _z in resp_res_entities, f"Отсутствует поле '{_z}' в 'res':'entities':{resp_res_entities}"
            else:
                assert resp_res_entities is None, f"Фильтрация возвращает больше значений чем ожидалось | post_data = {data}, resp: {resp.text}"

    def case_xba_cook_profiles_id_form_whitelist_get(self, prof_id: int, form: str):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_profiles_id_form_whitelist_get(prof_id, form)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_profile_id_whitelist_element_id_delete(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self.get_test_xba_profile_id()

        # профиль должен содержать хотя-бы 1 элемент в whitelist
        # todo: >> добавить элемент в whitelist

        whitelist_element_id = 1    # todo? id элемента в бд?
        resp = req.xba_cook_profiles_profile_id_whitelist_element_id_delete(prof_id, whitelist_element_id)
        print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # {"error":{"code":400,"description":"whitelist id cannot be less than 1","msg":"Данные не удалены из бд"}}

    def case_xba_cook_xba_get(self):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_xba_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_set_log_level_xba_py_mode_post(self, mode):
        req = XbaCook(self.sess, self.host)

        data = {}

        resp = req.xba_cook_set_log_level_xba_py_mode_post(mode, data)
        print(resp.text)
        assert False

    def case_xba_cook_xba_post(self):
        req = XbaCook(self.sess, self.host)
        data = {
            # "XMLName":
            #     {
            #         "Space": "",
            #         "Local": "xba"
            #     },
            "destinations":
                [
                    {
                        "email": QA_SPAM_EMAIL,
                        # "syslog_host": "",
                        # "syslog_port": "",
                        "syslog_protocol": "TCP",
                        "disable_syslog": True,
                        "disable_email": False
                    },
                    # {
                    #     "email": "y.vanin@ngrsoftlab.ru",
                    #     # "syslog_host": "127.0.0.1",
                    #     # "syslog_port": 514,
                    #     "syslog_protocol": "udp",
                    #     "disable_syslog": True,
                    #     "disable_email": False
                    # },
                    {
                        "email": "",
                        "syslog_host": "1.12.3.22",
                        "syslog_port": 333,
                        "syslog_protocol": "tcp",
                        "disable_syslog": True,
                        "disable_email": True
                    },
                    {
                        "email": "",
                        "syslog_host": "2.212.23.31",
                        "syslog_port": 33,
                        "syslog_protocol": "tcp",
                        "disable_syslog": True,
                        "disable_email": True
                    }
                ]

        }

        resp = req.xba_cook_xba_post(data)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # 400: {"error":{"code":400,"description":"duplicate destination email","msg":"Обнаружен повторяющийся объект настроек"}}

    # __del__
    def all_api_auto_test_entity_delete(self):
        delete_req = XbaCook(self.sess, self.host)
        self._collect_test_xba_group_id()
        while len(xba_group_id) > 0:
            delete_req.xba_cook_profiles_groups_id_delete(xba_group_id.pop())

        self._collect_xba_profile_id_()
        while len(xba_profile_id) > 0:
            _pf_id = xba_profile_id.pop()
            xba_db_name = f"XBA_{_pf_id}"
            # выдать права на изменение хранилища 'xba_db_name'
            PermitterCase().add_role_permission_to_change_db(self.get_self_role_id(), xba_db_name)
            delete_req.xba_cook_profiles_id_delete(_pf_id)
            # print(_pf_id)
