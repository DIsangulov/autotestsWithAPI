import json
import random

from req.Helpers.base_req import BaseReq
from resourses.credentials import DbName

API_AUTO_TEST_ = "API_AUTO_TEST_"

profile_id = set()  # 'id' профиля xBA
group_id = set()    # 'id' метапрофиля // API_AUTO_TEST_x


class XbaCook(BaseReq):

    def _get_group_id(self) -> int:
        """get from global group_id : API_AUTO_TEST_x"""
        if len(group_id) == 0:
            resp_group_id_list = self.xba_cook_profiles_groups_get()        # запрос на список метапрофилей
            _group_id_rows = json.loads(resp_group_id_list.text)['res']
            for _row in _group_id_rows:
                if str(_row['name']).startswith(API_AUTO_TEST_):            # фильтрация по шаблону > добавление в group_id
                    group_id.add(int(_row['id']))

        if len(group_id) == 0:
            resp_new_group_id = self.xba_cook_profiles_groups_post()        # запрос на создание нового метапрофиля
            # FIXME: assert на status_code == 200
            new_group_id = json.loads(resp_new_group_id.text)['res']
            group_id.add(int(new_group_id))                                 # добавление 'id' нового метапрофиля в group_id

        return group_id.pop()                                               # возвращает случайное значение из group_id

    def _get_profile_id(self) -> int:
        """get from global profile_id : API_AUTO_TEST_x"""
        if len(profile_id) == 0:
            resp_profile_id_list = self.xba_cook_profiles_get()             # запрос на список профилей xBA
            _profile_id_rows = json.loads(resp_profile_id_list.text)['res']
            for _row in _profile_id_rows:
                if str(_row['name']).startswith(API_AUTO_TEST_):            # фильтр по шаблону > добавление в profile_id
                    profile_id.add(int(_row['id']))

        if len(profile_id) == 0:
            resp_new_profile_id = self.xba_cook_profiles_post()             # запрос на создание нового профиля xBA
            # FIXME: assert на status_code == 200
            new_profile_id = json.loads(resp_new_profile_id.text)['res']
            profile_id.add(int(new_profile_id))                             # добавление 'id' нового профиля xBA в profile_id

        return profile_id.pop()

    # FIXME: mark.skip
    def xba_cook_anomalies_get(self):
        """process GET req to get all app anomalies"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/anomalies", headers=header, verify=False)
        return resp

    def xba_cook_anomalies_picker_max_min_get(self):
        """process GET to get max and min date values"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/anomalies/picker/max_min", headers=header, verify=False)
        return resp

    def xba_cook_check_entity_type_post(self):
        """process POST for checking if entity type column contains not more distinct values than 20 & no nulls"""
        db_picker_tables = self.get_db_id_by_name(DbName.picker_tables)
        data = {
            "column": "1",
            # "db_id": pt_id,
            "db_id": db_picker_tables,
            "table": "ad_users_ngr"
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/check_entity_type", headers=header, json=data, verify=False)
        return resp

    def xba_cook_dashboard_post(self):
        """process POST req to get xba dashboard data"""
        data = {
            "start_datetime": "2023-02-01T00:00:00.000Z",
            "time_zone": "Europe/Moscow"
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/dashboard", headers=header, json=data, verify=False)
        return resp

    # TODO: [POST] /back/dp.xba_cook/dashboard/profiles

    def xba_cook_entity_post(self):
        """returns Entity card summary info and risk levels graph"""
        data = {
            "end": "",
            "name": "user",
            "start": "",
            "type": ""
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/entity", headers=header, json=data, verify=False)
        return resp

    def xba_cook_entity_details_post(self):
        """returns Entity card detailed info: risk levels pie chart, risk by profile table"""
        data = {
            "end": "",
            "name": "user",
            "start": "",
            "type": ""
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/entity/details", headers=header, json=data, verify=False)
        return resp

    def xba_cook_entity_info_post(self):
        """returns Entity card enrichment info (additional entity attributes from AD or DB-based dictionary)"""
        data = {
            "name": "user",
            "type": ""
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/entity/info", headers=header, json=data, verify=False)
        return resp

    def xba_cook_entity_info_settings_get(self):
        """returns Entity card enrichment settings"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/entity/info/settings", headers=header, verify=False)
        return resp

    def xba_cook_entity_info_settings_post(self):
        """process POST req to set Entity card enrichment settings."""
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
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/entity/info/settings", headers=header, json=data, verify=False)
        return resp

    def xba_cook_entity_info_settings_entity_type_delete(self):
        """process DELETE req to remove Entity card enrichment settings"""
        entity_type = "name"        # FIXME: какие ещё
        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.xba_cook/entity/info/settings/{entity_type}", headers=header, verify=False)
        return resp

    def xba_cook_entity_picker_max_min_post(self):
        """process GET to get max and min date values"""
        data = {
            "name": "user",
            "type": "user"
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/entity/picker/max_min", headers=header, json=data, verify=False)
        return resp

    def xba_cook_entity_risks_description_post(self):
        """returns Entity card summary info and risk levels graph"""
        data = {"name": "shchetinin$@angaratech.ru",        # FIXME: хардкод
                "type": "user",
                "start": "2023-02-13T00:00:00Z",
                "end": "2023-02-14T00:00:00Z"}
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/entity/risks-description", headers=header, json=data, verify=False)
        return resp

    def xba_cook_max_min_post(self):
        """process POST to get max and min column values"""
        db_picker_tables = self.get_db_id_by_name(DbName.picker_tables)
        data = {
            "column": "1",
            # "db_id": pt_id,
            "db_id": db_picker_tables,
            "table": "ad_users_ngr"
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/max_min", headers=header, json=data, verify=False)
        return resp

    def xba_cook_profiles_get(self):
        """process GET req to get profile list"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles", headers=header, verify=False)
        return resp

    def xba_cook_profiles_post(self):
        """process POST req to create new profile"""
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

        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles", headers=header, json=data, verify=False)
        return resp

    def xba_cook_profiles_categories_get(self):
        """process GET req to get profile categories"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/categories", headers=header, verify=False)
        return resp

    def xba_cook_profiles_export_profiles_post(self):
        """process POST req to get profile list by ids"""
        prof_id = self._get_profile_id()
        data = {"profile_ids": [prof_id]}
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/export_profiles", headers=header, json=data, verify=False)
        return resp

    def xba_cook_profiles_functions_get(self):
        """process GET req to get profile functions"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/functions", headers=header, verify=False)
        return resp

    def xba_cook_profiles_graph_drilldown_statement_id_post(self):
        """process POST to get statement for xba drilldown custom execution"""
        prof_id = self._get_profile_id()
        data = {
            "columns": [
                ""
            ],
            "name": "",
            "time": "2022-12-06T08:36:09Z"
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/graph/drilldown/statement/{prof_id}", headers=header, json=data, verify=False)
        return resp

    def xba_cook_profiles_graph_drilldown_id_post(self, prof_id=None, data=None):
        """process POST to get profile raw data (deep-personal level)"""

        # if prof_id is None: pass
        # if data is None:
        #     data = {
        #         "columns": [
        #             ""
        #         ],
        #         "name": "",
        #         "time": "2022-12-06T08:36:09Z"
        #     }

        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/graph/drilldown/{prof_id}", headers=header, json=data, verify=False)

        return resp

    # FIXME: вынести из набора интерфейсов
    def xba_cook_profiles_graph_drilldown_id_post_xx_descriprion_key_check(self):
        # https://tasks.ngrsoftlab.ru/browse/DAT-5184
        # Проверка наличия ключа "description" в ответе

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

        resp = self.xba_cook_profiles_graph_drilldown_id_post(prof_id, data)

        try:
            # отсутствие ключа на любом узле бросит ошибку "KeyError"
            json.loads(resp.text)['res']['info']['description']
        except KeyError:
            assert False, f"Ошибка, отсутствует ключ res>info>description в ответе, {resp.text}"

        return resp

    def xba_cook_profiles_max_min_id_get(self):
        """process GET to get profile data max and min date"""
        prof_id = self._get_profile_id()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/graph/max_min/{prof_id}", headers=header, verify=False)
        return resp

    def xba_cook_profiles_graph_personal_id_post(self):
        """process POST to get profile personal data (personal level)"""
        prof_id = self._get_profile_id()

        data = {
            "end": "2023-02-14T00:00:00Z",
            "name": "",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/graph/personal/{prof_id}", headers=header, json=data, verify=False)
        return resp

    def xba_cook_profiles_graph_id_post(self):
        """process GET to get profile data for visualisation on front"""
        prof_id = self._get_profile_id()

        data = {
            "end": "2023-02-14T00:00:00Z",
            "name": "",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/graph/{prof_id}", headers=header, json=data, verify=False)
        return resp

    def xba_cook_profiles_groups_get(self):
        """process GET req to get groups list"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/groups", headers=header, verify=False)
        return resp

    def xba_cook_profiles_groups_put(self):
        """process PUT req for updating group name"""
        rand_num = random.randint(100, 999)
        _group_id = self._get_group_id()

        data = {
            "id": _group_id,
            "name": API_AUTO_TEST_ + f"changed_{rand_num}",
            "weight": ""
        }
        header = {'token': self.token}
        resp = self.sess.put(f"{self.host}/back/dp.xba_cook/profiles/groups", headers=header, json=data, verify=False)
        return resp

    def xba_cook_profiles_groups_post(self):
        """process POST to create new group"""
        # Создание метапрофиля
        str_rand_num = str(random.randint(1000, 9999))
        data = {
            "id": str_rand_num,     # FIXME: используется?
            "name": API_AUTO_TEST_ + str_rand_num,
            "weight": ""
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/groups", headers=header, json=data, verify=False)
        return resp  # возвращает также ид новой группы

    def xba_cook_profiles_groups_info_get(self):
        """process GET req to get info"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/groups/info", headers=header, verify=False)
        return resp

    def xba_cook_profiles_groups_id_delete(self):
        """process DELETE to delete group"""
        _group_id = self._get_group_id()
        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.xba_cook/profiles/groups/{_group_id}", headers=header, verify=False)
        return resp

    def xba_cook_profiles_groups_group_id_profiles_get(self):
        """process GET req to get list of profiles of the group"""
        _group_id = self._get_group_id()
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/groups/{_group_id}/profiles", headers=header, verify=False)
        return resp

    def xba_cook_profiles_groups_id_post(self):
        """process GET to get profile group data for visualisation on front"""
        _group_id = self._get_group_id()
        data = {
            "end": "2023-02-14T00:00:00Z",
            "name": "",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/groups/{_group_id}", headers=header, json=data, verify=False)
        return resp

    # FIXME: _group_id = None # FIXME: @mark.skip
    def xba_cook_profiles_groups_id_max_min_get(self):
        """process GET to get profile group data max and min date"""
        _group_id = None

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/groups/{_group_id}/max_min", headers=header, verify=False)
        return resp

    # TODO: [DELETE] /back/dp.xba_cook/profiles/groups/{profile_id}/{group_id}

    # FIXME: mark.skip
    def xba_cook_profiles_groups_profile_id_group_id_weight_get(self):
        """process GET req to update profile weight in group"""
        # FIXME: хардкод
        prof_id = 1931
        group_id = 1493
        weight = 2

        header = {'token': self.token}
        resp = self.sess.get(
            f"{self.host}/back/dp.xba_cook/profiles/groups/{prof_id}/{group_id}/{weight}", headers=header, verify=False)
        return resp

    def xba_cook_profiles_import_profiles_post(self):
        """process POST to create new profiles"""
        str_rand_num = str(random.randint(1200, 12500))
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

        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/import_profiles", headers=header, json=data, verify=False)
        return resp

    def xba_cook_profiles_start_id_get(self):
        """process GET req to start profile by id"""
        prof_id = self._get_profile_id()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/start/{prof_id}", headers=header, verify=False)
        return resp

    def xba_cook_profiles_stop_id_get(self):
        """process GET req to stop profile by id"""
        prof_id = self._get_profile_id()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/stop/{prof_id}", headers=header, verify=False)
        return resp

    def xba_cook_profiles_id_get(self):
        """process GET req to get profile info by id"""
        prof_id = self._get_profile_id()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/{prof_id}", headers=header, verify=False)
        return resp

    # TODO: [POST] /back/dp.xba_cook/profiles/{id}
    # {"name":"tdasap1","db_id":2528,"table_name":"API_TEST_TABLE","author":"Ежов Сергей","author_id":4870,"editor":"Ежов Сергей","editor_id":4870,"created":"2023-06-29T07:14:11.117929Z","modified":"2023-06-29T07:48:38.692Z","id_function":1,"id_category":1,"group_info":null,"filter_settings":[{"field":"one","action":">","value":"10/10/1010 00:00:00","value_type":"DateTime"}],"profile_type":"median","status":3,"time_last_executed":"2023-06-29T07:14:12.198135Z","time_settings":{"time_column":"one","time_start":"1970-01-01T00:00:00.000Z","time_end":"1970-01-01T00:00:00.000Z","discretization_period":"week"},"entity_settings":{"entity_column":"one","entity_column_name":"other","entity_type":"one","additional_column":"","levels":{"level1":2,"level2":4,"level3":6,"level4":8}}}

    # FIXME: mark.skip
    def xba_cook_profiles_id_delete(self):
        """process DELETE to delete xBA Profile"""
        # FIXME: хардкод
        # FIXME: удаление профиля xBA, недостаточно прав
        prof_id = 2001

        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.xba_cook/profiles/{prof_id}", headers=header, verify=False)
        return resp

    # TODO: [POST] /back/dp.xba_cook/profiles/{id}/graph

    def xba_cook_profiles_id_log_last_get(self):
        """process GET req to get profile last log by profile id"""
        prof_id = self._get_profile_id()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/{prof_id}/log/last", headers=header, verify=False)
        return resp

    # TODO: [POST] /back/dp.xba_cook/profiles/{id}/summary

    def xba_cook_profiles_id_whitelist_post(self):
        """process POST req to add element into profile whitelist"""
        prof_id = self._get_profile_id()

        data = {"data": [{"name": API_AUTO_TEST_ + "name"}]}      # FIXME: old: ApiTest; ?+ rand_num
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/{prof_id}/whitelist", json=data, headers=header, verify=False)
        return resp

    def xba_cook_profiles_id_whitelist_element_post(self):
        """process POST req to add element into profile whitelist"""
        # FIXME: нельзя изменить в профиле, в котором идет "перерасчет" иначе
        # {"error":{"code":102,"msg":"Запущен перерасчёт профиля, изменение состояния недоступно"}}
        prof_id = self._get_profile_id()

        str_random_num = str(random.randint(100, 999))

        data = {"data": API_AUTO_TEST_ + str_random_num}
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/{prof_id}/whitelist/element", json=data, headers=header, verify=False)
        return resp

    # TODO: [POST] /back/dp.xba_cook/profiles/{id}/zones

    # == {id}/{form} ====================================================

    # TODO: [GET] /back/dp.xba_cook/profiles/{id}/{form}/whitelist

    def xba_cook_profiles_id_string_whitelist_get(self):
        prof_id = self._get_profile_id()
        # FIXME: {form} = string

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/{prof_id}/string/whitelist", headers=header, verify=False)
        return resp

    def xba_cook_profiles_id_list_whitelist_get(self):
        prof_id = self._get_profile_id()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/{prof_id}/list/whitelist", headers=header, verify=False)
        return resp

    # == {id}/{form} ====================================================

    # TODO: [DELETE] /back/dp.xba_cook/profiles/{profile_id}/whitelist/element/{id}

    # TODO: [POST] /back/dp.xba_cook/set_log_level_xba_py/{mode}

    def xba_cook_xba_get(self):
        """process GET req to get current syslog-mailing-alert xba settings."""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/xba", headers=header, verify=False)
        return resp

    def xba_cook_xba_post(self):
        """process POST req to set new syslog-mailing-alert xba settings"""
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

        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/xba", json=data, headers=header, verify=False)
        return resp
