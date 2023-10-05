import requests

from req.Helpers.base_req import BaseReq


class Alarmer(BaseReq):

    def alarmer_alert_service_names_get(self):
        """process GET req with e-mail data for sending"""
        return self.sess.get(f"{self.host}/back/dp.alarmer/alert/service/names")

    def alarmer_email_server_post(self, data):
        """process POST to edit mail server receivers list (add new receiver)"""
        return self.sess.post(f"{self.host}/back/dp.alarmer/email_server", json=data)

    def alarmer_email_server_get(self):
        """process GET to get all mail server receivers list"""
        return self.sess.get(f"{self.host}/back/dp.alarmer/email_server")

    def alarmer_email_server_id_get(self, _id):
        """process GET to get mail server receivers by ID"""
        return self.sess.get(f"{self.host}/back/dp.alarmer/email_server/{_id}")

    def alarmer_email_server_id_delete(self, _id):
        """process DELETE to remove mail server receiver by ID"""
        return self.sess.delete(f"{self.host}/back/dp.alarmer/email_server/{_id}")

    def alarmer_notification_admin_all_get(self) -> requests.Response:
        """process GET to get all system notifications journal for all users"""
        return self.sess.get(f"{self.host}/back/dp.alarmer/notification/admin/all")

    def alarmer_notification_read_admin_get(self) -> requests.Response:
        """process GET to get not read notifications for System"""
        # исп: Перейти к Ленте уведомлений
        return self.sess.get(f"{self.host}/back/dp.alarmer/notification/read/admin")

    def alarmer_notification_read_type_post(self, _type, body) -> requests.Response:
        """process POST to save and send new notification"""
        return self.sess.post(f"{self.host}/back/dp.alarmer/notification/read/{_type}", json=body)

    def alarmer_notification_settings_admin_get(self) -> requests.Response:
        """process GET req to get admin user notify settings"""
        return self.sess.get(f"{self.host}/back/dp.alarmer/notification/settings/admin")

    def alarmer_notification_settings_common_get(self) -> requests.Response:
        """process GET req to get one user common notification settings (on/off, duration)"""
        return self.sess.get(f"{self.host}/back/dp.alarmer/notification/settings/common")

    def alarmer_notification_settings_common_post(self, body) -> requests.Response:
        """process POST to set common notification settings for one user"""
        return self.sess.post(f"{self.host}/back/dp.alarmer/notification/settings/common", json=body)

    def alarmer_notification_settings_user_get(self) -> requests.Response:
        """process GET req to get one user notification subscribe list"""
        return self.sess.get(f"{self.host}/back/dp.alarmer/notification/settings/user")

    def alarmer_notification_settings_userone_post(self, body) -> requests.Response:
        """process POST to get user notification settings for single object"""
        return self.sess.post(f"{self.host}/back/dp.alarmer/notification/settings/userone", json=body)

    def alarmer_notification_settings_type_post(self, _type, body) -> requests.Response:
        """process POST to set new settings for notification for one user"""
        return self.sess.post(f"{self.host}/back/dp.alarmer/notification/settings/{_type}", json=body)

    def alarmer_notification_settings_user_all_get(self) -> requests.Response:
        """process GET to get all notifications for all users"""
        return self.sess.get(f"{self.host}/back/dp.alarmer/notification/user/all")

    def alarmer_notification_type_get(self, _type) -> requests.Response:
        """process GET to get all notifications for user or admin"""
        return self.sess.get(f"{self.host}/back/dp.alarmer/notification/{_type}")

    def alarmer_notification_type_read_post(self, _type, data):
        """process POST to save and send new notification"""
        return self.sess.post(f"{self.host}//back/dp.alarmer/notification/{_type}/read", json=data)

    def alarmer_notifications_page_size_x_read_notify_type_page_x_get(self, page_size, notify_type, page):
        """process GET to get not read notifications page"""
        return self.sess.get(f"{self.host}/back/dp.alarmer/notifications/page-size/{page_size}/read/{notify_type}/page/{page}")

    def alarmer_send_invitation_post(self, body) -> requests.Response:
        """process POST req with invitational list for sending"""
        return self.sess.post(f"{self.host}/back/dp.alarmer/send_invitation", json=body)

    def alarmer_send_invitations_post(self, body) -> requests.Response:
        """process POST req with data for sending invitational mailing"""
        return self.sess.post(f"{self.host}/back/dp.alarmer/send_invitations", json=body)

    def alarmer_send_msg_post(self, body) -> requests.Response:
        """process POST req with e-mail data for sending"""
        return self.sess.post(f"{self.host}/back/dp.alarmer/send_msg", json=body)
