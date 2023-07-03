import requests

from req.Helpers.base_req_raw import BaseReqRaw


class AlarmerNew(BaseReqRaw):

    # TODO: [GET] /back/dp.alarmer/alert/service/names

    # TODO: [POST] /back/dp.alarmer/email_serve     # serve > server (c) swagger

    # TODO: [GET] /back/dp.alarmer/email_server

    # TODO: [GET] /back/dp.alarmer/email_server/{id}

    # TODO: [DELETE] /back/dp.alarmer/email_server/{id}

    def alarmer_notification_admin_all_get(self) -> requests.Response:
        """process GET to get all system notifications journal for all users"""
        return self.sess.get(f"{self.host}/back/dp.alarmer/notification/admin/all")

    def alarmer_notification_read_admin_get(self) -> requests.Response:
        """process GET to get not read notifications for System"""
        # исп: Перейти к Ленте уведомлений
        return self.sess.get(f"{self.host}/back/dp.alarmer/notification/read/admin")

    def alarmer_notification_read_type_admin_post(self, _type, body) -> requests.Response:
        """process POST to save and send new notification"""
        return self.sess.post(f"{self.host}/back/dp.alarmer/notification/read/{_type}", json=body)

    def alarmer_notification_settings_admin_get(self) -> requests.Response:
        """process GET req to get admin user notify settings"""
        # исп: Настройки уведомлений
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

    # TODO: [POST] /back/dp.alarmer/notification/{type}/read

    # TODO: [GET] /back/dp.alarmer/notifications/pagi-size/{page_size}/read/{notify_type}/page/{page}

    def alarmer_send_invitation_post(self, body) -> requests.Response:
        """process POST req with invitational list for sending"""
        # https://tasks.ngrsoftlab.ru/browse/DAT-5291
        return self.sess.post(f"{self.host}/back/dp.alarmer/send_invitation", json=body)

    def alarmer_send_invitations_post(self, body) -> requests.Response:
        """process POST req with data for sending invitational mailing"""
        # https://tasks.ngrsoftlab.ru/browse/DAT-5291
        return self.sess.post(f"{self.host}/back/dp.alarmer/send_invitations", json=body)

    def alarmer_send_msg_post(self, body) -> requests.Response:
        """process POST req with e-mail data for sending"""
        return self.sess.post(f"{self.host}/back/dp.alarmer/send_msg", json=body)
