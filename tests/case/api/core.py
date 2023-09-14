import os

from req.Helpers.user_session import UserSession
from req.Api.req_core import Core

# active directory creds
AD_USER = "dataplan@ngrsoftlab.ru"
AD_PASS = "d8hELYed9L809RB9FkSO!"
AD_HOST = "192.168.189.2"
AD_PORT_TLS = 636
AD_base_dn = "OU=Employees,DC=ngrsoftlab,DC=ru"

# ssh creds # .5.16
ssh_pass = "R3U7zYiyxVFtUq8QvRAJ"   # fixme: wrong

# post mailing creds
MAIL_USER = "svc_ngr_mail@ngrsoftlab.ru"
MAIL_PASS = "8327kHLHsfohn;hksjkfou!"
MAIL_HOST = "NGR-Exchange01.ngrsoftlab.ru"
MAIL_PORT = 587


class CoreCase(UserSession):

    def case_core_active_directory_get(self):
        req = Core(self.sess, self.host)
        resp = req.core_active_directory_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_core_active_directory_post(self):
        # front: /settings/domain
        # !Установка новых настроек для "Контроллер домена"
        req = Core(self.sess, self.host)

        # Тестовое соединение, для проверки корректности настроек, перед применением
        self.case_core_active_directory_test_settings_post()

        req.sess.headers.update({'skey': "ANGARA"})
        body = {
            "user": AD_USER,
            "password": AD_PASS,
            "base_dn": AD_base_dn,
            "host": AD_HOST,
            "port": AD_PORT_TLS,
            "open_ldap": False,
            "tls": True
        }
        resp = req.core_active_directory_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_core_active_directory_structure_post(self):
        # front: /settings/domain   # [контроллер домена]
        req = Core(self.sess, self.host)

        req.sess.headers.update({'skey': "ANGARA"})
        body = {
            "user": AD_USER,
            "password": AD_PASS,
            "base_dn": AD_base_dn,
            "host": AD_HOST,
            "port": AD_PORT_TLS,
            "open_ldap": False,
            "tls": True
        }
        resp = req.core_active_directory_structure_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_core_active_directory_test_settings_post(self):
        req = Core(self.sess, self.host)

        req.sess.headers.update({'skey': "ANGARA"})
        body = {
            "user": AD_USER,
            "password": AD_PASS,
            "base_dn": AD_base_dn,
            "host": AD_HOST,
            "port": AD_PORT_TLS,
            "open_ldap": False,
            "tls": True
        }
        resp = req.core_active_directory_test_settings_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_core_backups_get(self):
        req = Core(self.sess, self.host)
        resp = req.core_backups_get()
        # print(f"sc: {resp.status_code}, text: {resp.text}")
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # 200: text: {"res":[]}

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

    def case_core_backups_id_get(self):
        req = Core(self.sess, self.host)

        _id = 0     # what of id?

        resp = req.core_backups_id_get(_id)
        print(resp.text)
        assert False

    def case_core_backups_id_delete(self):
        req = Core(self.sess, self.host)

        _id = 0     # what of id?

        resp = req.core_backups_id_delete(_id)
        print(resp.text)
        assert False

    def case_core_backups_id_restore_post(self):
        req = Core(self.sess, self.host)

        _id = 0     # what of id?

        data = {}

        resp = req.core_backups_id_restore_post(_id, data)
        print(resp.text)
        assert False

    def case_core_backups_type_upload_post(self):
        req = Core(self.sess, self.host)

        _type = "servicedb"     # servicedb|storagedb

        data = {}

        resp = req.core_backups_type_upload_post(_type, data)
        print(resp.text)
        assert False

    def case_core_backups_type_id_download_get(self):
        req = Core(self.sess, self.host)

        _type = "servicedb"     # servicedb|storagedb

        _id = 0                 # ?what id

        resp = req.core_backups_type_id_download_get(_type, _id)
        print(resp.text)
        assert False

    def case_core_check_get(self):
        req = Core(self.sess, self.host)

        req.sess.headers.update({'skey': "ANGARA"})
        resp = req.core_check_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_core_common_get(self):
        req = Core(self.sess, self.host)

        req.sess.headers.update({'skey': "ANGARA"})
        resp = req.core_common_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_core_common_post(self):
        # front: /settings/common
        # Изменение настроек "Административный узел"

        req = Core(self.sess, self.host)
        req.sess.headers.update({'skey': "ANGARA"})

        body = {
            "XMLName": {"Space": "", "Local": "common"},
            "sessions": "7|day",        # todo: формат отправки
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

    def case_core_component_ml_restart_get(self):
        req = Core(self.sess, self.host)

        what = "ml"
        action = "restart"
        node = "0"
        resp = req.core_component_what_action_node(what, action, node)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_core_component_picker_restart_get(self):
        req = Core(self.sess, self.host)

        what = "picker"
        action = "restart"
        node = "0"
        resp = req.core_component_what_action_node(what, action, node)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_core_component_servicedb_restart_get(self):
        req = Core(self.sess, self.host)

        what = "servicedb"
        action = "restart"
        node = "0"
        resp = req.core_component_what_action_node(what, action, node)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def core_component_datastore_restart_get(self):
        req = Core(self.sess, self.host)

        what = "datastore"
        action = "restart"
        node = "0"
        resp = req.core_component_what_action_node(what, action, node)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_core_download_settings_get(self):
        req = Core(self.sess, self.host)

        resp = req.core_download_settings_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_core_email_import_cert_post(self):
        req = Core(self.sess, self.host)

        file_path = os.path.dirname(__file__) + "/../../Files/mailCert.crt"

        with open(file_path, 'r') as f:
            cert_text = f.read()
        body = {"data": cert_text}
        resp = req.core_email_import_cert_post(body)
        # print(resp.text)    {"res":"ok"}
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_core_email_send_test_post(self):
        req = Core(self.sess, self.host)

        body = {
            "user": MAIL_USER,
            "send_user": MAIL_USER,
            "psw": MAIL_PASS,
            "host": MAIL_HOST,
            "port": MAIL_PORT,
            "protocol": "smtp",
            "name": "Test_API",
            "description": "Test_API_description",
            "disable_tls": False,
        }
        resp = req.core_email_send_test_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_core_email_type_get(self, email_type):
        req = Core(self.sess, self.host)
        resp = req.core_email_type_get(email_type)
        assert resp.status_code == 200, \
            f"""Ошибка, email_type: '{email_type}'
            status_code: {resp.status_code},
            resp: {resp.text}
            """

    def case_core_email_type_post(self, email_type):
        # front: /settings/ms
        # !Изменение настроек "Почта"
        req = Core(self.sess, self.host)

        body = {
            "user": MAIL_USER,
            "send_user": MAIL_USER,
            "psw": MAIL_PASS,
            "host": MAIL_HOST,
            "port": MAIL_PORT,
            "protocol": "smtp",
            "name": "Test_NGR",
            "description": "Test_NGR_description",
            "disable_tls": False
        }
        resp = req.core_email_type_post(email_type, body)
        assert resp.status_code == 200, \
            f"""Ошибка, email_type: '{email_type}'
            status_code: {resp.status_code},
            resp: {resp.text}
            """

    def case_core_flag_get(self):
        req = Core(self.sess, self.host)
        req.sess.headers.update({'skey': "ANGARA"})
        resp = req.core_flag_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_core_ip_get(self):
        req = Core(self.sess, self.host)
        req.sess.headers.update({'skey': "ANGARA"})
        resp = req.core_ip_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # TODO: [POST] /back/dp.core/nodes/delete/{what}
    def case_core_nodes_delete_what_post(self):
        req = Core(self.sess, self.host)

        what = "ml"     # todo: ml/picker/servicedb/datastore

        data = {}

        resp = req.core_nodes_delete_what_post(what, data)
        print(resp.text)
        assert False

    def case_core_nodes_list_what_get(self, what):
        req = Core(self.sess, self.host)
        req.sess.headers.update({'skey': "ANGARA"})
        resp = req.core_nodes_list_what_get(what)
        assert resp.status_code == 200, f"Ошибка, what: {what} код: {resp.status_code}, {resp.text}"

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

    def case_core_nodes_what_get(self, what):
        req = Core(self.sess, self.host)
        resp = req.core_nodes_what_get(what)
        assert resp.status_code == 200, f"Ошибка, what: '{what}', код: {resp.status_code}, {resp.text}"

    def case_core_nodes_what_post(self, what):
        req = Core(self.sess, self.host)

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

    def case_core_save_get(self):
        req = Core(self.sess, self.host)
        resp = req.core_save_get()
        print(resp.text)
        assert False

    def case_core_secrets_get(self):
        req = Core(self.sess, self.host)
        resp = req.core_secrets_get()
        print(resp.text)
        assert False

    def case_core_secrets_post(self):
        req = Core(self.sess, self.host)

        data = {}

        resp = req.core_secrets_post(data)
        print(resp.text)
        assert False

    def case_core_secrets_id_get(self):
        req = Core(self.sess, self.host)

        _id = 0

        resp = req.core_secrets_id_get(_id)
        print(resp.text)
        assert False

    def case_core_secrets_id_put(self):
        req = Core(self.sess, self.host)

        _id = 0

        data = {}

        resp = req.core_secrets_id_put(_id, data)
        print(resp.text)
        assert False

    def case_core_secrets_id_delete(self):
        req = Core(self.sess, self.host)

        _id = 0

        resp = req.core_secrets_id_delete(_id)
        print(resp.text)
        assert False

    def case_core_service_what_action_get(self, what, action):
        req = Core(self.sess, self.host)
        resp = req.core_service_what_action_get(what, action)
        assert resp.status_code == 200, \
            f"""Ошибка, 
            what: {what}
            action: {action}
            status_code: {resp.status_code}
            resp: {resp.text}
            """

    def case_core_service_all_restart_get(self, action):
        req = Core(self.sess, self.host)
        resp = req.core_services_all_action_get(action)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_core_sid_get(self):
        req = Core(self.sess, self.host)
        req.sess.headers.update({'skey': "ANGARA"})
        resp = req.core_sid_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_core_syslog_get(self):
        req = Core(self.sess, self.host)
        req.sess.headers.update({'skey': "ANGARA"})
        resp = req.core_syslog_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

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
