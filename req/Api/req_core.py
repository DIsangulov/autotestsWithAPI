from req.Helpers.base_req import BaseReq


class Core(BaseReq):

    def core_active_directory_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/active_directory", headers=header, verify=False)
        return resp

    def core_active_directory_post(self, token):
        body = {
            "base_dn": "OU=Employees,DC=ngrsoftlab,DC=ru",
            "host": "192.168.189.2",
            "open_ldap": False,
            "password": "dfXjtp2uNI",
            "port": 636,
            "tls": True,
            "user": "dataplan@ngrsoftlab.ru"
        }
        header = {'token': token, 'skey': "ANGARA"}
        resp = self.sess.post(f"{self.host}/back/dp.core/active_directory", headers=header, json=body, verify=False)
        return resp

    def core_active_directory_structure_post(self, token):
        body = {
            "base_dn": "OU=Employees,DC=ngrsoftlab,DC=ru",
            "host": "192.168.189.2",
            "open_ldap": False,
            "password": "dfXjtp2uNI",
            "port": 636,
            "tls": True,
            "user": "dataplan@ngrsoftlab.ru"
        }
        header = {'token': token, 'skey': "ANGARA"}
        resp = self.sess.post(f"{self.host}/back/dp.core/active_directory/structure", headers=header, json=body,
                              verify=False)
        return resp

    def core_active_directory_test_settings_post(self, token):
        body = {
            "base_dn": "OU=Employees,DC=ngrsoftlab,DC=ru",
            "host": "192.168.189.2",
            "open_ldap": False,
            "password": "dfXjtp2uNI",
            "port": 636,
            "tls": True,
            "user": "dataplan@ngrsoftlab.ru"
        }
        header = {'token': token, 'skey': "ANGARA"}
        resp = self.sess.post(f"{self.host}/back/dp.core/active_directory/test_settings", headers=header, json=body,
                              verify=False)
        return resp

    def core_check(self, token):
        header = {'token': token, 'skey': "ANGARA"}
        resp = self.sess.get(f"{self.host}/back/dp.core/check", headers=header, verify=False)
        return resp

    def core_common_get(self, token):
        header = {'token': token, 'skey': "ANGARA"}
        resp = self.sess.get(f"{self.host}/back/dp.core/common", headers=header, verify=False)
        return resp

    def core_common_post(self, token):
        body = {"XMLName": {"Space": "", "Local": "common"},
                "sessions": "7|day",
                "ml": "",
                "query": "",
                "diagram": "",
                "report": "",
                "admin_ssh_user": "dataplan",
                "admin_ssh_password": "R3U7zYiyxVFtUq8QvRAJ",
                "msg_language": ""}
        header = {'token': token, 'skey': "ANGARA"}
        resp = self.sess.post(f"{self.host}/back/dp.core/common", headers=header, json=body, verify=False)
        return resp

    def core_common_test_post(self, token):
        body = {"XMLName": {"Space": "", "Local": "common"},
                "sessions": "7|day",
                "ml": "",
                "query": "",
                "diagram": "",
                "report": "",
                "admin_ssh_user": "dataplan",
                "admin_ssh_password": "R3U7zYiyxVFtUq8QvRAJ",
                "msg_language": ""}
        header = {'token': token, 'skey': "ANGARA"}
        resp = self.sess.post(f"{self.host}/back/dp.core/common/test", headers=header, json=body, verify=False)
        return resp

    # --------------------------------COMPONENT START-------------------------------
    def core_component_ml_restart(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/component/ml/restart/0", headers=header, verify=False)
        return resp

    def core_component_picker_restart(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/component/picker/restart/0", headers=header, verify=False)
        return resp

    def core_component_servicedb_restart(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/component/servicedb/restart/0", headers=header, verify=False)
        return resp

    def core_component_datastore_restart(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/component/datastore/restart/0", headers=header, verify=False)
        return resp

    # --------------------------------COMPONENT END-------------------------------

    def core_download_settings(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/download_settings", headers=header, verify=False)
        return resp

    def core_send_test(self, token):
        body = {
            "description": "TestAPICore",
            "disable_tls": False,
            "host": "NGR-Exchange01.ngrsoftlab.ru",
            "name": "TestAPI",
            "port": 587,
            "protocol": "smtp",
            "psw": "Fs5PUWnxTW",
            "send_user": "svc_ngr_mail@ngrsoftlab.ru",
            "user": "svc_ngr_mail@ngrsoftlab.ru"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.core/email/send_test", headers=header, json=body, verify=False)
        return resp

    def core_email_in_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/email/in", headers=header, verify=False)
        return resp

    def core_email_out_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/email/out", headers=header, verify=False)
        return resp

    def core_email_in_post(self, token):
        body = {
            "description": "TestAPICore",
            "disable_tls": False,
            "host": "NGR-Exchange01.ngrsoftlab.ru",
            "name": "TestAPI",
            "port": 587,
            "protocol": "smtp",
            "psw": "Fs5PUWnxTW",
            "send_user": "svc_ngr_mail@ngrsoftlab.ru",
            "user": "svc_ngr_mail@ngrsoftlab.ru"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.core/email/in", headers=header, json=body, verify=False)
        return resp

    def core_email_out_post(self, token):
        body = {
            "description": "TestAPICore",
            "disable_tls": False,
            "host": "NGR-Exchange01.ngrsoftlab.ru",
            "name": "TestAPI",
            "port": 587,
            "protocol": "smtp",
            "psw": "Fs5PUWnxTW",
            "send_user": "svc_ngr_mail@ngrsoftlab.ru",
            "user": "svc_ngr_mail@ngrsoftlab.ru"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.core/email/out", headers=header, json=body, verify=False)
        return resp

    def core_flag(self, token):
        header = {'token': token, 'skey': "ANGARA"}
        resp = self.sess.get(f"{self.host}/back/dp.core/flag", headers=header, verify=False)
        return resp

    def core_ip(self, token):
        header = {'token': token, 'skey': "ANGARA"}
        resp = self.sess.get(f"{self.host}/back/dp.core/ip", headers=header, verify=False)
        return resp

    # --------------------------------NODES LIST WHAT--------------------------------

    def core_nodes_list_ml_get(self, token):
        header = {'token': token, 'skey': "ANGARA"}
        resp = self.sess.get(f"{self.host}/back/dp.core/nodes/list/ml", headers=header, verify=False)
        return resp

    def core_nodes_list_picker_get(self, token):
        header = {'token': token, 'skey': "ANGARA"}
        resp = self.sess.get(f"{self.host}/back/dp.core/nodes/list/picker", headers=header, verify=False)
        return resp

    def core_nodes_list_servicedb_get(self, token):
        header = {'token': token, 'skey': "ANGARA"}
        resp = self.sess.get(f"{self.host}/back/dp.core/nodes/list/servicedb", headers=header, verify=False)
        return resp

    def core_nodes_list_datastore_get(self, token):
        header = {'token': token, 'skey': "ANGARA"}
        resp = self.sess.get(f"{self.host}/back/dp.core/nodes/list/datastore", headers=header, verify=False)
        return resp

    # --------------------------------NODES LIST WHAT--------------------------------
    # def core_nodes_test_datastore_post(self, token):  # здесь нужны данные
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
    #     header = {'token': token, 'skey': "ANGARA"}
    #     resp = self.sess.post(f"{self.host}/back/dp.core/nodes/test/datastore", headers=header, json=body, verify=False)
    #     return resp

    # --------------------------------NODES WHAT--------------------------------

    def core_nodes_ml_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/nodes/ml", headers=header, verify=False)
        return resp

    def core_nodes_picker_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/nodes/picker", headers=header, verify=False)
        return resp

    def core_nodes_servicedb_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/nodes/servicedb", headers=header, verify=False)
        return resp

    def core_nodes_datastore_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/nodes/datastore", headers=header, verify=False)
        return resp

    def core_nodes_datastore_post(self, token):  # здесь нужны данные
        body = {"active": 0,
                "has_nodes": "0",
                "what": "datastore",
                "ssh_user": "dataplan",
                "ssh_password": "R3U7zYiyxVFtUq8QvRAJ",
                "store_user": "default",
                "" "store_password": "1q2w3e4r5t",
                "db": "",
                "nodes": [
                    {"XMLName": {"Space": "", "Local": "node"}, "param": "8000000", "threads": "1",
                     "ip_node": "127.0.0.1", "ssh_port": "22", "store_port": "8123", "keyIdForFront": "127.0.0.1"}]}
        header = {'token': token, 'skey': "ANGARA"}
        resp = self.sess.post(f"{self.host}/back/dp.core/nodes/datastore", headers=header, json=body, verify=False)
        return resp

    def core_nodes_datastore_delete(self, token):
        header = {'token': token, 'skey': "ANGARA"}
        resp = self.sess.delete(f"{self.host}/back/dp.core/nodes/datastore", headers=header, verify=False)
        return resp

    # --------------------------------NODES WHAT--------------------------------

    # --------------------------------SERVICE WHAT ACTION--------------------------------

    def core_service_dp_alarmer(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_alarmer/restart", headers=header, verify=False)
        return resp

    def core_service_dp_auth(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_auth/restart", headers=header, verify=False)
        return resp

    def core_service_dp_core(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_core/restart", headers=header, verify=False)
        return resp

    def core_service_dp_licenser(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_licenser/restart", headers=header, verify=False)
        return resp

    def core_service_dp_log_eater(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_log_eater/restart", headers=header, verify=False)
        return resp

    def core_service_dp_monitor(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_monitor/restart", headers=header, verify=False)
        return resp

    def core_service_dp_peopler(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_peopler/restart", headers=header, verify=False)
        return resp

    def core_service_dp_permitter(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_permitter/restart", headers=header, verify=False)
        return resp

    def core_service_dp_postgres_single(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_postgres_single/restart", headers=header,
                             verify=False)
        return resp

    def core_service_dp_taskplan(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_taskplan/restart", headers=header, verify=False)
        return resp

    def core_service_dp_updater(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_updater/restart", headers=header, verify=False)
        return resp

    def core_service_dp_absorber(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_absorber/restart", headers=header, verify=False)
        return resp

    def core_service_dp_picker(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_picker/restart", headers=header, verify=False)
        return resp

    def core_service_dp_storage_single(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_storage_single/restart", headers=header,
                             verify=False)
        return resp

    def core_service_dp_storage_worker(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_storage_worker/restart", headers=header,
                             verify=False)
        return resp

    def core_service_dp_ml(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_ml/restart", headers=header, verify=False)
        return resp

    def core_service_dp_scripter(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_scripter/restart", headers=header, verify=False)
        return resp

    def core_service_dp_datapie_baker(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_datapie_baker/restart", headers=header, verify=False)
        return resp

    def core_service_dp_elements_eater(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_elements_eater/restart", headers=header,
                             verify=False)
        return resp

    def core_service_dp_frontend(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_frontend/restart", headers=header, verify=False)
        return resp

    def core_service_dp_reporter(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_reporter/restart", headers=header, verify=False)
        return resp

    def core_service_dp_rm_cook(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_rm_cook/restart", headers=header, verify=False)
        return resp

    def core_service_dp_rm_ml(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_rm_ml/restart", headers=header, verify=False)
        return resp

    def core_service_dp_screener(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_screener/restart", headers=header, verify=False)
        return resp

    def core_service_dp_visualisation(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_visualisation/restart", headers=header, verify=False)
        return resp

    def core_service_dp_xba_cook(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_xba_cook/restart", headers=header, verify=False)
        return resp

    def core_service_dp_xba_py(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/service/dp_xba_py/restart", headers=header, verify=False)
        return resp

    # --------------------------------SERVICE WHAT ACTION--------------------------------

    def core_service_all_restart(self, token):  # стенд не тянет этот метод
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.core/services/all/restart", headers=header, verify=False)
        return resp

    def core_sid(self, token):
        header = {'token': token, 'skey': "ANGARA"}
        resp = self.sess.get(f"{self.host}/back/dp.core/sid", headers=header, verify=False)
        return resp

    def core_syslog_get(self, token):
        header = {'token': token, 'skey': "ANGARA"}
        resp = self.sess.get(f"{self.host}/back/dp.core/syslog", headers=header, verify=False)
        return resp

    def core_syslog_post(self, token):
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
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.core/syslog", headers=header, json=body, verify=False)
        return resp
