import requests

from req.Helpers.base_req import BaseReq


class Core(BaseReq):

    def core_active_directory_get(self) -> requests.Response:
        """process GET req for getting current ad settings"""
        return self.sess.get(f"{self.host}/back/dp.core/active_directory")

    def core_active_directory_post(self, data) -> requests.Response:
        """process POST req with new settings for domain active directory to test and save (if ok)"""
        return self.sess.post(f"{self.host}/back/dp.core/active_directory", json=data)

    def core_active_directory_structure_post(self, data) -> requests.Response:
        """process POST req for getting domain AD struct (by root dir input)"""
        return self.sess.post(f"{self.host}/back/dp.core/active_directory/structure", json=data)

    def core_active_directory_test_settings_post(self, data) -> requests.Response:
        """process POST req with new settings for domain active directory to test and save (if ok)"""
        return self.sess.post(f"{self.host}/back/dp.core/active_directory/test_settings", json=data)

    def core_backups_get(self):
        """process GET req for getting list of service DB backups"""
        return self.sess.get(f"{self.host}/back/dp.core/backups")

    def core_backups_post(self, data):
        """process POST req for creating a service DB backup"""
        return self.sess.post(f"{self.host}/back/dp.core/backups", json=data)

    def core_backups_last_get(self):
        """process GET req for getting status of the last service DB backup/restore job"""
        return self.sess.get(f"{self.host}/back/dp.core/backups/last")

    def core_backups_id_get(self, _id):
        """process GET req for getting backup info by ID"""
        return self.sess.get(f"{self.host}/back/dp.core/backups/{_id}")

    def core_backups_id_delete(self, _id):
        """process DELETE req for deleting the service DB backup"""
        return self.sess.delete(f"{self.host}/back/dp.core/backups/{_id}")

    def core_backups_id_restore_post(self, _id, data):
        """process POST req for restoring the service DB backup"""
        return self.sess.post(f"{self.host}/back/dp.core/backups/{_id}/restore", json=data)

    def core_backups_type_upload_post(self, _type, data):
        """process POST req for importing external backup file"""
        return self.sess.post(f"{self.host}/back/dp.core/backups/{_type}/upload", json=data)

    def core_backups_type_id_download_get(self, _type, _id):
        """process GET req to download backup file by ID"""
        return self.sess.get(f"{self.host}/back/dp.core/backups/{_type}/{_id}/download")

    def core_check_get(self) -> requests.Response:
        """process GET req for checking if the installation has start settings."""
        return self.sess.get(f"{self.host}/back/dp.core/check")

    def core_common_get(self) -> requests.Response:
        """process GET req for getting current common settings"""
        return self.sess.get(f"{self.host}/back/dp.core/common")

    def core_common_post(self, data) -> requests.Response:
        """process POST req with new common settings"""
        return self.sess.post(f"{self.host}/back/dp.core/common", json=data)

    def core_common_test_post(self, data) -> requests.Response:
        """process POST req with common settings to test"""
        return self.sess.post(f"{self.host}/back/dp.core/common/test", json=data)

    def core_component_what_action_node(self, what, action, node) -> requests.Response:
        """process GET req for restarting/stopping node component services"""
        return self.sess.get(f"{self.host}/back/dp.core/component/{what}/{action}/{node}")

    def core_download_settings_get(self) -> requests.Response:
        """process GET req for getting static and dynamic settings"""
        return self.sess.get(f"{self.host}/back/dp.core/download_settings")

    def core_email_import_cert_post(self, data) -> requests.Response:
        """process POST req with new email cert for import"""
        return self.sess.post(f"{self.host}/back/dp.core/email/import_cert", json=data)

    def core_email_send_test_post(self, data) -> requests.Response:
        """process POST req with data for testing mail settings by test send"""
        return self.sess.post(f"{self.host}/back/dp.core/email/send_test", json=data)

    def core_email_type_get(self, _type) -> requests.Response:
        """process GET req for getting current email settings (type = in/out)"""
        return self.sess.get(f"{self.host}/back/dp.core/email/{_type}")

    def core_email_type_post(self, _type, data) -> requests.Response:
        """process POST req with new email settings (type = in/out)"""
        return self.sess.post(f"{self.host}/back/dp.core/email/{_type}", json=data)

    def core_flag_get(self) -> requests.Response:
        """process GET req with node settings to get has_nodes flag"""
        return self.sess.get(f"{self.host}/back/dp.core/flag")

    def core_ip_get(self) -> requests.Response:
        """process GET req for getting installation IP (haha)"""
        return self.sess.get(f"{self.host}/back/dp.core/ip")

    def core_nodes_delete_what_post(self, what, data):
        """process DELETE req for deleting remote node with ip."""
        return self.sess.post(f"{self.host}/back/dp.core/nodes/delete/{what}", json=data)

    def core_nodes_list_what_get(self, what) -> requests.Response:
        """process GET req for getting nodes list"""
        return self.sess.get(f"{self.host}/back/dp.core/nodes/list/{what}")

    def core_nodes_test_what_post(self, what, data) -> requests.Response:
        """process POST req with node settings to test node connection"""
        return self.sess.post(f"{self.host}/back/dp.core/nodes/test/{what}", json=data)

    def core_nodes_what_get(self, what) -> requests.Response:
        """process GET req for getting current remote nodes settings (sys settings page)"""
        return self.sess.get(f"{self.host}/back/dp.core/nodes/{what}")

    def core_nodes_what_post(self, what, data) -> requests.Response:
        """process POST req for setting current remote nodes ml&logstash settings (sys settings page)"""
        return self.sess.post(f"{self.host}/back/dp.core/nodes/{what}", json=data)

    def core_save_get(self):
        """process GET req for saving all start settings"""
        return self.sess.get(f"{self.host}/back/dp.core/save")

    def core_secrets_get(self):
        """process GET req for getting secrets list (with encrypted values)"""
        return self.sess.get(f"{self.host}/back/dp.core/secrets")

    def core_secrets_post(self, data):
        """process POST req for adding secret"""
        return self.sess.post(f"{self.host}/back/dp.core/secrets", json=data)

    def core_secrets_id_get(self, _id):
        """process GET req for getting secret by id (with encrypted values)"""
        return self.sess.get(f"{self.host}/back/dp.core/secrets/{_id}")

    def core_secrets_id_put(self, _id, data):
        """process PUT req for editing secret by id"""
        return self.sess.put(f"{self.host}/back/dp.core/secrets/{_id}", json=data)

    def core_secrets_id_delete(self, _id):
        """process DELETE req for deleting secret by id"""
        return self.sess.delete(f"{self.host}/back/dp.core/secrets/{_id}")

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

    def core_syslog_post(self, data) -> requests.Response:
        """process POST req with new syslog settings"""
        return self.sess.post(f"{self.host}/back/dp.core/syslog", json=data)
