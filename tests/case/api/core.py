import os

from req.Helpers.user_session import UserSession
from req.Api.req_core import Core


act_dir_pass = "d8hELYed9L809RB9FkSO!"
ssh_pass = "R3U7zYiyxVFtUq8QvRAJ"  # 22
# ssh_pass = "nCNmqNT<)>Bsr3c]"  # 16
mail_pass = "8327kHLHsfohn;hksjkfou!"


class CoreCase(UserSession):

    def case_core_active_directory_get(self):
        req = Core(self.sess, self.host)

        resp = req.core_active_directory_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_active_directory_post(self):
        req = Core(self.sess, self.host)

        req.sess.headers.update({'skey': "ANGARA"})
        body = {
            "base_dn": "OU=Employees,DC=ngrsoftlab,DC=ru",
            "host": "192.168.189.2",
            "open_ldap": False,
            "password": act_dir_pass,
            "port": 636,
            "tls": True,
            "user": "dataplan@ngrsoftlab.ru"
        }

        resp = req.core_active_directory_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_active_directory_structure_post(self):
        # front: /settings/domain   # [контроллер домена]
        req = Core(self.sess, self.host)

        req.sess.headers.update({'skey': "ANGARA"})
        body = {
            "base_dn": "OU=Employees,DC=ngrsoftlab,DC=ru",
            "host": "192.168.189.2",
            "open_ldap": False,
            "password": act_dir_pass,
            "port": 636,
            "tls": True,
            "user": "dataplan@ngrsoftlab.ru"
        }

        resp = req.core_active_directory_structure_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_active_directory_test_settings_post(self):
        req = Core(self.sess, self.host)

        req.sess.headers.update({'skey': "ANGARA"})
        body = {
            "base_dn": "OU=Employees,DC=ngrsoftlab,DC=ru",
            "host": "192.168.189.2",
            "open_ldap": False,
            "password": act_dir_pass,
            "port": 636,
            "tls": True,
            "user": "dataplan@ngrsoftlab.ru"
        }
        resp = req.core_active_directory_test_settings_post(body)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_core_backups_get(self):
        req = Core(self.sess, self.host)
        resp = req.core_backups_get()
        # print(f"sc: {resp.status_code}, text: {resp.text}")
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # 200: text: {"res":[]}

    # TODO: [POST] /back/dp.core/backups
    def case_core_backups_post(self):
        req = Core(self.sess, self.host)

        data = {}

        resp = req.core_backups_post(data)
        print(resp.text)
        assert False

    def case_core_backups_last_get(self):
        req = Core(self.sess, self.host)
        resp = req.core_backups_last_get()
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # 200: {"res":{"ID":0,"startTime":"","status":"","type":"","log":""}}

    # TODO: [GET] /back/dp.core/backups/{id}
    def case_core_backups_id_get(self):
        req = Core(self.sess, self.host)

        _id = 0     # todo: what of id?

        resp = req.core_backups_id_get(_id)
        print(resp.text)
        assert False

    # TODO: [DELETE] /back/dp.core/backups
    def case_core_backups_id_delete(self):
        req = Core(self.sess, self.host)

        _id = 0     # todo: what of id?

        resp = req.core_backups_id_delete(_id)
        print(resp.text)
        assert False

    # TODO: [POST] /back/dp.core/backups/{id}/restore
    def case_core_backups_id_restore_post(self):
        req = Core(self.sess, self.host)

        _id = 0     # todo: what of id?

        data = {}

        resp = req.core_backups_id_restore_post(_id, data)
        print(resp.text)
        assert False

    # TODO: [POST] /back/dp.core/backups/{type}/upload
    def case_core_backups_type_upload_post(self):
        req = Core(self.sess, self.host)

        _type = "servicedb"     # todo: servicedb|storagedb

        data = {}

        resp = req.core_backups_type_upload_post(_type, data)
        print(resp.text)
        assert False

    # TODO: [GET] /back/dp.core/backups/{type}/{id}/download
    def case_core_backups_type_id_download_get(self):
        req = Core(self.sess, self.host)

        _type = "servicedb"     # todo: servicedb|storagedb

        _id = 0                 # todo: what id

        resp = req.core_backups_type_id_download_get(_type, _id)
        print(resp.text)
        assert False

    def case_core_check_get(self):
        req = Core(self.sess, self.host)

        req.sess.headers.update({'skey': "ANGARA"})
        resp = req.core_check_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_common_get(self):
        req = Core(self.sess, self.host)

        req.sess.headers.update({'skey': "ANGARA"})
        resp = req.core_common_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_common_post(self):
        req = Core(self.sess, self.host)

        req.sess.headers.update({'skey': "ANGARA"})
        body = {
            "XMLName": {"Space": "", "Local": "common"},
            "sessions": "7|day",
            "ml": "",
            "query": "",
            "diagram": "",
            "report": "",
            "admin_ssh_user": "dataplan",
            "admin_ssh_password": ssh_pass,
            "msg_language": ""
        }
        resp = req.core_common_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_common_test_post(self):
        req = Core(self.sess, self.host)

        req.sess.headers.update({'skey': "ANGARA"})
        body = {
            "XMLName": {"Space": "", "Local": "common"},
            "sessions": "7|day",
            "ml": "",
            "query": "",
            "diagram": "",
            "report": "",
            "admin_ssh_user": "dataplan",
            "admin_ssh_password": ssh_pass,
            "msg_language": ""
        }
        resp = req.core_common_test_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_component_ml_restart_get(self):
        req = Core(self.sess, self.host)

        what = "ml"
        action = "restart"
        node = "0"
        resp = req.core_component_what_action_node(what, action, node)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_component_picker_restart_get(self):
        req = Core(self.sess, self.host)

        what = "picker"
        action = "restart"
        node = "0"
        resp = req.core_component_what_action_node(what, action, node)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_component_servicedb_restart_get(self):
        req = Core(self.sess, self.host)

        what = "servicedb"
        action = "restart"
        node = "0"
        resp = req.core_component_what_action_node(what, action, node)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def core_component_datastore_restart_get(self):
        req = Core(self.sess, self.host)

        what = "datastore"
        action = "restart"
        node = "0"
        resp = req.core_component_what_action_node(what, action, node)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_download_settings_get(self):
        req = Core(self.sess, self.host)

        resp = req.core_download_settings_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_email_import_cert_post(self):
        req = Core(self.sess, self.host)

        file_path = os.path.dirname(__file__) + "/../../Files/mailCert.crt"

        with open(file_path, 'r') as f:
            cert_text = f.read()
        body = {"data": cert_text}
        resp = req.core_email_import_cert_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_email_send_test_post(self):
        req = Core(self.sess, self.host)

        body = {
            "description": "TestAPICore",
            "disable_tls": False,
            "host": "NGR-Exchange01.ngrsoftlab.ru",
            "name": "TestAPI",
            "port": 587,
            "protocol": "smtp",
            "psw": mail_pass,
            "send_user": "svc_ngr_mail@ngrsoftlab.ru",
            "user": "svc_ngr_mail@ngrsoftlab.ru"
        }
        resp = req.core_email_send_test_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_email_in_get(self):
        req = Core(self.sess, self.host)

        _type = "in"
        resp = req.core_email_type_get(_type)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_email_out_get(self):
        req = Core(self.sess, self.host)

        _type = "out"
        resp = req.core_email_type_get(_type)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_email_in_post(self):
        req = Core(self.sess, self.host)

        _type = "in"
        body = {
            "description": "TestAPICore",
            "disable_tls": False,
            "host": "NGR-Exchange01.ngrsoftlab.ru",
            "name": "TestAPI",
            "port": 587,
            "protocol": "smtp",
            "psw": mail_pass,
            "send_user": "svc_ngr_mail@ngrsoftlab.ru",
            "user": "svc_ngr_mail@ngrsoftlab.ru"
        }
        resp = req.core_email_type_post(_type, body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_email_out_post(self):
        req = Core(self.sess, self.host)

        _type = "out"
        body = {
            "description": "TestAPICore",
            "disable_tls": False,
            "host": "NGR-Exchange01.ngrsoftlab.ru",
            "name": "TestAPI",
            "port": 587,
            "protocol": "smtp",
            "psw": mail_pass,
            "send_user": "svc_ngr_mail@ngrsoftlab.ru",
            "user": "svc_ngr_mail@ngrsoftlab.ru"
        }
        resp = req.core_email_type_post(_type, body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_flag_get(self):
        req = Core(self.sess, self.host)

        req.sess.headers.update({'skey': "ANGARA"})
        resp = req.core_flag_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_ip_get(self):
        req = Core(self.sess, self.host)

        req.sess.headers.update({'skey': "ANGARA"})
        resp = req.core_ip_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    # TODO: [POST] /back/dp.core/nodes/delete/{what}
    def case_core_nodes_delete_what_post(self):
        req = Core(self.sess, self.host)

        what = "ml"     # todo: ml/picker/servicedb/datastore

        data = {}

        resp = req.core_nodes_delete_what_post(what, data)
        print(resp.text)
        assert False

    def case_core_nodes_list_ml_get(self):
        req = Core(self.sess, self.host)

        req.sess.headers.update({'skey': "ANGARA"})
        what = "ml"
        resp = req.core_nodes_list_what_get(what)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_nodes_list_picker_get(self):
        req = Core(self.sess, self.host)

        req.sess.headers.update({'skey': "ANGARA"})
        what = "picker"
        resp = req.core_nodes_list_what_get(what)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_nodes_list_servicedb_get(self):
        req = Core(self.sess, self.host)

        req.sess.headers.update({'skey': "ANGARA"})
        what = "servicedb"
        resp = req.core_nodes_list_what_get(what)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_nodes_list_datastore_get(self):
        req = Core(self.sess, self.host)

        req.sess.headers.update({'skey': "ANGARA"})
        what = "datastore"
        resp = req.core_nodes_list_what_get(what)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    # TODO: empty
    def case_core_nodes_test_what_post(self):
        req = Core(self.sess, self.host)

        what = "ml"     # TODO: ml/picker/servicedb/datastore
        data = {}

        resp = req.core_nodes_test_what_post(data)
        print(resp.text)
        assert False

    # TODO:
    # def core_nodes_test_datastore_post(self):  # здесь нужны данные
    #     body = {"active": 0,
    #             "has_nodes": "0",
    #             "what": "datastore",
    #             "ssh_user": "dataplan",
    #             "ssh_password": "R3U7zYiyxVFtUq8QvRAJ",
    #             "store_user": "default",
    #             "" "store_password": "1q2w3e4r5t",
    #             "db": "",
    #             "nodes": [
    #                 {"XMLName": {"Space": "", "Local": "node"}, "param": "800000000000000000", "threads": "1",
    #                  "ip_node": "127.0.0.1", "ssh_port": "22", "store_port": "8123", "keyIdForFront": "127.0.0.1"}]}
    #     header = {'token': self.token, 'skey': "ANGARA"}
    #     resp = self.sess.post(f"{self.host}/back/dp.core/nodes/test/datastore", headers=header, json=body, verify=False)
    #     return resp

    def case_core_nodes_ml_get(self):
        req = Core(self.sess, self.host)
        what = "ml"
        resp = req.core_nodes_what_get(what)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_nodes_picker_get(self):
        req = Core(self.sess, self.host)
        what = "picker"
        resp = req.core_nodes_what_get(what)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_nodes_servicedb_get(self):
        req = Core(self.sess, self.host)
        what = "servicedb"
        resp = req.core_nodes_what_get(what)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_nodes_datastore_get(self):
        req = Core(self.sess, self.host)
        what = "datastore"
        resp = req.core_nodes_what_get(what)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    # TODO: [POST] /back/dp.core/nodes/{what}
    def case_core_nodes_what_post(self):
        req = Core(self.sess, self.host)

        what = "ml"     # todo: ml/picker/servicedb/datastore

        data = {}

        resp = req.core_nodes_what_post(what, data)
        print(resp.text)
        assert False

    # TODO:
    # def case_core_nodes_datastore_post(self):  # здесь нужны данные
    #     req = CoreNew(self.sess, self.host)
    #
    #     req.sess.headers.update({'skey': "ANGARA"})
    #     what = "datastore"
    #     body = {
    #         "active": 0,
    #         "has_nodes": "0",
    #         "what": "datastore",
    #         "ssh_user": "dataplan",
    #         "ssh_password": ssh_pass,
    #         "store_user": "default",
    #         "" "store_password": "1q2w3e4r5t",
    #         "db": "",
    #         "nodes": [
    #             {
    #                 "XMLName": {"Space": "", "Local": "node"}, "param": "8000000", "threads": "1",
    #                 "ip_node": "127.0.0.1", "ssh_port": "22", "store_port": "8123", "keyIdForFront": "127.0.0.1"
    #             }
    #         ]
    #     }
    #     resp = req.core_nodes_what_post(what, body)

    # TODO: [GET] /back/dp.core/save
    def case_core_save_get(self):
        req = Core(self.sess, self.host)
        resp = req.core_save_get()
        print(resp.text)
        assert False

    # TODO: [GET] /back/dp.core/secrets
    def case_core_secrets_get(self):
        req = Core(self.sess, self.host)
        resp = req.core_secrets_get()
        print(resp.text)
        assert False

    # TODO: [POST] /back/dp.core/secrets
    def case_core_secrets_post(self):
        req = Core(self.sess, self.host)

        data = {}

        resp = req.core_secrets_post(data)
        print(resp.text)
        assert False

    # TODO: [GET] /back/dp.core/secrets/{id}
    def case_core_secrets_id_get(self):
        req = Core(self.sess, self.host)

        _id = 0

        resp = req.core_secrets_id_get(_id)
        print(resp.text)
        assert False

    # TODO: [PUT] /back/dp.core/secrets/{id}
    def case_core_secrets_id_put(self):
        req = Core(self.sess, self.host)

        _id = 0

        data = {}

        resp = req.core_secrets_id_put(_id, data)
        print(resp.text)
        assert False

    # TODO: [DELETE] /back/dp.core/secrets/{id}
    def case_core_secrets_id_delete(self):
        req = Core(self.sess, self.host)

        _id = 0

        resp = req.core_secrets_id_delete(_id)
        print(resp.text)
        assert False

    def case_core_service_dp_alarmer_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_alarmer"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_auth_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_auth"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_core_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_core"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_licenser_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_licenser"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_log_eater_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_log_eater"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_monitor_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_monitor"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_peopler_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_peopler"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_permitter_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_permitter"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_postgres_single_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_postgres_single"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_taskplan_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_taskplan"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_updater_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_updater"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_absorber_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_absorber"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_picker_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_picker"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_storage_single_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_storage_single"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_storage_worker_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_storage_worker"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_ml_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_ml"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_scripter_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_scripter"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_datapie_baker_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_datapie_baker"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_elements_eater_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_elements_eater"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_frontend_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_frontend"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_reporter_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_reporter"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_rm_cook_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_rm_cook"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_rm_ml_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_rm_ml"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_screener_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_screener"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_visualisation_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_visualisation"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_xba_cook_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_xba_cook"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_dp_xba_py_restart_get(self):
        req = Core(self.sess, self.host)
        what = "dp_xba_py"
        action = "restart"
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_service_all_restart_get(self):  # стенд не тянет этот метод
        req = Core(self.sess, self.host)
        action = "restart"      # todo: restart|stop
        resp = req.core_services_all_action_get(action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_sid_get(self):
        req = Core(self.sess, self.host)
        req.sess.headers.update({'skey': "ANGARA"})

        resp = req.core_sid_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_core_syslog_get(self):
        req = Core(self.sess, self.host)
        req.sess.headers.update({'skey': "ANGARA"})

        resp = req.core_syslog_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    # fixme: не перебить настройки
    def case_core_syslog_post(self):
        req = Core(self.sess, self.host)

        body = {
            "destinations": [
                {
                    "XMLName": {
                        "Space": "",
                        "Local": "destination"
                    },
                    "email": "",
                    "syslog_host": "10.130.0.22",
                    "syslog_port": 6514,
                    "syslog_protocol": "tcp"
                },
                {
                    "XMLName": {
                        "Space": "",
                        "Local": "destination"
                    },
                    "email": "",
                    "syslog_host": "127.0.0.1",
                    "syslog_port": 8000,
                    "syslog_protocol": "udp"
                }
            ]
        }
        resp = req.core_syslog_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp
