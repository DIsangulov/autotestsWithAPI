from req.Helpers.base_req import BaseReq
from resourses.credentials import DpQaa

_QA_SPAM_EMAIL = "s.yezhov@ngrsoftlab.ru"
API_AUTO_TEST_ = "API_AUTO_TEST_"


class Alarmer(BaseReq):

    # TODO: [GET] /back/dp.alarmer/alert/service/names

    # TODO: [POST] /back/dp.alarmer/email_serve     # serve > server (c) swagger

    # TODO: [GET] /back/dp.alarmer/email_server

    # TODO: [GET] /back/dp.alarmer/email_server/{id}

    # TODO: [DELETE] /back/dp.alarmer/email_server/{id}

    def alarmer_notification_admin_all_get(self):
        """process GET to get all system notifications journal for all users"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.alarmer/notification/admin/all", headers=header, verify=False)
        return resp

    def alarmer_notification_read_admin_get(self):
        """process GET to get not read notifications for System"""
        # исп: Перейти к Ленте уведомлений
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.alarmer/notification/read/admin", headers=header, verify=False)
        return resp

    def alarmer_notification_read_type_admin_post(self):
        """process POST to save and send new notification"""
        _type = "admin"     # FIXME: какие ещё типы
        body = {
            "id": 5590483   # FIXME: magic?
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.alarmer/notification/read/{_type}", headers=header, json=body, verify=False)
        return resp

    def alarmer_notification_settings_admin_get(self):
        """process GET req to get admin user notify settings"""
        # исп: Настройки уведомлений
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.alarmer/notification/settings/admin", headers=header, verify=False)
        return resp

    def alarmer_notification_settings_common_get(self):
        """process GET req to get one user common notification settings (on/off, duration)"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.alarmer/notification/settings/common", headers=header, verify=False)
        return resp

    def alarmer_notification_settings_common_post(self):
        """process POST to set common notification settings for one user"""
        body = {
            "get_sys_notify": True,
            "notify_duration": 1
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.alarmer/notification/settings/common", headers=header, json=body, verify=False)
        return resp

    def alarmer_notification_settings_user_get(self):
        """process GET req to get one user notification subscribe list"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.alarmer/notification/settings/user", headers=header, verify=False)
        return resp

    def alarmer_notification_settings_userone_post(self):
        """process POST to get user notification settings for single object"""
        body = {
            "object_id": 1,
            "type": 1,
            "user_id": 1
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.alarmer/notification/settings/userone", headers=header, json=body, verify=False)
        return resp

    def alarmer_notification_settings_type_post(self):
        """process POST to set new settings for notification for one user"""
        _type = "user"
        body = {
            "data": None    # TODO: add any data
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.alarmer/notification/settings/{_type}", headers=header, json=body, verify=False)
        return resp

    def alarmer_notification_settings_user_all_get(self):
        """process GET to get all notifications for all users"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.alarmer/notification/user/all", headers=header, verify=False)
        return resp

    def alarmer_notification_type_get(self):
        """process GET to get all notifications for user or admin"""
        _type = "user"      # TODO: add also 'admin'
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.alarmer/notification/{_type}", headers=header, verify=False)
        return resp

    # TODO: [POST] /back/dp.alarmer/notification/{type}/read

    # TODO: [GET] /back/dp.alarmer/notifications/pagi-size/{page_size}/read/{notify_type}/page/{page}

    def alarmer_send_invitation_post(self):
        """process POST req with invitational list for sending"""
        # https://tasks.ngrsoftlab.ru/browse/DAT-5291
        body = {
            # "link": "https://10.130.0.22/",  # нужно?
            # "msg": "TestAPI",                # нужно?
            "to": _QA_SPAM_EMAIL,
            "user_id": 4870     # FIXME: могу отправлять сообщения от другого имени?
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.alarmer/send_invitation", headers=header, json=body, verify=False)
        return resp

    def alarmer_send_invitations_post(self):
        """process POST req with data for sending invitational mailing"""
        # https://tasks.ngrsoftlab.ru/browse/DAT-5291
        body = {
            # "link": "https://10.130.0.22/",     # нужно?
            # "msg": "TestAPI",                   # нужно?
            "to": [
                _QA_SPAM_EMAIL
            ],
            "user_id": 4870     # FIXME: могу отправлять сообщения от другого имени?
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.alarmer/send_invitations", headers=header, json=body, verify=False)
        return resp

    def alarmer_send_msg_post(self):
        """process POST req with e-mail data for sending"""
        body = {
            "topic": API_AUTO_TEST_ + "topic",
            "message": API_AUTO_TEST_ + "message",
            "name": API_AUTO_TEST_ + "name",
            "description": API_AUTO_TEST_ + "alarmer_desc",
            "disable_tls": False,
            "host": "NGR-Exchange01.ngrsoftlab.ru",
            "port": 587,
            "protocol": "smpt",
            "to": _QA_SPAM_EMAIL,
            # "send_user": DpQaa.USER,
            "send_user": "Владимир Даль",       # FIXME: Имя отправителя в полученном сообщении
            "psw": DpQaa.PASS,      # пароль для аунтефикации
            "user": DpQaa.USER      # имя для аунтефикации
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.alarmer/send_msg", headers=header, json=body, verify=False)
        return resp

    # TODO: (14/21)
