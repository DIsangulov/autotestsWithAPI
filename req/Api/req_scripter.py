import json
import random

import requests

from req.Helpers.base_req import BaseReq

API_AUTO_TEST_ = "API_AUTO_TEST_"

script_id = []          # 'id' скрипта  # предполагается, что будут использоваться только скрипты с именем .startswith(API_AUTO_TEST_%)
sequence_id = []        # 'id' последовательности


class Scripter(BaseReq):

    def _get_script_id(self) -> int:
        if len(script_id) == 0:                             # global script_id # id скрипта
            self.scripter_script_get()                      # запрос на наличие подходящих 'script_id'
            # FIXME: если подходящих скриптов нет, создавать один из них
            # self.создать_новый_скрипт_post()
        return script_id[-1]

    def _get_sequence_id(self) -> int:
        if len(sequence_id) == 0:                           # global sequence_id # id последовательности
            self.scripter_sequence_get()                    # запрос на наличие подходящих 'sequence_id'
            # FIXME: если подходящих последовательностей нет, создавать одну из них
            # self.создать_новую_последовательность()
        return sequence_id[-1]

    def _get_log_id(self, _script_id: int) -> int:
        # лог есть у скрипта, который запускался хоть один раз || {"res":null}

        # запрос на получение логов у скрипта _script_id
        log_resp = self.scripter_script_id_log_get(_script_id)
        # {"res":null}
        # {"res":[{"id":359949,"name":"","start":"2023-06-22T14:44:53.544363Z","status":"выполнен",...

        # проверка на результат != null
        if log_resp.text == '{"res":null}\n':
            self.scripter_script_start_post(_script_id)             # запускаем скрипт _script_id
            # FIXME: нужно ли дожидаться исполнения скрипта?
            log_resp = self.scripter_script_id_log_get(_script_id)  # повторный запрос на наличие логов
            # FIXME: кинуть ещё одну проверку logs != null; вообще, скрипт может и не исполниться, логов не будет тогда снова

        dct = json.loads(log_resp.text)
        log_id = dct['res'][-1]['id']

        return log_id

    def scripter_category_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/category", headers=header, verify=False)
        # {"res":[{"name":"Аналитические","path":"analitycs"},{"name":"Парсеры","path":"parsers"},{"name":"Служебные","path":"service"}]}
        return resp

    def scripter_libs_get(self):
        # исп: front>при создании скрипта>возвращает список "Разрешенные пакеты и библиотеки python"
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/libs", headers=header, verify=False)
        return resp

    def scripter_script_post(self):
        """process POST to create new script"""
        rand_num = random.randint(0, 999)
        data = {
            # "author": "dataplan_qaa@ngrsoftlab.ru",
            # "author": "Владимир Даль",
            "name": API_AUTO_TEST_ + str(rand_num),
            "description": API_AUTO_TEST_ + str(rand_num),
            "type": True,
            "category": 1,
            "keys": [],
            "node": 0,
            "encrypt": False,
            "encapsulate": False,
            "main_file": {
                "file_data": "print ('Test')",
                "file_name": "script.py"
            },
            "additional_files": [],
            # "author_id": at_uid
            "author_id": self.get_self_user_id()
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.scripter/script", headers=header, json=data, verify=False)
        return resp

    def scripter_script_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script", headers=header, verify=False)

        script_info_rows = json.loads(resp.text)['res']

        # вывести список всех script_info
        # for _row in script_info_rows:
        #     print(_row)

        # FIXME: assert на ответ, иначе ключа "name" может и не быть
        for sc_info_row in script_info_rows:
            if str(sc_info_row["name"]).startswith(API_AUTO_TEST_):
                # print(sc_info_row)
                script_id.append(sc_info_row['id'])     # global: script_id

        # print(f"script_id list: {script_id}")
        return resp

    def scripter_script_put(self):

        _script_id = self._get_script_id()
        data = {
            "type": True,
            # "editor_id": at_uid,
            "editor_id": self.get_self_user_id(),
            "id": _script_id,
            "name": "TestAPIscripter1",
            "description": "TestAPIscripter",
            "category": 1,
            "keys": [
                {
                    "1": "2"
                }
            ],
            "node": 0,
            "encrypt": False,
            "encapsulate": False
        }
        header = {'token': self.token}
        resp = self.sess.put(f"{self.host}/back/dp.scripter/script", headers=header, json=data, verify=False)
        return resp

    def scripter_script_exec_list_get(self):
        """process GET to get list of all scripts with access level exec"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/exec_list", headers=header, verify=False)
        return resp

    def scripter_script_id_get(self):
        _script_id = self._get_script_id()
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/" + str(_script_id), headers=header, verify=False)
        # print(resp.text)
        return resp

    def scripter_script_start_post(self, _script_id: int = None):
        """process POST req to start script (if not started and user have rights for that)"""

        if _script_id is None:
            _script_id = self._get_script_id()

        data = {
            "id": str(_script_id),
            "node": 0,
            "keys": [
                {
                    "keys": [{"CPU": 40}, {"RAM": 40}]
                }
            ]
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.scripter/script/start", headers=header, json=data, verify=False)
        return resp

    # FIXME: {"error":{"code":400,"msg":"Задание не было запущено"}}
    def scripter_script_stop_id_get(self):
        _script_id = self._get_script_id()
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/stop/" + str(_script_id), headers=header, verify=False)
        return resp

    def scripter_script_id_files_get(self):
        _script_id = self._get_script_id()
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/" + str(_script_id) + "/files", headers=header, verify=False)
        return resp

    def scripter_script_id_files_put(self):
        _script_id = self._get_script_id()
        data = {
            "additional_files": [
                {
                    "file_data": "print('Test Scripter1')",
                    "file_name": "testScripter1.py"
                }
            ],
            "main_file": {
                "file_data": "print('Test Scripter')",
                "file_name": "testScripter.py"
            }
        }
        header = {'token': self.token}
        resp = self.sess.put(f"{self.host}/back/dp.scripter/script/" + str(_script_id) + "/files", headers=header, json=data, verify=False)
        return resp

    def scripter_script_id_log_get(self, _script_id: int = None) -> requests.Response:

        if _script_id is None:
            _script_id = self._get_script_id()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/" + str(_script_id) + "/log", headers=header, verify=False)

        # print(resp.text)    # если скрипт '_script_id' не запускался >> {"res":null}
        return resp

    def scripter_script_id_log_delete(self):
        """process DELETE to delete all script logs from now"""
        _script_id = self._get_script_id()

        # {"error":{"code":400,"description":"sql: no rows in result set","msg":"Ошибка выборки из бд"}}
        # При отсутствии логов; запускаю скрипт '_script_id', чтобы появилась строка логов
        self.scripter_script_start_post(_script_id)     # запрос на старт исполнения скрипта '_script_id'
        # FIXME: ждать, пока скрипт исполнится?

        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.scripter/script/" + str(_script_id) + "/log", headers=header, verify=False)
        return resp

    def scripter_script_id_log_last_get(self):
        _script_id = self._get_script_id()

        # {"error":{"code":400,"description":"sql: no rows in result set","msg":"Ошибка выборки из бд"}}
        # При отсутствии логов; запускаю скрипт '_script_id', чтобы появилась строка логов
        self.scripter_script_start_post(_script_id)     # запрос на старт исполнения скрипта '_script_id'
        # FIXME: ждать, пока скрипт исполнится?

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/" + str(_script_id) + "/log/last", headers=header, verify=False)
        return resp

    def scripter_script_script_id_log_log_id_get(self):
        _script_id = self._get_script_id()
        _log_id = self._get_log_id(_script_id)

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/" + str(_script_id) + "/log/" + str(_log_id), headers=header, verify=False)
        return resp

    def scripter_script_script_id_log_log_id_delete(self):
        _script_id = self._get_script_id()
        _log_id = self._get_log_id(_script_id)

        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.scripter/script/" + str(_script_id) + "/log/" + str(_log_id), headers=header, verify=False)

        # print(f"Был удален лог: {_log_id}")
        return resp

    def scripter_script_id_delete(self):
        _script_id = self._get_script_id()
        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.scripter/script/" + str(_script_id), headers=header, verify=False)
        return resp

    def scripter_script_type_admin_get(self):
        # исп: получить список скриптов "Административные"
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/admin", headers=header, verify=False)
        return resp

    def scripter_script_type_user_get(self):
        # исп: получить список скриптов "Пользовательские"
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/user", headers=header, verify=False)
        return resp

    def scripter_sequence_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/sequence", headers=header, verify=False)

        sequence_info_rows = json.loads(resp.text)['res']

        # вывести все строки скрипты>>"Последовательности"
        # for _row in sequence_info_rows:
        #     print(_row)

        # FIXME: assert на ответ, иначе ключа "name" может и не быть
        for _row in sequence_info_rows:
            if str(_row["name"]).startswith(API_AUTO_TEST_):
                # print(_row)
                sequence_id.append(_row['id'])     # global: sequence_id

        return resp

    def scripter_sequence_post(self):
        """process POST to create new sequence"""

        _script_id = self._get_script_id()
        random_num = random.randint(0, 999)

        data = {
            "name": API_AUTO_TEST_ + str(random_num),                           # name of new sequence
            "description": API_AUTO_TEST_ + str(random_num) + " description",   # ..and its description
            "type": True,
            "scripts": [
                {
                    # "name": "TestAPIscripter1",                               # ?? имя подцепаемого скрипта _script_id
                    "id": str(_script_id),
                    "keys": [{"CPU": 40}, {"RAM": 40}],
                    "usage": True,
                    "stage_num": 0
                }
            ],
            "node": 0,
            # "author_id": at_uid
            "author_id": self.get_self_user_id()
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.scripter/sequence", headers=header, json=data, verify=False)
        return resp

    def scripter_sequence_put(self):  # почему-то создает новую секвенцию, а не обновляет старую
        _script_id = self._get_script_id()
        _seq_id = self._get_sequence_id()
        data = {
            "name": " TestSeqApi",              # FIXME:
            "description": " TestSeqApi1",
            "type": True,
            "scripts": [
                {
                    "name": "TestAPIscripter1",
                    "id": str(_script_id),
                    "keys": [
                        {
                            "CPU": 40
                        },
                        {
                            "RAM": 40
                        }
                    ],
                    "usage": True,
                    "stage_num": 0
                }
            ],
            "node": 0,
            "id": str(_seq_id),
            "author_id": self.get_self_user_id()
        }
        header = {'token': self.token}
        resp = self.sess.put(f"{self.host}/back/dp.scripter/sequence", headers=header, json=data, verify=False)
        return resp

    def scripter_sequence_log_id_get(self):
        # исп: получить логи >> front: проваливаешься в скрипт;
        _seq_id = self._get_sequence_id()
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/sequence/log/" + str(_seq_id), headers=header, verify=False)
        return resp

    def scripter_sequence_id_get(self):
        _seq_id = self._get_sequence_id()
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/sequence/" + str(_seq_id), headers=header, verify=False)
        return resp

    def scripter_sequence_start_post(self):
        _seq_id = self._get_sequence_id()
        data = {
            "id": str(_seq_id),
            "node": 0,
            "keys": [
                {
                    "1": "2"
                }
            ]
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.scripter/sequence/start", headers=header, json=data, verify=False)
        return resp

    # FIXME: {"error":{"code":400,"msg":"Задание не было запущено"}}
    def scripter_sequence_stop_id_get(self):
        _seq_id = self._get_sequence_id()
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/sequence/stop/" + str(_seq_id), headers=header, verify=False)
        return resp

    def scripter_sequence_sequence_id_log_last_get(self):
        _seq_id = self._get_sequence_id()
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/sequence/" + str(_seq_id) + "/log/last", headers=header, verify=False)
        return resp

    # FIXME: хардкод в EP # >> sequence_id_log_log_id ??
    def scripter_sequence_id_log_id_get(self):
        _seq_id = self._get_sequence_id()
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/sequence/" + str(_seq_id) + "/log/last/TestAPIscripter1", headers=header, verify=False)
        return resp

    def scripter_sequence_sequence_type_admin_get(self):
        # исп: получить список Последовательностей "Административные"
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/sequence/admin", headers=header, verify=False)
        return resp

    def scripter_sequence_sequence_type_user_get(self):
        # исп: получить список Последовательностей "Пользовательские"
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/sequence/user", headers=header, verify=False)
        return resp
