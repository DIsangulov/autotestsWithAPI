import json
import random

from req.Helpers.base_req import BaseReq

API_AUTO_TEST_ = "API_AUTO_TEST_"

profile_id = set()  # 'id' профиля xBA
group_id = set()    # 'id' метапрофиля // API_AUTO_TEST_x


class DbName:
    picker_tables = "picker_tables"     # FIXME: перевести на таблицу > like. API_TEST_DBx


class XbaCook(BaseReq):

    def _get_user_id(self) -> int:
        """Возвращает 'user_id' текущего пользователя"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.peopler/profile", headers=header, verify=False)
        dct = json.loads(resp.text)
        return dct['res']['user_id']

    def _get_db_id_by_name(self, db_name: str) -> int:
        """Возвращает 'id' хранилища с указанным именем"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/db", headers=header, verify=False)
        dct = json.loads(resp.text)
        db_info_rows = dct['res']
        db_info_row = next((db_info for db_info in db_info_rows if db_info['name'] == db_name), None)
        assert db_info_row is not None, f"Не удалось найти базу данных с именем {db_name}"

        db_id = db_info_row['id']

        return db_id

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

    def xba_cook_anomalies_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/anomalies", headers=header, verify=False)
        return resp

    def xba_cook_anomalies_picker_max_min_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/anomalies/picker/max_min", headers=header, verify=False)
        return resp

    def xba_cook_check_entity_type_post(self):
        db_picker_tables = self._get_db_id_by_name(DbName.picker_tables)
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
        data = {
            "start_datetime": "2023-02-01T00:00:00.000Z",
            "time_zone": "Europe/Moscow"
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/dashboard", headers=header, json=data, verify=False)
        return resp

    def xba_cook_entity_post(self):
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
        data = {
            "name": "user",
            "type": ""
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/entity/info", headers=header, json=data, verify=False)
        return resp

    def xba_cook_entity_info_settings_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/entity/info/settings", headers=header, verify=False)
        return resp

    def xba_cook_entity_info_settings_post(self):
        db_picker_tables = self._get_db_id_by_name(DbName.picker_tables)
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
        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.xba_cook/entity/info/settings/name", headers=header, verify=False)
        return resp

    def xba_cook_entity_picker_min_max_post(self):
        data = {
            "name": "user",
            "type": "user"
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/entity/picker/max_min", headers=header, json=data, verify=False)
        return resp

    def xba_cook_entity_risks_description_post(self):
        data = {"name": "shchetinin$@angaratech.ru",        # FIXME: хардкод
                "type": "user",
                "start": "2023-02-13T00:00:00Z",
                "end": "2023-02-14T00:00:00Z"}
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/entity/risks-description", headers=header, json=data, verify=False)
        return resp

    def xba_cook_max_min_post(self):
        db_picker_tables = self._get_db_id_by_name(DbName.picker_tables)
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
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles", headers=header, verify=False)

        # dct = json.loads(resp.text)
        # prof_id = dct['res'][2]['id']  # получили id профаила
        # print(resp.text)
        # print(f"prof_id is {prof_id}")
        return resp

    def xba_cook_profiles_post(self):
        # FIXME: редактировать заполнение
        str_random_num = str(random.randint(1000, 9999))
        db_picker_tables = self._get_db_id_by_name(DbName.picker_tables)
        data = {
            # "id": ???
            "name": API_AUTO_TEST_ + str_random_num,
            "description": None,
            "published": False,
            "opened": False,
            # "author_id": at_uid,
            "author_id": self._get_user_id(),
            "author": "Тест Апи",
            # "editor_id": at_uid,
            "editor_id": self._get_user_id(),
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
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/categories", headers=header, verify=False)
        return resp

    def xba_cook_profiles_export_profiles_post(self):
        prof_id = self._get_profile_id()
        data = {"profile_ids": [str(prof_id)]}
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/export_profiles", headers=header, json=data, verify=False)
        return resp

    def xba_cook_profiles_functions_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/functions", headers=header, verify=False)
        return resp

    def xba_cook_profiles_graph_drilldown_statement_id_post(self):
        prof_id = self._get_profile_id()
        data = {
            "columns": [
                ""
            ],
            "name": "",
            "time": "2022-12-06T08:36:09Z"
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/graph/drilldown/statement/" + str(prof_id), headers=header, json=data, verify=False)
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
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/graph/drilldown/" + str(prof_id), headers=header, json=data, verify=False)

        return resp

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
        prof_id = self._get_profile_id()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/graph/max_min/" + str(prof_id), headers=header, verify=False)
        return resp

    def xba_cook_profiles_graph_personal_id_post(self):
        prof_id = self._get_profile_id()

        data = {
            "end": "2023-02-14T00:00:00Z",
            "name": "",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/graph/personal/" + str(prof_id), headers=header, json=data, verify=False)
        return resp

    def xba_cook_profiles_graph_id_post(self):
        prof_id = self._get_profile_id()

        data = {
            "end": "2023-02-14T00:00:00Z",
            "name": "",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/graph/" + str(prof_id), headers=header, json=data, verify=False)
        return resp

    def xba_cook_profiles_groups_post(self):
        """Создание метапрофиля"""
        rand_num = random.randint(0, 9999)
        data = {
            "id": rand_num,
            "name": API_AUTO_TEST_ + str(rand_num),    # FIXME:
            "weight": ""
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/groups", headers=header, json=data, verify=False)
        return resp  # возвращает также ид новой группы

    def xba_cook_profiles_groups_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/groups", headers=header, verify=False)
        return resp

    def xba_cook_profiles_groups_put(self):
        """process PUT req for updating group name"""
        rand = random.randint(100, 999)
        _group_id = self._get_group_id()

        data = {
            "id": _group_id,
            "name": API_AUTO_TEST_ + "changed_" + str(rand),
            "weight": ""
        }
        header = {'token': self.token}
        resp = self.sess.put(f"{self.host}/back/dp.xba_cook/profiles/groups", headers=header, json=data, verify=False)
        return resp

    def xba_cook_profiles_groups_info_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/groups/info", headers=header, verify=False)
        return resp

    def xba_cook_profiles_groups_id_delete(self):
        _group_id = self._get_group_id()
        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.xba_cook/profiles/groups/" + str(_group_id), headers=header, verify=False)
        return resp

    def xba_cook_profiles_groups_group_id_profiles_get(self):
        _group_id = self._get_group_id()
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/groups/" + str(_group_id) + "/profiles", headers=header, verify=False)
        return resp

    def xba_cook_profiles_groups_id_post(self):
        _group_id = self._get_group_id()
        data = {
            "end": "2023-02-14T00:00:00Z",
            "name": "",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/groups/" + str(_group_id), headers=header, json=data, verify=False)
        return resp

    def xba_cook_profiles_groups_id_max_min_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/groups/2/max_min", headers=header, verify=False)
        return resp

    def xba_cook_profiles_groups_profile_id_group_id_weight_get(self):
        """process GET req to update profile weight in group"""
        # FIXME: хардкод
        prof_id = 1931
        group_id = 1493

        header = {'token': self.token}
        resp = self.sess.get(
            f"{self.host}/back/dp.xba_cook/profiles/groups/" + str(prof_id) + "/" + str(group_id) + "/2", headers=header, verify=False)
        return resp

    def xba_cook_profiles_import_profiles_post(self):
        str_rand_num = str(random.randint(1200, 12500))
        data = {
            "profile_list": [
                {
                    # "id": str_rand_num,         # FIXME: ??
                    "name": API_AUTO_TEST_ + str_rand_num,
                    "description": None,
                    "published": False,
                    "opened": False,
                    "author_id": self._get_user_id(),
                    # "author": "Ванин Юрий",
                    "editor_id": self._get_user_id(),
                    # "editor": "Ванин Юрий",
                    "created": "2023-02-15T07:55:02.631066Z",
                    "modified": "2023-02-15T07:55:02.631066Z",
                    "db_id": None,
                    "db_name": "picker_tables",     # FIXME: использовать другую таблицу?
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
        prof_id = self._get_profile_id()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/start/" + str(prof_id), headers=header, verify=False)
        return resp

    def xba_cook_profiles_stop_id_get(self):
        prof_id = self._get_profile_id()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/stop/" + str(prof_id), headers=header, verify=False)
        return resp

    def xba_cook_profiles_id_get(self):
        prof_id = self._get_profile_id()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/" + str(prof_id), headers=header, verify=False)
        return resp

    def xba_cook_profiles_id_delete(self):
        # FIXME: хардкод
        # FIXME: удаление профиля xBA, недостаточно прав
        prof_id = 2001

        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.xba_cook/profiles/" + str(prof_id), headers=header, verify=False)
        return resp

    def xba_cook_profiles_id_log_last_get(self):
        prof_id = self._get_profile_id()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/" + str(prof_id) + "/log/last", headers=header, verify=False)
        return resp

    def xba_cook_profiles_id_whitelist_post(self):
        """process POST req to add element into profile whitelist"""
        prof_id = self._get_profile_id()

        data = {"data": [{"name": "ApiTest"}]}      # FIXME: >> API_AUTO_TEST_
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/" + str(prof_id) + "/whitelist", json=data, headers=header, verify=False)
        return resp

    def xba_cook_profiles_id_whitelist_element_post(self):
        # FIXME: нельзя изменить в профиле, в котором идет "перерасчет" иначе
        # {"error":{"code":102,"msg":"Запущен перерасчёт профиля, изменение состояния недоступно"}}
        prof_id = self._get_profile_id()

        random_num = random.randint(0, 999)

        data = {"data": "ApiTest" + str(random_num)}        # FIXME:    >> API_AUTO_TEST_
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/" + str(prof_id) + "/whitelist/element", json=data, headers=header, verify=False)
        return resp

    def xba_cook_profiles_id_string_whitelist_get(self):
        prof_id = self._get_profile_id()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/" + str(prof_id) + "/string/whitelist", headers=header, verify=False)
        return resp

    # FIXME: swagger - нет описания
    def xba_cook_profiles_id_list_whitelist_get(self):
        prof_id = self._get_profile_id()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/" + str(prof_id) + "/list/whitelist", headers=header, verify=False)
        return resp

    def xba_cook_xba_get(self):
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
