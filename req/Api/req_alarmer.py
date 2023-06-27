from req.Helpers.base_req import BaseReq
from resourses.credentials import DpQaa

_QA_SPAM_EMAIL = "s.yezhov@ngrsoftlab.ru"
API_AUTO_TEST_ = "API_AUTO_TEST_"


class Alarmer(BaseReq):

    def alarmer_notification_admin_all_get(self):
        """process GET to get all system notifications journal for all users"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.alarmer/notification/admin/all", headers=header, verify=False)
        return resp

    def alarmer_notification_read_admin_get(self):
        # исп: Перейти к Ленте уведомлений
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.alarmer/notification/read/admin", headers=header, verify=False)
        return resp

    def alarmer_notification_read_type_admin_post(self):
        body = {
            "id": 5590483  # FIXME: magic?
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.alarmer/notification/read/admin", headers=header, json=body, verify=False)
        return resp

    def alarmer_notification_settings_admin_get(self):
        # исп: Настройки уведомлений
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.alarmer/notification/settings/admin", headers=header, verify=False)
        return resp

    def alarmer_notification_settings_common_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.alarmer/notification/settings/common", headers=header, verify=False)
        return resp

    def alarmer_notification_settings_common_post(self):
        body = {
            "get_sys_notify": True,
            "notify_duration": 1
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.alarmer/notification/settings/common", headers=header, json=body, verify=False)
        return resp

    def alarmer_notification_settings_user_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.alarmer/notification/settings/user", headers=header, verify=False)
        return resp

    def alarmer_notification_settings_userone_post(self):
        body = {
            "object_id": 1,
            "type": 1,
            "user_id": 1
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.alarmer/notification/settings/userone", headers=header, json=body, verify=False)
        return resp

    def alarmer_notification_settings_type_post(self):  # мегастранный запрос и большой
        body = {
            "data": None
        }
        header = {'token': self.token}
        # FIXME: не тот EP
        resp = self.sess.post(f"{self.host}/back/dp.alarmer/notification/settings/user", headers=header, json=body, verify=False)
        return resp

    def alarmer_notification_settings_user_all_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.alarmer/notification/user/all", headers=header, verify=False)
        return resp

    def alarmer_notification_user_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.alarmer/notification/user", headers=header, verify=False)
        return resp

    def alarmer_send_invitation_post(self):
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
