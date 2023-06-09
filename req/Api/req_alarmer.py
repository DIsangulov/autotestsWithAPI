from req.Helpers.base_req import BaseReq

rand_id = None


class Alarmer(BaseReq):

    def alarmer_notification_admin_all_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.alarmer/notification/admin/all", headers=header, verify=False)
        return resp

    def alarmer_notification_read_admin_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.alarmer/notification/read/admin", headers=header, verify=False)
        return resp

    def alarmer_notification_read_type_admin_post(self):
        body = {
            "id": 5590483
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.alarmer/notification/read/admin", headers=header, json=body,
                              verify=False)
        return resp

    def alarmer_notification_settings_admin_get(self):
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
            "link": "https://10.130.0.22/",
            "msg": "TestAPI",
            "to": "d.isangulov@ngrsoftlab.ru",
            "user_id": 11
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.alarmer/send_invitation", headers=header, json=body,
                              verify=False)
        return resp

    def alarmer_send_invitations_post(self):
        body = {
            "link": "https://10.130.0.22/",
            "msg": "TestAPI",
            "to": [
                "d.isangulov@ngrsoftlab.ru"
            ],
            "user_id": 11
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
            "message": "TestTest",
            "name": "TestAPI",
            "port": 587,
            "protocol": "smpt",
            "psw": "fHNHQBc7jEKfaO0kywZz!",
            "send_user": "dataplan_qaa@ngrsoftlab.ru",
            "to": "d.isangulov@ngrsoftlab.ru",
            "topic": "TestAPI",
            "user": "dataplan_qaa@ngrsoftlab.ru"
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.alarmer/send_msg", headers=header, json=body,
                              verify=False)
        return resp
