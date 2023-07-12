import requests

from req.Helpers.base_req import BaseReq

act_dir_pass = "d8hELYed9L809RB9FkSO!"
ssh_pass = "R3U7zYiyxVFtUq8QvRAJ"  # 22
# ssh_pass = "nCNmqNT<)>Bsr3c]"  # 16
mail_pass = "8327kHLHsfohn;hksjkfou!"


class Core(BaseReq):

    def core_active_directory_get(self) -> requests.Response:
        """process GET req for getting current ad settings"""
        return self.sess.get(f"{self.host}/back/dp.core/active_directory")

    def core_active_directory_post(self, body) -> requests.Response:
        """process POST req with new settings for domain active directory to test and save (if ok)"""
        return self.sess.post(f"{self.host}/back/dp.core/active_directory", json=body)

    def core_active_directory_structure_post(self, body) -> requests.Response:
        """process POST req for getting domain AD struct (by root dir input)"""
        return self.sess.post(f"{self.host}/back/dp.core/active_directory/structure", json=body)

    def core_active_directory_test_settings_post(self, body) -> requests.Response:
        """process POST req with new settings for domain active directory to test and save (if ok)"""
        return self.sess.post(f"{self.host}/back/dp.core/active_directory/test_settings", json=body)

    # TODO: [GET] /back/dp.core/backups

    # TODO: [POST] /back/dp.core/backups

    # TODO: [GET] /back/dp.core/backups/last

    # TODO: [GET] /back/dp.core/backups/{id}

    # TODO: [DELETE] /back/dp.core/backups

    # TODO: [POST] /back/dp.core/backups/{id}/restore

    # TODO: [POST] /back/dp.core/backups/{type}/upload

    # TODO: [GET] /back/dp.core/backups/{type}/{id}/download

    def core_check_get(self) -> requests.Response:
        """process GET req for checking if the installation has start settings."""
        return self.sess.get(f"{self.host}/back/dp.core/check")

    def core_common_get(self) -> requests.Response:
        """process GET req for getting current common settings"""
        return self.sess.get(f"{self.host}/back/dp.core/common")

    def core_common_post(self, body) -> requests.Response:
        """process POST req with new common settings"""
        return self.sess.post(f"{self.host}/back/dp.core/common", json=body)

    def core_common_test_post(self, body) -> requests.Response:
        """process POST req with common settings to test"""
        return self.sess.post(f"{self.host}/back/dp.core/common/test", json=body)

    def core_component_what_action_node(self, what, action, node) -> requests.Response:
        """process GET req for restarting/stopping node component services"""
        return self.sess.get(f"{self.host}/back/dp.core/component/{what}/{action}/{node}")

    def core_download_settings_get(self) -> requests.Response:
        """process GET req for getting static and dynamic settings"""
        return self.sess.get(f"{self.host}/back/dp.core/download_settings")

    def core_email_import_cert_post(self, body) -> requests.Response:
        """process POST req with new email cert for import"""
        return self.sess.post(f"{self.host}/back/dp.core/email/import_cert", json=body)

    def core_email_send_test_post(self, body) -> requests.Response:
        """process POST req with data for testing mail settings by test send"""
        return self.sess.post(f"{self.host}/back/dp.core/email/send_test", json=body)

    def core_email_type_get(self, _type) -> requests.Response:
        """process GET req for getting current email settings (type = in/out)"""
        return self.sess.get(f"{self.host}/back/dp.core/email/{_type}")

    def core_email_type_post(self, _type, body) -> requests.Response:
        """process POST req with new email settings (type = in/out)"""
        return self.sess.post(f"{self.host}/back/dp.core/email/{_type}", json=body)

    def core_flag_get(self) -> requests.Response:
        """process GET req with node settings to get has_nodes flag"""
        return self.sess.get(f"{self.host}/back/dp.core/flag")

    def core_ip_get(self) -> requests.Response:
        """process GET req for getting installation IP (haha)"""
        return self.sess.get(f"{self.host}/back/dp.core/ip")

    # TODO: [POST] /back/dp.core/nodes/delete/{what}

    def core_nodes_list_what_get(self, what) -> requests.Response:
        """process GET req for getting nodes list"""
        return self.sess.get(f"{self.host}/back/dp.core/nodes/list/{what}")

    def core_nodes_test_what_post(self, what, body) -> requests.Response:
        """process POST req with node settings to test node connection"""
        return self.sess.post(f"{self.host}/back/dp.core/nodes/test/{what}", json=body)

    def core_nodes_what(self, what) -> requests.Response:
        """process GET req for getting current remote nodes settings (sys settings page)"""
        return self.sess.get(f"{self.host}/back/dp.core/nodes/{what}")

    # TODO: [POST] /back/dp.core/nodes/{what}

    def core_nodes_what_post(self, what, body) -> requests.Response:
        """process POST req for setting current remote nodes ml&logstash settings (sys settings page)"""
        return self.sess.post(f"{self.host}/back/dp.core/nodes/{what}", json=body)

    # TODO: [GET] /back/dp.core/save

    # TODO: [GET] /back/dp.core/secrets

    # TODO: [POST] /back/dp.core/secrets

    # TODO: [GET] /back/dp.core/secrets/{id}

    # TODO: [PUT] /back/dp.core/secrets/{id}

    # TODO: [DELETE] /back/dp.core/secrets/{id}

    def core_service_what_action_get(self, what, action) -> requests.Response:
        """process GET req for restarting/stopping one webserver service"""
        # action: restart|stop
        return self.sess.get(f"{self.host}/back/dp.core/service/{what}/{action}")

    def core_services_all_action_get(self, action) -> requests.Response:
        """process GET req for restarting/stopping all webserver services"""
        # action: restart|stop
        return self.sess.get(f"{self.host}/back/dp.core/services/all/{action}")

    def core_sid_get(self) -> requests.Response:
        """process GET req for getting installation SID"""
        return self.sess.get(f"{self.host}/back/dp.core/sid")

    def core_syslog_get(self) -> requests.Response:
        """process GET req for getting current syslog settings"""
        return self.sess.get(f"{self.host}/back/dp.core/syslog")

    def core_syslog_post(self, body) -> requests.Response:
        """process POST req with new syslog settings"""
        return self.sess.post(f"{self.host}/back/dp.core/syslog",  json=body)
