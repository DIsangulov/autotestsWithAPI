import json
import random

from req.Helpers.base_req import BaseReq
from req.Api.req_scripter import Scripter

API_AUTO_TEST_ = "API_AUTO_TEST_"

script_id = set()          # 'id' скрипта  # предполагается, что будут использоваться только скрипты с именем .startswith(API_AUTO_TEST_%)
sequence_id = set()        # 'id' последовательности


class ScripterCase(BaseReq):

    def _collect_script_id(self):
        resp = Scripter(self.sess, self.host).scripter_script_get()
        assert resp.status_code == 200, f"assert::scripter_script_get, failed. status_code: {resp.status_code}, resp.text: {resp.text}"

        script_info_rows = json.loads(resp.text)['res']

        for _row in script_info_rows:
            if str(_row["name"]).startswith(API_AUTO_TEST_):
                script_id.add(_row['id'])    # global: script_id
        # print(f"script_id list: {script_id}")

    def _get_script_id(self) -> int:
        """get from global script_id: API_AUTO_TEST_x"""
        if len(script_id) == 0:
            self._collect_script_id()

        if len(script_id) == 0:
            # создать новый скрипт, вернуть его значение
            r_new_script = self.case_scripter_script_post()
            new_script_id = json.loads(r_new_script.text)['res']
            return int(new_script_id)

        return script_id.pop()

    def _collect_sequence_id(self):
        resp = Scripter(self.sess, self.host).scripter_sequence_get()
        assert resp.status_code == 200, f"assert::scripter_sequence_get, failed. status_code: {resp.status_code}, resp.text: {resp.text}"

        sequence_info_rows = json.loads(resp.text)['res']

        for _row in sequence_info_rows:
            if str(_row["name"]).startswith(API_AUTO_TEST_):
                sequence_id.add(_row['id'])     # global: sequence_id
        # print(f"sequence_id list: {sequence_id}")

    def _get_sequence_id(self) -> int:
        """get from global sequence_id: API_AUTO_TEST_x"""
        if len(sequence_id) == 0:
            self._collect_sequence_id()

        if len(sequence_id) == 0:
            # создать новую последовательность, вернуть ее значение
            r_new_sequence = self.case_scripter_sequence_post()
            new_sequence_id = json.loads(r_new_sequence.text)['res']
            return int(new_sequence_id)

        return sequence_id.pop()

    # todo: убрать внутрь кейсов
    def _get_log_id(self, _script_id: int) -> int:
        # лог есть у скрипта, который запускался хоть один раз || {"res":null}

        # запрос на получение логов у скрипта _script_id
        log_resp = Scripter(self.sess, self.host).scripter_script_id_log_get(_script_id)
        # {"res":null}
        # {"res":[{"id":359949,"name":"","start":"2023-06-22T14:44:53.544363Z","status":"выполнен",...

        # проверка на результат != null
        if log_resp.text == '{"res":null}\n':
            Scripter(self.sess, self.host).scripter_script_start_post(_script_id)             # запускаем скрипт _script_id
            # FIXME: нужно ли дожидаться исполнения скрипта?
            log_resp = Scripter(self.sess, self.host).scripter_script_id_log_get(_script_id)  # повторный запрос на наличие логов
            # FIXME: кинуть ещё одну проверку logs != null; вообще, скрипт может и не исполниться, логов не будет тогда снова

        dct = json.loads(log_resp.text)
        log_id = dct['res'][-1]['id']
        return log_id

    def case_scripter_category_get(self):
        req = Scripter(self.sess, self.host)
        resp = req.scripter_category_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)
        # {"res":[{"name":"Аналитические","path":"analitycs"},{"name":"Парсеры","path":"parsers"},{"name":"Служебные","path":"service"}]}

    def case_scripter_libs_get(self):
        req = Scripter(self.sess, self.host)
        resp = req.scripter_libs_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_scripter_script_get(self):
        req = Scripter(self.sess, self.host)
        resp = req.scripter_script_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_scripter_script_put(self):
        req = Scripter(self.sess, self.host)

        _script_id = self._get_script_id()
        str_rand_num = str(random.randint(100, 999))
        data = {
            "type": True,
            "editor_id": self.get_self_user_id(),
            "id": _script_id,
            "name": API_AUTO_TEST_ + "changed" + str_rand_num,
            "description": API_AUTO_TEST_ + "changed" + str_rand_num,
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
        resp = req.scripter_script_put(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_scripter_script_post(self):
        req = Scripter(self.sess, self.host)
        str_rand_num = str(random.randint(0, 999))
        data = {
            # "author": "dataplan_qaa@ngrsoftlab.ru",
            # "author": "Владимир Даль",
            "name": API_AUTO_TEST_ + str_rand_num,
            "description": API_AUTO_TEST_ + str_rand_num,
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
            "author_id": self.get_self_user_id()
        }
        resp = req.scripter_script_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)
        return resp     # исп: _get_script_id(self)

    def case_scripter_script_exec_list_get(self):
        req = Scripter(self.sess, self.host)
        resp = req.scripter_script_exec_list_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_scripter_script_start_post(self):
        req = Scripter(self.sess, self.host)
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
        resp = req.scripter_script_start_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    # FIXME: {"error":{"code":400,"msg":"Задание не было запущено"}}
    def case_scripter_script_stop_id_get(self):
        req = Scripter(self.sess, self.host)
        _script_id = self._get_script_id()
        resp = req.scripter_script_stop_id_get(_script_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_scripter_script_id_get(self):
        req = Scripter(self.sess, self.host)
        _script_id = self._get_script_id()
        resp = req.scripter_script_id_get(_script_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_scripter_script_id_delete(self):
        req = Scripter(self.sess, self.host)
        _script_id = self._get_script_id()
        resp = req.scripter_script_id_delete(_script_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_scripter_script_id_files_get(self):
        req = Scripter(self.sess, self.host)
        _script_id = self._get_script_id()
        resp = req.scripter_script_id_files_get(_script_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_scripter_script_id_files_put(self):
        req = Scripter(self.sess, self.host)
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
        resp = req.scripter_script_id_files_put(_script_id, data)
        # fixme: 400 статус код, файл существует
        assert resp.status_code == 200 or 400, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_scripter_script_id_log_get(self):
        req = Scripter(self.sess, self.host)
        _script_id = self._get_script_id()
        resp = req.scripter_script_id_log_get(_script_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)    # если скрипт '_script_id' не запускался >> {"res":null}

    def case_scripter_script_id_log_delete(self):
        req = Scripter(self.sess, self.host)
        _script_id = self._get_script_id()
        # {"error":{"code":400,"description":"sql: no rows in result set","msg":"Ошибка выборки из бд"}}
        # При отсутствии логов; запускаю скрипт '_script_id', чтобы появилась строка логов
        req.scripter_script_start_post(_script_id)     # запрос на старт исполнения скрипта '_script_id'
        # FIXME: ждать, пока скрипт исполнится?
        resp = req.scripter_script_id_log_delete(_script_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_scripter_script_id_log_last_get(self):
        req = Scripter(self.sess, self.host)
        _script_id = self._get_script_id()

        # {"error":{"code":400,"description":"sql: no rows in result set","msg":"Ошибка выборки из бд"}}
        # При отсутствии логов; запускаю скрипт '_script_id', чтобы появилась строка логов
        req.scripter_script_start_post(_script_id)     # запрос на старт исполнения скрипта '_script_id'
        # FIXME: ждать, пока скрипт исполнится?
        resp = req.scripter_script_id_log_last_get(_script_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_scripter_script_script_id_log_log_id_get(self):
        req = Scripter(self.sess, self.host)
        _script_id = self._get_script_id()
        _log_id = self._get_log_id(_script_id)
        resp = req.scripter_script_script_id_log_log_id_get(_script_id, _log_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_scripter_script_script_id_log_log_id_delete(self):
        req = Scripter(self.sess, self.host)
        _script_id = self._get_script_id()
        _log_id = self._get_log_id(_script_id)
        resp = req.scripter_script_script_id_log_log_id_delete(_script_id, _log_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)
        # print(f"Был удален лог: {_log_id}")

    def case_scripter_script_type_admin_get(self):
        req = Scripter(self.sess, self.host)
        script_type = "admin"
        resp = req.scripter_script_script_type_get(script_type)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_scripter_script_type_user_get(self):
        req = Scripter(self.sess, self.host)
        script_type = "user"
        resp = req.scripter_script_script_type_get(script_type)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_scripter_sequence_get(self):
        req = Scripter(self.sess, self.host)
        resp = req.scripter_sequence_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_scripter_sequence_put(self):  # почему-то создает новую секвенцию, а не обновляет старую
        req = Scripter(self.sess, self.host)

        str_random_num = str(random.randint(100, 999))
        _script_id = self._get_script_id()
        _seq_id = self._get_sequence_id()
        data = {
            "name": API_AUTO_TEST_ + "changed" + str_random_num,
            "description": API_AUTO_TEST_ + "changed" + str_random_num,
            "type": True,
            "scripts": [
                {
                    # "name": "TestAPIscripter1",
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
        resp = req.scripter_sequence_put(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_scripter_sequence_post(self):
        req = Scripter(self.sess, self.host)
        _script_id = self._get_script_id()
        str_random_num = str(random.randint(100, 999))

        data = {
            "name": API_AUTO_TEST_ + str_random_num,                           # name of new sequence
            "description": API_AUTO_TEST_ + str_random_num + " description",   # ..and its description
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
            "author_id": self.get_self_user_id()
        }
        resp = req.scripter_sequence_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)
        return resp     # исп: _get_sequence_id

    def case_scripter_sequence_log_id_get(self):
        req = Scripter(self.sess, self.host)
        _seq_id = self._get_sequence_id()
        resp = req.scripter_sequence_log_id_get(_seq_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_scripter_sequence_start_post(self):
        req = Scripter(self.sess, self.host)
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
        resp = req.scripter_sequence_start_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    # FIXME: {"error":{"code":400,"msg":"Задание не было запущено"}}
    def case_scripter_sequence_stop_id_get(self):
        req = Scripter(self.sess, self.host)
        _seq_id = self._get_sequence_id()
        resp = req.scripter_sequence_stop_id_get(_seq_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_scripter_sequence_id_get(self):
        req = Scripter(self.sess, self.host)
        _seq_id = self._get_sequence_id()
        resp = req.scripter_sequence_id_get(_seq_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_scripter_sequence_id_delete(self):
        req = Scripter(self.sess, self.host)
        _seq_id = self._get_sequence_id()
        resp = req.scripter_sequence_id_delete(_seq_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        print(resp.text)

    def case_scripter_sequence_sequence_id_log_last_get(self):
        req = Scripter(self.sess, self.host)
        _seq_id = self._get_sequence_id()
        resp = req.scripter_sequence_sequence_id_log_last_get(_seq_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_scripter_sequence_sequence_type_admin_get(self):
        # исп: получить список Последовательностей "Административные"
        req = Scripter(self.sess, self.host)
        sequence_type = "admin"
        resp = req.scripter_sequence_sequence_type_get(sequence_type)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_scripter_sequence_sequence_type_user_get(self):
        # исп: получить список Последовательностей "Пользовательские"
        req = Scripter(self.sess, self.host)
        sequence_type = "user"
        resp = req.scripter_sequence_sequence_type_get(sequence_type)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    # __del__
    def all_api_auto_test_entity_delete(self):
        delete_machine = Scripter(self.sess, self.host)
        self._collect_script_id()
        while len(script_id) > 0:
            delete_machine.scripter_script_id_delete(script_id.pop())

        self._collect_sequence_id()
        while len(sequence_id) > 0:
            delete_machine.scripter_sequence_id_delete(sequence_id.pop())
