from req.Helpers.base_req import BaseReq
from resourses.credentials import DpQaa

_QA_SPAM_EMAIL = "s.yezhov@ngrsoftlab.ru"


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
        resp = self.sess.post(f"{self.host}/back/dp.alarmer/notification/read/admin", headers=header, json=body,
                              verify=False)
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
        resp = self.sess.post(f"{self.host}/back/dp.alarmer/notification/settings/common", headers=header, json=body,
                              verify=False)
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
        resp = self.sess.post(f"{self.host}/back/dp.alarmer/notification/settings/userone", headers=header, json=body,
                              verify=False)
        return resp

    def alarmer_notification_settings_type_post(self):  # мегастранный запрос и большой
        body = {
            "data": None
        }
        header = {'token': self.token}
        # FIXME: не тот EP
        resp = self.sess.post(f"{self.host}/back/dp.alarmer/notification/settings/user", headers=header, json=body,
                              verify=False)
        return resp

    def alarmer_notification_settings_user_all_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.alarmer/notification/user/all", headers=header,
                             verify=False)
        return resp

    def alarmer_notification_user_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.alarmer/notification/user", headers=header,
                             verify=False)
        return resp

    def alarmer_send_invitation_post(self):
        body = {
            # "link": "https://10.130.0.22/",  # нужно?
            # "msg": "TestAPI",                # нужно?
            "to": _QA_SPAM_EMAIL,
            "user_id": 7741  # FIXME: могу отправлять сообщения от другого имени?
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.alarmer/send_invitation", headers=header, json=body,
                              verify=False)
        return resp

    def alarmer_send_invitations_post(self):
        body = {
            # "link": "https://10.130.0.22/",     # нужно?
            # "msg": "TestAPI",                   # нужно?
            "to": [
                _QA_SPAM_EMAIL
            ],
            "user_id": 7741
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.alarmer/send_invitations", headers=header, json=body,
                              verify=False)
        return resp

    def alarmer_send_msg_post(self):
        body = {
            "description": "TestApiAlarmer",
            "disable_tls": False,
            "host": "NGR-Exchange01.ngrsoftlab.ru",
            "message": "TestAPI_message",
            "name": "TestAPI_name",
            "port": 587,
            "protocol": "smpt",
            "send_user": DpQaa.USER,
            "psw": DpQaa.PASS,
            # "to": "d.isangulov@ngrsoftlab.ru",
            "to": _QA_SPAM_EMAIL,
            "topic": "TestAPI_topic",
            "user": DpQaa.USER
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.alarmer/send_msg", headers=header, json=body, verify=False)
        return resp
