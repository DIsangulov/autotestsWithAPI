import json
import random


from req.Helpers.base_req import BaseReq

rand = None
script_id = None
log_id = None
seq_id = None
log_seq_id = None
at_uid = None


class Scripter(BaseReq):

    def peopler_users_at_uid_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.peopler/users", headers=header, verify=False)
        name = 'dataplan_qaa@ngrsoftlab.ru'
        users = json.loads(resp.text)['res']
        uid = next((user for user in users if user['name'] == name), None)
        global at_uid
        at_uid = uid['id']
        return resp

    def scripter_category_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/category", headers=header, verify=False)
        return resp

    def scripter_libs_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/libs", headers=header, verify=False)
        return resp

    def scripter_script_post(self):
        global rand
        rand = random.randint(1200, 12500)
        data = {
            "author": "dataplan_qaa@ngrsoftlab.ru",
            "name": "API TEST " + str(rand),
            "description": "API TEST",
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
            "author_id": at_uid
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.scripter/script", headers=header, json=data, verify=False)
        return resp

    def scripter_script_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script", headers=header, verify=False)
        dct = json.loads(resp.text)
        global script_id
        script_id = dct['res'][0]['id']  # получили id скрипта
        return resp

    def scripter_script_put(self):
        data = {
            "type": True,
            "editor_id": at_uid,
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
        header = {'token': self.token}
        resp = self.sess.put(f"{self.host}/back/dp.scripter/script", headers=header, json=data, verify=False)
        return resp

    def scripter_script_exec_list_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/exec_list", headers=header, verify=False)
        return resp

    def scripter_script_id_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/" + str(script_id), headers=header, verify=False)
        # print(resp.text)
        return resp

    def scripter_script_start_post(self):
        data = {
            "id": str(script_id),
            "node": 0,
            "keys": [
                {
                    "1": "2"
                }
            ]
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.scripter/script/start", headers=header, json=data, verify=False)
        return resp

    def scripter_script_stop_id_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/stop/" + str(script_id), headers=header,
                             verify=False)
        return resp

    def scripter_script_id_files_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/" + str(script_id) + "/files", headers=header,
                             verify=False)
        return resp

    def scripter_script_id_files_put(self):
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
        resp = self.sess.put(f"{self.host}/back/dp.scripter/script/" + str(script_id) + "/files", headers=header,
                             json=data, verify=False)
        return resp

    def scripter_script_id_log_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/" + str(script_id) + "/log", headers=header,
                             verify=False)
        dct = json.loads(resp.text)
        global log_id
        log_id = dct['res'][0]['id']  # получили id лога
        return resp

    def scripter_script_id_log_delete(self):
        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.scripter/script/" + str(script_id) + "/log", headers=header,
                                verify=False)
        return resp

    def scripter_script_id_log_last_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/" + str(script_id) + "/log/last", headers=header,
                             verify=False)
        return resp

    def scripter_script_id_log_log_id_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/" + str(script_id) + "/log/" + str(log_id),
                             headers=header,
                             verify=False)
        return resp

    def scripter_script_id_log_log_id_delete(self):
        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.scripter/script/" + str(script_id) + "/log/" + str(log_id),
                                headers=header,
                                verify=False)
        return resp

    def scripter_script_id_delete(self):
        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.scripter/script/" + str(script_id), headers=header, verify=False)
        return resp

    def scripter_script_type_admin_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/admin", headers=header, verify=False)
        return resp

    def scripter_script_type_user_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/script/user", headers=header, verify=False)
        return resp

    def scripter_sequence_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/sequence", headers=header, verify=False)
        dct = json.loads(resp.text)
        global seq_id
        seq_id = dct['res'][0]['id']  # получили id последовательности
        return resp

    def scripter_sequence_post(self):
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
            "author_id": at_uid
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.scripter/sequence", headers=header, json=data, verify=False)
        return resp

    def scripter_sequence_put(self):  # почему-то создает новую секвенцию, а не обновляет старую
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
            "author_id": at_uid
        }
        header = {'token': self.token}
        resp = self.sess.put(f"{self.host}/back/dp.scripter/sequence", headers=header, json=data, verify=False)
        return resp

    def scripter_sequence_log_id_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/sequence/log/" + str(seq_id), headers=header, verify=False)
        return resp

    def scripter_sequence_id_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/sequence/" + str(seq_id), headers=header, verify=False)
        return resp

    def scripter_sequence_start_post(self):
        data = {
            "id": str(seq_id),
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

    def scripter_sequence_stop_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/sequence/stop/" + str(seq_id), headers=header, verify=False)
        return resp

    def scripter_sequence_id_log_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/sequence/" + str(seq_id) + "/log/last", headers=header,
                             verify=False)
        # dct = json.loads(resp.text)
        # global log_seq_id
        # log_seq_id = dct['res'][0]['id']  # получили id лога последовательности
        # print(log_seq_id)
        return resp

    def scripter_sequence_id_log_id_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/sequence/" + str(seq_id) + "/log/last/TestAPIscripter1",
                             headers=header, verify=False)
        return resp

    def scripter_sequence_sequence_type_admin_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/sequence/admin", headers=header, verify=False)
        return resp

    def scripter_sequence_sequence_type_user_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.scripter/sequence/user", headers=header, verify=False)
        return resp
