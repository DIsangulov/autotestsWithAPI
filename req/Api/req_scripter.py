import json
import random

import pytest

from req.Helpers.base_req import BaseReq

rand = None
script_id = None
log_id = None
seq_id = None
log_seq_id = None


class Scripter(BaseReq):

    def scripter_category_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/category", headers=header, verify=False)
        return resp

    def scripter_libs_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/libs", headers=header, verify=False)
        return resp

    def scripter_script_post(self, token):
        global rand
        rand = random.randint(1200, 12500)
        data = {
            "name": "TestAPIscripter" + str(rand),
            "description": "TestAPIscripter",
            "type": True,
            "category": 1,
            "keys": [
                {
                    "1": "2"
                }
            ],
            "node": 0,
            "encrypt": False,
            "encapsulate": False,
            "main_file": {
                "file_data": "print('Test Scripter')",
                "file_name": "testScripter.py"
            },
            "additional_files": [],
            "author_id": 44
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.scripter/script", headers=header, json=data, verify=False)
        return resp

    def scripter_script_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script", headers=header, verify=False)
        dct = json.loads(resp.text)
        global script_id
        script_id = dct['res'][0]['id']  # получили id скрипта
        return resp

    def scripter_script_put(self, token):
        data = {
            "type": True,
            "editor_id": 44,
            "id": str(script_id),
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
        header = {'token': token}
        resp = self.sess.put(f"{self.host}/back/dp.scripter/script", headers=header, json=data, verify=False)
        return resp

    def scripter_script_exec_list_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/exec_list", headers=header, verify=False)
        return resp

    def scripter_script_id_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/" + str(script_id), headers=header, verify=False)
        print(resp.text)
        return resp

    def scripter_script_start_post(self, token):
        data = {
            "id": str(script_id),
            "node": 0,
            "keys": [
                {
                    "1": "2"
                }
            ]
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.scripter/script/start", headers=header, json=data, verify=False)
        return resp

    def scripter_script_stop_id_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/stop/" + str(script_id), headers=header,
                             verify=False)
        return resp

    def scripter_script_id_files_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/" + str(script_id) + "/files", headers=header,
                             verify=False)
        return resp

    def scripter_script_id_files_put(self, token):
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
        header = {'token': token}
        resp = self.sess.put(f"{self.host}/back/dp.scripter/script/" + str(script_id) + "/files", headers=header,
                             json=data, verify=False)
        return resp

    def scripter_script_id_log_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/" + str(script_id) + "/log", headers=header,
                             verify=False)
        dct = json.loads(resp.text)
        global log_id
        log_id = dct['res'][0]['id']  # получили id лога
        return resp

    def scripter_script_id_log_delete(self, token):
        header = {'token': token}
        resp = self.sess.delete(f"{self.host}/back/dp.scripter/script/" + str(script_id) + "/log", headers=header,
                                verify=False)
        return resp

    def scripter_script_id_log_last_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/" + str(script_id) + "/log/last", headers=header,
                             verify=False)
        return resp

    def scripter_script_id_log_log_id_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/" + str(script_id) + "/log/" + str(log_id),
                             headers=header,
                             verify=False)
        return resp

    def scripter_script_id_log_log_id_delete(self, token):
        header = {'token': token}
        resp = self.sess.delete(f"{self.host}/back/dp.scripter/script/" + str(script_id) + "/log/" + str(log_id),
                                headers=header,
                                verify=False)
        return resp

    def scripter_script_id_delete(self, token):
        header = {'token': token}
        resp = self.sess.delete(f"{self.host}/back/dp.scripter/script/" + str(script_id), headers=header, verify=False)
        return resp

    def scripter_script_type_admin_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/admin", headers=header, verify=False)
        return resp

    def scripter_script_type_user_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/user", headers=header, verify=False)
        return resp

    def scripter_sequence_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/sequence", headers=header, verify=False)
        dct = json.loads(resp.text)
        global seq_id
        seq_id = dct['res'][0]['id']  # получили id последовательности
        return resp

    def scripter_sequence_post(self, token):
        data = {
            "name": " TestSeqApi",
            "description": " TestSeqApi",
            "type": True,
            "scripts": [
                {
                    "name": "TestAPIscripter1",
                    "id": str(script_id),
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
            "author_id": 44
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.scripter/sequence", headers=header, json=data, verify=False)
        return resp

    def scripter_sequence_put(self, token):  # почему-то создает новую секвенцию, а не обновляет старую
        data = {
            "name": " TestSeqApi",
            "description": " TestSeqApi1",
            "type": True,
            "scripts": [
                {
                    "name": "TestAPIscripter1",
                    "id": str(script_id),
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
            "id": str(seq_id),
            "author_id": 44
        }
        header = {'token': token}
        resp = self.sess.put(f"{self.host}/back/dp.scripter/sequence", headers=header, json=data, verify=False)
        return resp

    def scripter_sequence_log_id_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/sequence/log/" + str(seq_id), headers=header, verify=False)
        return resp

    def scripter_sequence_id_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/sequence/" + str(seq_id), headers=header, verify=False)
        return resp

    def scripter_sequence_start_post(self, token):
        data = {
            "id": str(seq_id),
            "node": 0,
            "keys": [
                {
                    "1": "2"
                }
            ]
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.scripter/sequence/start", headers=header, json=data, verify=False)
        return resp

    def scripter_sequence_stop_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/sequence/stop/" + str(seq_id), headers=header, verify=False)
        return resp

    def scripter_sequence_id_log_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/sequence/" + str(seq_id) + "/log/last", headers=header,
                             verify=False)
        # dct = json.loads(resp.text)
        # global log_seq_id
        # log_seq_id = dct['res'][0]['id']  # получили id лога последовательности
        # print(log_seq_id)
        return resp

    def scripter_sequence_id_log_id_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/sequence/" + str(seq_id) + "/log/last/TestAPIscripter1",
                             headers=header, verify=False)
        return resp

    def scripter_sequence_sequence_type_admin_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/sequence/admin", headers=header, verify=False)
        return resp

    def scripter_sequence_sequence_type_user_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/sequence/user", headers=header, verify=False)
        return resp
