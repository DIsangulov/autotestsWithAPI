import json
import random

from req.Helpers.user_session import UserSession
from req.Api.req_xba_cook import XbaCook
from resourses.credentials import DbName

API_AUTO_TEST_ = "API_AUTO_TEST_"

profile_id = set()  # 'id' профиля xBA
group_id = set()    # 'id' метапрофиля // API_AUTO_TEST_x


class XbaCookCase(UserSession):

    # fixme: add collect
    def _get_group_id(self) -> int:
        """get from global group_id : API_AUTO_TEST_x"""
        if len(group_id) == 0:
            resp_group_id_list = self.case_xba_cook_profiles_groups_get()        # запрос на список метапрофилей
            _group_id_rows = json.loads(resp_group_id_list.text)['res']
            for _row in _group_id_rows:
                if str(_row['name']).startswith(API_AUTO_TEST_):            # фильтрация по шаблону > добавление в group_id
                    group_id.add(int(_row['id']))

        if len(group_id) == 0:
            resp_new_group_id = self.case_xba_cook_profiles_groups_post()        # запрос на создание нового метапрофиля
            # FIXME: assert на status_code == 200
            new_group_id = json.loads(resp_new_group_id.text)['res']
            group_id.add(int(new_group_id))                                 # добавление 'id' нового метапрофиля в group_id

        return group_id.pop()                                               # возвращает случайное значение из group_id

    # fixme: add _collect
    def _get_profile_id(self) -> int:
        """get from global profile_id : API_AUTO_TEST_x"""
        if len(profile_id) == 0:
            resp_profile_id_list = self.case_xba_cook_profiles_get()             # запрос на список профилей xBA
            _profile_id_rows = json.loads(resp_profile_id_list.text)['res']
            for _row in _profile_id_rows:
                if str(_row['name']).startswith(API_AUTO_TEST_):            # фильтр по шаблону > добавление в profile_id
                    profile_id.add(int(_row['id']))

        if len(profile_id) == 0:
            resp_new_profile_id = self.case_xba_cook_profiles_post()             # запрос на создание нового профиля xBA
            # FIXME: assert на status_code == 200
            new_profile_id = json.loads(resp_new_profile_id.text)['res']
            profile_id.add(int(new_profile_id))                             # добавление 'id' нового профиля xBA в profile_id

        return profile_id.pop()

    # FIXME: mark.skip  timeout
    def case_xba_cook_anomalies_get(self):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_anomalies_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

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
        # print(resp.text)

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
        data = {
            "user_settings":
            {
                # "db_id": pt_id,
                "db_id": db_picker_tables,
                "db_name": "picker_tables",
                "table_name": "ad_users_ngr",
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
        return resp

    def case_xba_cook_profiles_post(self):
        req = XbaCook(self.sess, self.host)
        # FIXME: редактировать заполнение
        str_random_num = str(random.randint(1000, 9999))
        self_user_id = self.get_self_user_id()
        db_picker_tables = self.get_db_id_by_name(DbName.picker_tables)
        data = {
            # "id": ???
            "name": API_AUTO_TEST_ + str_random_num,
            "description": None,
            "published": False,
            "opened": False,
            # "author_id": at_uid,
            "author_id": self_user_id,
            "author": "Тест Апи",
            # "editor_id": at_uid,
            "editor_id": self_user_id,
            "editor": "Тест Апи",
            "created": "2023-02-15T07:55:02.631066Z",
            "modified": "2023-02-15T07:55:02.631066Z",
            # "db_id": pt_id,
            "db_id": db_picker_tables,
            "db_name": DbName.picker_tables,     # FIXME: возможно, стоит использовать другую таблицу
            "table_name": "ad_users_ngr",
            "status": 3,
            "profile_type": "median",
            "id_function": 6,
            "id_category": 1,
            "time_settings":
                {
                    "time_column": "badPasswordTime",
                    "time_start": "1971-01-01T00:00:00Z",
                    "time_end": "2022-12-06T08:36:09Z",
                    "discretization_period": "minute",
                    "stat_period": ""
                },
            "entity_settings":
                {
                    "entity_column": "Enabled",
                    "entity_column_name": "user",
                    "entity_type": "Enabled",
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
            "time_last_executed": "2023-02-15T07:55:03.838988Z",
            "log_last_executed": "",
            "group_info": None
        }
        resp = req.xba_cook_profiles_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        return resp

    def case_xba_cook_profiles_categories_get(self):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_profiles_categories_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_export_profiles_post(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self._get_profile_id()
        data = {"profile_ids": [prof_id]}
        resp = req.xba_cook_profiles_export_profiles_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_functions_get(self):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_profiles_functions_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_graph_drilldown_statement_id_post(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self._get_profile_id()
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
        # if prof_id is None: pass
        # if data is None:
        #     data = {
        #         "columns": [
        #             ""
        #         ],
        #         "name": "",
        #         "time": "2022-12-06T08:36:09Z"
        #     }
        prof_id = None
        data = None
        resp = req.xba_cook_profiles_graph_drilldown_id_post(prof_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_graph_drilldown_1888_post(self):
        # https://tasks.ngrsoftlab.ru/browse/DAT-5184
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
        prof_id = self._get_profile_id()
        resp = req.xba_cook_profiles_max_min_id_get(prof_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_graph_personal_id_post(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self._get_profile_id()
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
        prof_id = self._get_profile_id()
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
        return resp

    def case_xba_cook_profiles_groups_put(self):
        req = XbaCook(self.sess, self.host)
        rand_num = random.randint(100, 999)
        _group_id = self._get_group_id()
        data = {
            "id": _group_id,
            "name": API_AUTO_TEST_ + f"changed_{rand_num}",
            "weight": ""
        }
        resp = req.xba_cook_profiles_groups_put(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_groups_post(self):
        req = XbaCook(self.sess, self.host)
        str_rand_num = str(random.randint(1000, 9999))
        data = {
            "id": str_rand_num,     # FIXME: используется?
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
        _group_id = self._get_group_id()
        resp = req.xba_cook_profiles_groups_id_delete(_group_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_groups_group_id_profiles_get(self):
        req = XbaCook(self.sess, self.host)
        _group_id = self._get_group_id()
        resp = req.xba_cook_profiles_groups_group_id_profiles_get(_group_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # fixme: # нужен group_id хотя бы с одним пользователем
    def case_xba_cook_profiles_groups_id_post(self):
        req = XbaCook(self.sess, self.host)
        _group_id = self._get_group_id()
        data = {
            "end": "2023-02-14T00:00:00Z",
            "name": "",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        resp = req.xba_cook_profiles_groups_id_post(_group_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # FIXME: _group_id = None # FIXME: @mark.skip
    def case_xba_cook_profiles_groups_id_max_min_get(self):
        req = XbaCook(self.sess, self.host)
        _group_id = None
        resp = req.xba_cook_profiles_groups_id_max_min_get(_group_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # FIXME: mark.skip
    def case_xba_cook_profiles_groups_profile_id_group_id_weight_get(self):
        req = XbaCook(self.sess, self.host)
        # FIXME: хардкод
        prof_id = 1931
        group_id = 1493
        weight = 2
        resp = req.xba_cook_profiles_groups_profile_id_group_id_weight_get(prof_id, group_id, weight)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_import_profiles_post(self):
        req = XbaCook(self.sess, self.host)
        str_rand_num = str(random.randint(7000, 9999))
        self_user_id = self.get_self_user_id()
        data = {
            "profile_list": [
                {
                    # "id": str_rand_num,         # FIXME: ??
                    "name": API_AUTO_TEST_ + str_rand_num,
                    "description": None,
                    "published": False,
                    "opened": False,
                    "author_id": self_user_id,
                    "editor_id": self_user_id,
                    "created": "2023-02-15T07:55:02.631066Z",
                    "modified": "2023-02-15T07:55:02.631066Z",
                    "db_id": None,
                    "db_name": DbName.picker_tables,     # FIXME: использовать другую таблицу?
                    "table_name": "ad_users_ngr",
                    "status": 3,
                    "profile_type": "median",
                    "id_function": 6,
                    "id_category": 1,
                    "time_settings":
                        {
                            "time_column": "badPasswordTime",
                            "time_start": "1971-01-01T00:00:00Z",
                            "time_end": "2022-12-06T08:36:09Z",
                            "discretization_period": "minute",
                            "stat_period": ""
                        },
                    "entity_settings":
                        {
                            "entity_column": "Enabled",
                            "entity_column_name": "user",
                            "entity_type": "Enabled",
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
                    "time_last_executed": None,
                    "log_last_executed": "",
                    "group_info": None
                }
            ]
        }
        resp = req.xba_cook_profiles_import_profiles_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_start_id_get(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self._get_profile_id()
        resp = req.xba_cook_profiles_start_id_get(prof_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_stop_id_get(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self._get_profile_id()
        resp = req.xba_cook_profiles_stop_id_get(prof_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_id_get(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self._get_profile_id()
        resp = req.xba_cook_profiles_id_get(prof_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # [POST] /back/dp.xba_cook/profiles/{id}
    # {"name":"tdasap1","db_id":2528,"table_name":"API_TEST_TABLE","author":"Ежов Сергей","author_id":4870,"editor":"Ежов Сергей","editor_id":4870,"created":"2023-06-29T07:14:11.117929Z","modified":"2023-06-29T07:48:38.692Z","id_function":1,"id_category":1,"group_info":null,"filter_settings":[{"field":"one","action":">","value":"10/10/1010 00:00:00","value_type":"DateTime"}],"profile_type":"median","status":3,"time_last_executed":"2023-06-29T07:14:12.198135Z","time_settings":{"time_column":"one","time_start":"1970-01-01T00:00:00.000Z","time_end":"1970-01-01T00:00:00.000Z","discretization_period":"week"},"entity_settings":{"entity_column":"one","entity_column_name":"other","entity_type":"one","additional_column":"","levels":{"level1":2,"level2":4,"level3":6,"level4":8}}}

    # FIXME: mark.skip
    def case_xba_cook_profiles_id_delete(self):
        req = XbaCook(self.sess, self.host)

        # FIXME: хардкод
        # FIXME: удаление профиля xBA, недостаточно прав
        prof_id = 2001
        resp = req.xba_cook_profiles_id_delete(prof_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_id_log_last_get(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self._get_profile_id()
        resp = req.xba_cook_profiles_id_log_last_get(prof_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_id_whitelist_post(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self._get_profile_id()
        data = {"data": [{"name": API_AUTO_TEST_ + "name"}]}      # FIXME: old: ApiTest; ?+ rand_num
        resp = req.xba_cook_profiles_id_whitelist_post(prof_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_id_whitelist_element_post(self):
        req = XbaCook(self.sess, self.host)
        # FIXME: нельзя изменить в профиле, в котором идет "перерасчет" иначе
        # {"error":{"code":102,"msg":"Запущен перерасчёт профиля, изменение состояния недоступно"}}
        prof_id = self._get_profile_id()

        str_random_num = str(random.randint(100, 999))

        data = {"data": API_AUTO_TEST_ + str_random_num}
        resp = req.xba_cook_profiles_id_whitelist_element_post(prof_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_id_string_whitelist_get(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self._get_profile_id()
        form = "string"
        resp = req.xba_cook_profiles_id_form_whitelist_get(prof_id, form)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_profiles_id_list_whitelist_get(self):
        req = XbaCook(self.sess, self.host)
        prof_id = self._get_profile_id()
        form = "list"
        resp = req.xba_cook_profiles_id_form_whitelist_get(prof_id, form)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_xba_get(self):
        req = XbaCook(self.sess, self.host)
        resp = req.xba_cook_xba_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_xba_cook_xba_post(self):
        req = XbaCook(self.sess, self.host)
        data = {
            "res":
                {
                    "XMLName":
                        {
                            "Space": "",
                            "Local": "xba"
                        },
                    "destinations":
                        [
                            {
                                "email": "y.vanin@ngrsoftlab.ru",   # FIXME:
                                "syslog_host": "127.0.0.1",
                                "syslog_port": 514,
                                "syslog_protocol": "udp",
                                "disable_syslog": False,
                                "disable_email": False
                            },
                            {
                                "email": "",
                                "syslog_host": "1.12.3.22",
                                "syslog_port": 333,
                                "syslog_protocol": "tcp",
                                "disable_syslog": False,
                                "disable_email": True
                            },
                            {
                                "email": "",
                                "syslog_host": "2.212.23.31",
                                "syslog_port": 33,
                                "syslog_protocol": "tcp",
                                "disable_syslog": False,
                                "disable_email": True
                            }
                        ]
                }
        }
        resp = req.xba_cook_xba_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

