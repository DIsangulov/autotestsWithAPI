import json
import random
import datetime


from req.Helpers.user_session import UserSession
from req.Api.req_xba_cook import XbaCook
from resourses.credentials import DbName
from tests.case.api.permitter import PermitterCase

_QA_SPAM_EMAIL = "s.yezhov@ngrsoftlab.ru"
API_AUTO_TEST_ = "API_AUTO_TEST_"

xba_profile_id = set()  # 'id' профиля xBA
xba_group_id = set()    # 'id' метапрофиля // API_AUTO_TEST_x


def get_datetime_now_z() -> str:
    # 2023-07-20T17:04:16Z
    return datetime.datetime.today().replace(microsecond=0).isoformat() + "Z"


def get_str_random_num(length: int = 4) -> str:
    return str(random.randint(int(10**(length-1)), int(10**length-1)))


def _get_sample_xba_profile_data(u_session: UserSession) -> dict:
    # todo: сделать "более" живые профили

    self_user_id = u_session.get_self_user_id()

    db_picker_tables = u_session.get_db_id_by_name(DbName.picker_tables)
    db_picker_tables_table_name = "ad_users_ngr"
    db_picker_tables_time_column = "badPasswordTime"
    db_es_entity_column = "department"
    db_es_entity_type = "lastLogoff"

    sample_data = {
        # "id": ???
        "name": API_AUTO_TEST_ + get_str_random_num(),
        # "description": None,
        "published": False,
        "opened": False,
        "author_id": self_user_id,
        # "author": "self_user_id",
        # "editor_id": self_user_id,
        # "editor": "self_user_id",
        # "created": "2023-02-15T07:55:02.631066Z",
        # "modified": "2023-02-15T07:55:02.631066Z",
        "db_id": db_picker_tables,
        "db_name": DbName.picker_tables,
        "table_name": db_picker_tables_table_name,
        # "status": 3,
        "profile_type": "median",
        "id_function": 6,  # << [get] /profiles/functions
        "id_category": 1,  # todo: описание
        "time_settings":
            {
                "time_column": db_picker_tables_time_column,
                "time_start": "1971-01-01T00:00:00Z",
                "time_end": "2022-12-06T08:36:09Z",
                "discretization_period": "minute",
                # "stat_period": ""
            },
        "entity_settings":
            {
                "entity_column": db_es_entity_column,
                "entity_column_name": "other",  # Категория сущности ( user|..|other
                "entity_type": db_es_entity_type,
                "obj_column": "",
                "obj_column_name": "",
                "additional_column": "",
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
        "group_info": None
    }

    return sample_data.copy()


class EntityCategory:
    user = "user"
    host = "host"
    process = "process"
    department = "department"
    other = "other"


class XbaCookCase(UserSession):

    def _collect_xba_group_id(self):
        resp = XbaCook(self.sess, self.host).xba_cook_profiles_groups_get()
        assert resp.status_code == 200, f"assert::xba_cook_profiles_groups_get, failed. status_code: {resp.status_code}, resp.text: {resp.text}"

        _group_id_rows = json.loads(resp.text)['res']
        for _row in _group_id_rows:
            if str(_row['name']).startswith(API_AUTO_TEST_):                # фильтрация по шаблону > добавление в group_id
                xba_group_id.add(int(_row['id']))

    def _get_xba_group_id(self) -> int:
        """get from global group_id : API_AUTO_TEST_x"""
        if len(xba_group_id) == 0:
            self._collect_xba_group_id()

        if len(xba_group_id) == 0:
            resp_new_group_id = self.case_xba_cook_profiles_groups_post()   # запрос на создание нового метапрофиля
            new_group_id = json.loads(resp_new_group_id.text)['res']
            return int(new_group_id)                                        # вернуть 'id' нового метапрофиля

        return xba_group_id.pop()                                           # возвращает случайное значение из group_id

    def _collect_xba_profile_id_(self):
        resp = XbaCook(self.sess, self.host).xba_cook_profiles_get()
        assert resp.status_code == 200, f"assert::xba_cook_profiles_get, failed. status_code: {resp.status_code}, resp.text: {resp.text}"

        _profile_id_rows = json.loads(resp.text)['res']
        for _row in _profile_id_rows:
            if str(_row['name']).startswith(API_AUTO_TEST_):                # фильтр по шаблону > добавление в profile_id
                xba_profile_id.add(int(_row['id']))

    def _get_xba_profile_id(self) -> int:
        """get from global profile_id : API_AUTO_TEST_x"""
        if len(xba_profile_id) == 0:
            self._collect_xba_profile_id_()

        if len(xba_profile_id) == 0:
            resp_new_profile_id = self.case_xba_cook_profiles_post()        # запрос на создание нового профиля xBA
            new_profile_id = json.loads(resp_new_profile_id.text)['res']
            return int(new_profile_id)                                      # вернуть 'id' нового профиля xBA

        return xba_profile_id.pop()

    def case_xba_cook_anomalies_get(self):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_anomalies_get()
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_anomalies_picker_max_min_get(self):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_anomalies_picker_max_min_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_xba_cook_check_entity_type_post(self):
        req = XbaCook(self.sess, self.host)
        db_picker_tables = self.get_db_id_by_name(DbName.picker_tables)
        data = {
            "column": "1",
            # "db_id": pt_id,
            "db_id": db_picker_tables,
            "table": "ad_users_ngr"
        }
        resp = req.xba_cook_check_entity_type_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_xba_cook_dashboard_post(self):
        req = XbaCook(self.sess, self.host)
        data = {
            "start_datetime": "2023-02-01T00:00:00.000Z",
            "time_zone": "Europe/Moscow"
        }
        resp = req.xba_cook_dashboard_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_xba_cook_dashboard_entities_post(self):
        # DAT-5251
        req = XbaCook(self.sess, self.host)
        data = {
            "start": "2022-10-21T16:39:01Z",
            "end": get_datetime_now_z(),
            "entity_category": EntityCategory.process    # todo: user|host|process|department|other
        }
        # data = {}   # :400
        resp = req.xba_cook_dashboard_entities_post(data)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_dashboard_entities_more_post(self):
        # DAT-5251
        req = XbaCook(self.sess, self.host)
        data = {
            "start": "2023-07-21T16:39:01Z",
            "end": get_datetime_now_z(),
            "entity_category": EntityCategory.host  # todo: user|host|process|department|other
        }
        # data = {}   # :200
        resp = req.xba_cook_dashboard_entities_more_post(data)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # 200: {"res":{"entities_for_top":[]}}

    def case_xba_cook_dashboard_groups_post(self):
        # DAT-5252
        req = XbaCook(self.sess, self.host)

        data_keyless = {
            "start": "2021-10-21T16:39:01Z",
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
            assert resp.status_code == 200, f"c.key: {key}. Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_dashboard_groups_more_post(self):
        # DAT-5252
        req = XbaCook(self.sess, self.host)

        data_keyless = {
            "start": "2021-10-21T16:39:01Z",
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

    def case_xba_cook_dashboard_profiles_post(self):
        # DAT-5245
        # "entity_category" # user, host, process, department, other, etc... # ?"entity_type"
        # "profile_category_id" # id of xba profile category (use get profile category list request)
        req = XbaCook(self.sess, self.host)

        data = {
            "start": "2022-10-21T16:39:01Z",
            "end": get_datetime_now_z(),
            "entity_category": EntityCategory.process,  # todo: user|host|process|department|other
            "profile_category_id": 0,  # 0  # 1-11
            }
        # data = {}
        resp = req.xba_cook_dashboard_profiles_post(data)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # {"res":{"top_profiles_table":null,"profile_categories_chart":null,"entity_categories_chart":null,"risky_profiles_graph":null}}

    def case_xba_cook_dashboard_profiles_more_post(self):
        # DAT-5245
        req = XbaCook(self.sess, self.host)

        data = {
            "start": "2022-10-21T16:39:01Z",
            "end": get_datetime_now_z(),
            "entity_category": EntityCategory.process,  # todo: user|host|process|department|other
            "profile_category_id": 0,   # 0  # 1-11
            }
        # data = {}
        resp = req.xba_cook_dashboard_profiles_more_post(data)
        print(resp.text)
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
        # print(resp.text)
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
        # print(resp.text)

    def case_xba_cook_entity_info_post(self):
        req = XbaCook(self.sess, self.host)
        data = {
            "name": "user",
            "type": ""
        }
        resp = req.xba_cook_entity_info_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_xba_cook_entity_info_settings_get(self):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_entity_info_settings_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_xba_cook_entity_info_settings_post(self):
        req = XbaCook(self.sess, self.host)
        db_picker_tables = self.get_db_id_by_name(DbName.picker_tables)
        db_picker_tables_table_name = "ad_users_ngr"
        data = {
            "user_settings":
            {
                "db_id": db_picker_tables,
                # "db_name": "picker_tables",
                "table_name": db_picker_tables_table_name,
                "fields_mapping":
                    {
                        "mapping_key_field": "sAMAccountName",
                        "full_name": "name",
                        "position": "description",
                        "department": "department",
                        "phone": "mobile",
                        "email": "mail",
                        "manager": "sn"
                    }
            }
        }
        resp = req.xba_cook_entity_info_settings_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        assert resp.text == '{"res":"ok"}\n', f"Ошибка, текст ответа {resp.text}"
        # print(resp.text)

    def case_xba_cook_entity_info_settings_entity_type_delete(self):
        req = XbaCook(self.sess, self.host)
        entity_type = "name"        # TODO: какие ещё || user|department|process|other. 'all' to delete everything
        resp = req.xba_cook_entity_info_settings_entity_type_delete(entity_type)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_entity_picker_max_min_post(self):
        req = XbaCook(self.sess, self.host)
        data = {
            "name": "user",
            "type": "user"
        }
        resp = req.xba_cook_entity_picker_max_min_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_entity_risks_description_post(self):
        req = XbaCook(self.sess, self.host)
        data = {"name": "shchetinin$@angaratech.ru",        # FIXME: хардкод
                "type": "user",
                "start": "2023-02-13T00:00:00Z",
                "end": "2023-02-14T00:00:00Z"}
        resp = req.xba_cook_entity_risks_description_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_xba_cook_max_min_post(self):
        req = XbaCook(self.sess, self.host)
        db_picker_tables = self.get_db_id_by_name(DbName.picker_tables)
        data = {
            "column": "1",
            # "db_id": pt_id,
            "db_id": db_picker_tables,
            "table": "ad_users_ngr"
        }
        resp = req.xba_cook_max_min_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_get(self):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_profiles_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_post(self):
        # создать xba_профиль
        req = XbaCook(self.sess, self.host)

        data = _get_sample_xba_profile_data(self)

        resp = req.xba_cook_profiles_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        return resp

    def case_xba_cook_profiles_categories_get(self):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_profiles_categories_get()
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_export_profiles_post(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self._get_xba_profile_id()
        data = {"profile_ids": [prof_id]}
        resp = req.xba_cook_profiles_export_profiles_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_functions_get(self):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_profiles_functions_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_graph_drilldown_statement_id_post(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self._get_xba_profile_id()
        data = {
            "columns": [
                ""
            ],
            "name": "",
            "time": "2022-12-06T08:36:09Z"
        }
        resp = req.xba_cook_profiles_graph_drilldown_statement_id_post(prof_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # fixme: mark.skip
    def case_xba_cook_profiles_graph_drilldown_id_post(self):
        req = XbaCook(self.sess, self.host)

        prof_id = self._get_xba_profile_id()
        data = {

        }
        resp = req.xba_cook_profiles_graph_drilldown_id_post(prof_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_graph_drilldown_1888_post(self):
        # DAT-5184
        # Проверка наличия ключа "description" в ответе
        req = XbaCook(self.sess, self.host)

        # FIXME: хардкод
        # нужны конкретные данные, для получения ответа иначе: {"error":{"code":400,"msg":"Нет данных"}}
        prof_id = 1888
        data = {
            "name": "Кривошеин Сергей",
            "time": "2023-05-23",
            "columns":
                [
                    "calc_time",
                    "name",
                    "risk"
                ]
        }
        resp = req.xba_cook_profiles_graph_drilldown_id_post(prof_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        try:
            # отсутствие ключа на любом узле бросит ошибку "KeyError"
            json.loads(resp.text)['res']['info']['description']
        except KeyError:
            assert False, f"Ошибка, отсутствует ключ res>info>description в ответе, {resp.text}"

    def case_xba_cook_profiles_max_min_id_get(self):
        req = XbaCook(self.sess, self.host)

        prof_id = self._get_xba_profile_id()

        # запустить профиль прежде чем получить max_min:
        # новый профиль может ещё рассчитываться -> 400: нет данных

        resp = req.xba_cook_profiles_max_min_id_get(prof_id)
        # print(f"prof_id: {prof_id}, resp: {resp.text}")
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # профиль 'prof_id' не запускался >> 400: {"error":{"code":400,"msg":"Нет данных"}}
        # профиль запускался; выполнен с ошибками >> 200: {"res":{"max":null,"min":null}}

    def case_xba_cook_profiles_graph_personal_id_post(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self._get_xba_profile_id()
        data = {
            "end": "2023-02-14T00:00:00Z",
            "name": "",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        resp = req.xba_cook_profiles_graph_personal_id_post(prof_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_graph_id_post(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self._get_xba_profile_id()
        data = {
            "end": "2023-02-14T00:00:00Z",
            "name": "",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        resp = req.xba_cook_profiles_graph_id_post(prof_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_groups_get(self):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_profiles_groups_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_groups_put(self):
        # Поменять имя Метапрофиля
        req = XbaCook(self.sess, self.host)
        rand_num = random.randint(100, 999)
        _group_id = self._get_xba_group_id()
        data = {
            "id": _group_id,
            "name": API_AUTO_TEST_ + f"changed_{rand_num}",
            "weight": ""
        }
        resp = req.xba_cook_profiles_groups_put(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_groups_post(self):
        # Создание метапрофиля
        req = XbaCook(self.sess, self.host)
        str_rand_num = str(random.randint(1000, 9999))
        data = {
            # "id": str_rand_num,
            "name": API_AUTO_TEST_ + str_rand_num,
            "weight": ""
        }
        resp = req.xba_cook_profiles_groups_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        return resp  # возвращает также ид новой группы

    def case_xba_cook_profiles_groups_info_get(self):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_profiles_groups_info_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_groups_id_delete(self):
        req = XbaCook(self.sess, self.host)
        _group_id = self._get_xba_group_id()
        resp = req.xba_cook_profiles_groups_id_delete(_group_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_groups_group_id_profiles_get(self):
        req = XbaCook(self.sess, self.host)
        _group_id = self._get_xba_group_id()
        resp = req.xba_cook_profiles_groups_group_id_profiles_get(_group_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_groups_id_post(self):
        # нужен group_id хотя бы с одним профилем
        req = XbaCook(self.sess, self.host)

        group_id = self._get_xba_group_id()

        # todo: вынести метод привязки метапрофиля к профилю
        # Получить данные профиля, для изменения
        prof_id = self._get_xba_profile_id()
        prof_id_data_resp = req.xba_cook_profiles_id_get(prof_id)
        assert prof_id_data_resp.status_code == 200, \
            f"2.Ошибка при получении данных профиля, code: {prof_id_data_resp.status_code}, text: {prof_id_data_resp.text}"
        prof_id_data: dict = json.loads(prof_id_data_resp.text)['res']

        # Привязать метапрофиль 'group_id' к профилю 'prof_id'
        prof_id_data.update({
            "group_info": [
                {
                    "id": group_id,
                    # "name": "group_name",
                    "weight": 5
                },
            ]
        })
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
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # FIXME: FIXME: @mark.skip
    # нужен профиль с метапрофилем
    def case_xba_cook_profiles_groups_id_max_min_get(self):
        req = XbaCook(self.sess, self.host)
        _group_id = self._get_xba_group_id()
        resp = req.xba_cook_profiles_groups_id_max_min_get(_group_id)
        print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # {"error":{"code":400,"description":"no completed profiles in this group","msg":"Нет данных"}}

    # TODO: [DELETE] /back/dp.xba_cook/profiles/groups/{profile_id}/{group_id}
    def case_xba_cook_profiles_groups_profile_id_group_id_delete(self):
        req = XbaCook(self.sess, self.host)
        prof_id = None
        group_id = None
        resp = req.xba_cook_profiles_groups_profile_id_group_id_delete(prof_id, group_id)
        print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # FIXME: mark.skip
    def case_xba_cook_profiles_groups_profile_id_group_id_weight_get(self):
        req = XbaCook(self.sess, self.host)
        # FIXME: хардкод
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
        prof_id = self._get_xba_profile_id()
        resp = req.xba_cook_profiles_start_id_get(prof_id)
        if resp.status_code == 400:
            assert resp.text == '{"error":{"code":400,"msg":"Задание уже запустили"}}\n', f"Ошибка, код {resp.status_code}, {resp.text}"
        else:
            assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # {"error":{"code":400,"msg":"Задание уже запустили"}}

    def case_xba_cook_profiles_stop_id_get(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self._get_xba_profile_id()
        resp = req.xba_cook_profiles_stop_id_get(prof_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_id_get(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self._get_xba_profile_id()
        resp = req.xba_cook_profiles_id_get(prof_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_id_post(self):
        # изменить xba_профиль
        req = XbaCook(self.sess, self.host)
        prof_id = self._get_xba_profile_id()

        data = _get_sample_xba_profile_data(self)
        data.update({"name": API_AUTO_TEST_ + "changed_" + get_str_random_num()})

        resp = req.xba_cook_profiles_id_post(prof_id, data)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # 400: {"error":{"code":400,"msg":"Пожалуйста, дождитесь окончания расчета профиля"}}

    def case_xba_cook_profiles_id_delete(self):
        req = XbaCook(self.sess, self.host)

        prof_id = self._get_xba_profile_id()

        xba_db_name = f"XBA_{prof_id}"
        # выдать права на изменение хранилища 'xba_db_name'
        PermitterCase().permitter_sysop_add_permission_to_change_db_by_name(xba_db_name)

        resp = req.xba_cook_profiles_id_delete(prof_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_id_graph_post(self):
        # DAT-5230
        req = XbaCook(self.sess, self.host)

        prof_id = self._get_xba_profile_id()    # status: запущен | выполнен
        data = {
            "start": "2022-10-21T16:39:01Z",
            "end": get_datetime_now_z(),
            # "entity": "?",
            # "entity_group": "?str(int)"
        }
        resp = req.xba_cook_profiles_id_graph_post(prof_id, data)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_id_log_last_get(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self._get_xba_profile_id()
        resp = req.xba_cook_profiles_id_log_last_get(prof_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_id_summary_post(self):
        # DAT-5211
        req = XbaCook(self.sess, self.host)
        prof_id = self._get_xba_profile_id()
        data = {
            "entity_group": "user",
            "start": "2023-02-09T00:00:00Z",
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
        prof_id = self._get_xba_profile_id()

        cur_whitelist_resp = req.xba_cook_profiles_id_form_whitelist_get(prof_id, "list")
        assert cur_whitelist_resp.status_code == 200, f"Ошибка, код {cur_whitelist_resp.status_code}, {cur_whitelist_resp.text}"
        cur_whitelist: list = json.loads(cur_whitelist_resp.text)['res']
        # print(f"cur_wl: {cur_whitelist}") # print(type(cur_whitelist)) >> list
        cur_whitelist.append({"name": API_AUTO_TEST_ + str_rand_num})

        data = {"data": cur_whitelist}
        resp = req.xba_cook_profiles_id_whitelist_post(prof_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_id_whitelist_element_post(self):
        req = XbaCook(self.sess, self.host)

        str_random_num = str(random.randint(100, 999))
        prof_id = self._get_xba_profile_id()

        data = {"data": API_AUTO_TEST_ + str_random_num}
        resp = req.xba_cook_profiles_id_whitelist_element_post(prof_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # fixme: # {"error":{"code":102,"msg":"Запущен перерасчёт профиля, изменение состояния недоступно"}}

    def case_xba_cook_profiles_id_zones_post(self):
        # DAT-5276
        req = XbaCook(self.sess, self.host)

        prof_id = self._get_xba_profile_id()
        data = {
            "start": "2022-02-09T00:00:00Z",
            "end": get_datetime_now_z(),
            # "entity_group": "other",  # str(int)
            # "zone": "red",     # todo: red|green|yellow
            # "zones": {
            #     "red_high": 3,
            #     "red_low": 3,
            #     "yellow_high": 2,
            #     "yellow_low": 2,
            #     "green_high": 1,
            #     "green_low": 1,
            # }
        }
        resp = req.xba_cook_profiles_id_zones_post(prof_id, data)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_id_string_whitelist_get(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self._get_xba_profile_id()
        form = "string"
        resp = req.xba_cook_profiles_id_form_whitelist_get(prof_id, form)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_id_list_whitelist_get(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self._get_xba_profile_id()
        form = "list"
        resp = req.xba_cook_profiles_id_form_whitelist_get(prof_id, form)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_profile_id_whitelist_element_id_delete(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self._get_xba_profile_id()

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
                        "email": _QA_SPAM_EMAIL,
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
        self._collect_xba_group_id()
        while len(xba_group_id) > 0:
            delete_req.xba_cook_profiles_groups_id_delete(xba_group_id.pop())

        self._collect_xba_profile_id_()
        while len(xba_profile_id) > 0:
            _pf_id = xba_profile_id.pop()
            xba_db_name = f"XBA_{_pf_id}"
            # выдать права на изменение хранилища 'xba_db_name'
            PermitterCase().permitter_sysop_add_permission_to_change_db_by_name(xba_db_name)
            delete_req.xba_cook_profiles_id_delete(_pf_id)
            # print(_pf_id)
