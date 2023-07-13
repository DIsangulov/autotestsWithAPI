from req.Helpers.user_session import UserSession
from req.Api.req_alarmer import Alarmer
from resourses.credentials import DpQaa

_QA_SPAM_EMAIL = "s.yezhov@ngrsoftlab.ru"
API_AUTO_TEST_ = "API_AUTO_TEST_"


class AlarmerCase(UserSession):

    def case_alarmer_notification_admin_all_get(self):
        req = Alarmer(self.sess, self.host)

        resp = req.alarmer_notification_admin_all_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_alarmer_notification_read_admin_get(self):
        req = Alarmer(self.sess, self.host)

        resp = req.alarmer_notification_read_admin_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_alarmer_notification_read_type_admin_post(self):
        req = Alarmer(self.sess, self.host)

        _type = "admin"     # FIXME: какие ещё типы
        body = {
            "id": 5590483   # FIXME: magic?
        }
        resp = req.alarmer_notification_read_type_admin_post(_type, body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_alarmer_notification_settings_admin_get(self):
        req = Alarmer(self.sess, self.host)

        resp = req.alarmer_notification_settings_admin_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_alarmer_notification_settings_common_get(self):
        req = Alarmer(self.sess, self.host)

        resp = req.alarmer_notification_settings_common_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_alarmer_notification_settings_common_post(self):
        req = Alarmer(self.sess, self.host)

        body = {
            "get_sys_notify": True,
            "notify_duration": 1
        }
        resp = req.alarmer_notification_settings_common_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_alarmer_notification_settings_user_get(self):
        req = Alarmer(self.sess, self.host)

        resp = req.alarmer_notification_settings_user_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_alarmer_notification_settings_userone_post(self):
        req = Alarmer(self.sess, self.host)

        body = {
            "object_id": 1,
            "type": 1,
            "user_id": 1
        }
        resp = req.alarmer_notification_settings_userone_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_alarmer_notification_settings_type_post(self):
        req = Alarmer(self.sess, self.host)

        _type = "user"
        body = {
            "data": None    # TODO: add any data
        }
        resp = req.alarmer_notification_settings_type_post(_type, body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_alarmer_notification_settings_user_all_get(self):
        req = Alarmer(self.sess, self.host)

        resp = req.alarmer_notification_settings_user_all_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    # TODO: parametrize? type = user, type = admin
    def case_alarmer_notification_user_get(self):
        req = Alarmer(self.sess, self.host)

        _type = "user"      # TODO: add also 'admin'
        resp = req.alarmer_notification_type_get(_type)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_alarmer_send_invitation_post(self):
        # "user_id" > https://tasks.ngrsoftlab.ru/browse/DAT-5291
        req = Alarmer(self.sess, self.host)

        body = {
            # "link": "https://10.130.0.22/",  # нужно?
            # "msg": "TestAPI",                # нужно?
            "to": _QA_SPAM_EMAIL,
            # "user_id": 4870
        }
        resp = req.alarmer_send_invitation_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_alarmer_send_invitations_post(self):
        req = Alarmer(self.sess, self.host)

        body = {
            # "link": "https://10.130.0.22/",     # нужно?
            # "msg": "TestAPI",                   # нужно?
            "to": [
                _QA_SPAM_EMAIL
            ],
            # "user_id": 4870
        }
        resp = req.alarmer_send_invitations_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_alarmer_send_msg_post(self):
        req = Alarmer(self.sess, self.host)

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
        resp = req.alarmer_send_msg_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp
