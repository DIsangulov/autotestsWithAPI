import json
import random

from req.Helpers.base_req import BaseReq
from resourses.credentials import DpQaa


class XbaCook(BaseReq):

    def _id_picker_tables_get(self) -> int:  # забираем id таблицы picker_table
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/db", headers=header, verify=False)
        json_data = json.loads(resp.text)
        pt_id = None
        for item in json_data['res']:
            if item['name'] == 'picker_tables':
                pt_id = item['id']
        # print(f"pt_id = {pt_id}")
        return pt_id

    def _at_uid_get(self) -> int:
        """Получить id пользователя датаплан"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.peopler/users", headers=header, verify=False)
        # name = 'dataplan_qaa@ngrsoftlab.ru'
        name = DpQaa.USER
        users = json.loads(resp.text)['res']
        uid = next((user for user in users if user['name'] == name), None)

        at_uid = uid['id']
        return at_uid

    def _get_random_group_id(self) -> int:
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/groups", headers=header, verify=False)
        dct = json.loads(resp.text)
        group_id = dct['res'][-1]['id']  # получили id группы
        return group_id

    def _get_random_profile_id(self) -> int:
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles", headers=header, verify=False)

        dct = json.loads(resp.text)
        prof_id = dct['res'][2]['id']  # получили id профаила
        # print(resp.text)
        # print(f"prof_id is {prof_id}")
        return prof_id

    def xba_cook_anomalies_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/anomalies", headers=header, verify=False)
        return resp

    def xba_cook_anomalies_picker_max_min_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/anomalies/picker/max_min", headers=header, verify=False)
        return resp

    def xba_cook_check_entity_type_post(self):
        data = {
            "column": "1",
            # "db_id": pt_id,
            "db_id": self._id_picker_tables_get(),
            "table": "ad_users_ngr"
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/check_entity_type", headers=header, json=data,
                              verify=False)
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
        data = {
            "user_settings":
            {
                # "db_id": pt_id,
                "db_id": self._id_picker_tables_get(),
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
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/entity/picker/max_min", headers=header, json=data,
                              verify=False)
        return resp

    def xba_cook_entity_risks_description_post(self):
        data = {"name": "shchetinin$@angaratech.ru",
                "type": "user",
                "start": "2023-02-13T00:00:00Z",
                "end": "2023-02-14T00:00:00Z"}
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/entity/risks-description", headers=header, json=data,
                              verify=False)
        return resp

    def xba_cook_max_min_post(self):
        data = {
            "column": "1",
            # "db_id": pt_id,
            "db_id": self._id_picker_tables_get(),
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
        prof_id = self._get_random_profile_id()
        data = {
            "id": str(prof_id) + str(1),
            "name": "123",
            "description": None,
            "published": False,
            "opened": False,
            # "author_id": at_uid,
            "author_id": self._at_uid_get(),
            "author": "Тест Апи",
            # "editor_id": at_uid,
            "editor_id": self._at_uid_get(),
            "editor": "Тест Апи",
            "created": "2023-02-15T07:55:02.631066Z",
            "modified": "2023-02-15T07:55:02.631066Z",
            # "db_id": pt_id,
            "db_id": self._id_picker_tables_get(),
            "db_name": "picker_tables",
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
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles", headers=header, json=data, verify=False)
        return resp

    def xba_cook_profiles_categories_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/categories", headers=header, verify=False)
        return resp

    def xba_cook_profiles_export_profiles_post(self):
        prof_id = self._get_random_profile_id()
        data = {"profile_ids": [str(prof_id)]}
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/export_profiles", headers=header, json=data,
                              verify=False)
        return resp

    def xba_cook_profiles_functions_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/functions", headers=header, verify=False)
        return resp

    def xba_cook_profiles_graph_drilldown_statement_id_post(self):
        prof_id = self._get_random_profile_id()
        data = {
            "columns": [
                ""
            ],
            "name": "",
            "time": "2022-12-06T08:36:09Z"
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/graph/drilldown/statement/" + str(prof_id),
                              headers=header, json=data, verify=False)
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
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/graph/drilldown/" + str(prof_id), headers=header,
                              json=data, verify=False)

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
        prof_id = self._get_random_profile_id()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/graph/max_min/" + str(prof_id), headers=header,
                             verify=False)
        return resp

    def xba_cook_profiles_graph_personal_id_post(self):
        prof_id = self._get_random_profile_id()

        data = {
            "end": "2023-02-14T00:00:00Z",
            "name": "",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/graph/personal/" + str(prof_id), headers=header,
                              json=data, verify=False)
        return resp

    def xba_cook_profiles_graph_id_post(self):
        prof_id = self._get_random_profile_id()

        data = {
            "end": "2023-02-14T00:00:00Z",
            "name": "",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/graph/" + str(prof_id), headers=header,
                              json=data, verify=False)
        return resp

    def xba_cook_profiles_groups_post(self):
        """Создание метапрофиля"""
        rand_num = random.randint(0, 9999)
        data = {
            "id": rand_num,
            "name": "F_auto_group_" + str(rand_num),
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
        rand = random.randint(1200, 12500)

        group_id = 1496  # FIXME: хардкод

        data = {
            "id": group_id,
            "name": "F_auto_name_changed_" + str(rand),
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
        group_id = None  # FIXME: удаление после создания шаблонистой группы
        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.xba_cook/profiles/groups/" + str(group_id), headers=header,
                                verify=False)
        return resp

    def xba_cook_profiles_groups_group_id_profiles_get(self):
        group_id = self._get_random_group_id()
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/groups/" + str(group_id) + "/profiles",
                             headers=header, verify=False)
        return resp

    def xba_cook_profiles_groups_id_post(self):
        group_id = self._get_random_group_id()
        data = {
            "end": "2023-02-14T00:00:00Z",
            "name": "",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/groups/" + str(group_id), headers=header,
                              json=data, verify=False)
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
            f"{self.host}/back/dp.xba_cook/profiles/groups/" + str(prof_id) + "/" + str(group_id) + "/2",
            headers=header, verify=False)
        return resp

    def xba_cook_profiles_import_profiles_post(self):
        rand = random.randint(1200, 12500)
        data = {
            "profile_list": [
                {
                    "id": rand,
                    "name": str(rand),
                    "description": None,
                    "published": False,
                    "opened": False,
                    # "author_id": at_uid,
                    "author_id": self._at_uid_get(),
                    "author": "Ванин Юрий",
                    # "editor_id": at_uid,
                    "editor_id": self._at_uid_get(),
                    "editor": "Ванин Юрий",
                    "created": "2023-02-15T07:55:02.631066Z",
                    "modified": "2023-02-15T07:55:02.631066Z",
                    "db_id": None,
                    "db_name": "picker_tables",
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
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/import_profiles", headers=header,
                              json=data, verify=False)
        return resp

    def xba_cook_profiles_start_id_get(self):
        prof_id = self._get_random_profile_id()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/start/" + str(prof_id), headers=header,
                             verify=False)
        return resp

    def xba_cook_profiles_stop_id_get(self):
        prof_id = self._get_random_profile_id()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/stop/" + str(prof_id), headers=header,
                             verify=False)
        return resp

    def xba_cook_profiles_id_get(self):
        prof_id = self._get_random_profile_id()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/" + str(prof_id), headers=header, verify=False)
        return resp

    def xba_cook_profiles_id_delete(self):
        # FIXME: удаление профиля xBA, недостаточно прав
        prof_id = None

        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.xba_cook/profiles/" + str(prof_id), headers=header, verify=False)
        return resp

    def xba_cook_profiles_id_log_last_get(self):
        prof_id = self._get_random_profile_id()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/" + str(prof_id) + "/log/last", headers=header,
                             verify=False)
        return resp

    def xba_cook_profiles_id_whitelist_post(self):
        prof_id = self._get_random_profile_id()

        data = {"data": [{"name": "ApiTest"}]}
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/" + str(prof_id) + "/whitelist", json=data,
                              headers=header, verify=False)
        return resp

    def xba_cook_profiles_id_whitelist_element_post(self):
        # FIXME: нельзя изменить в профиле, в котором идет "перерасчет" иначе
        # {"error":{"code":102,"msg":"Запущен перерасчёт профиля, изменение состояния недоступно"}}
        prof_id = self._get_random_profile_id()

        random_num = random.randint(0, 999)

        data = {"data": "ApiTest" + str(random_num)}
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/" + str(prof_id) + "/whitelist/element",
                              json=data, headers=header, verify=False)
        return resp

    def xba_cook_profiles_id_string_whitelist_get(self):
        prof_id = self._get_random_profile_id()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/" + str(prof_id) + "/string/whitelist",
                             headers=header, verify=False)
        return resp

    def xba_cook_profiles_id_list_whitelist_get(self):
        prof_id = self._get_random_profile_id()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/" + str(prof_id) + "/list/whitelist",
                             headers=header, verify=False)
        return resp

    def xba_cook_xba_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/xba", headers=header, verify=False)
        return resp

    def xba_cook_xba_post(self):
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
                                "email": "y.vanin@ngrsoftlab.ru",
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
