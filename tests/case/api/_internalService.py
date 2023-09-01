import requests

from req.Helpers.user_session import UserSession
from resourses.credentials import TARGET_URL


class InternalServiceCase:

    def case_dat_5566(self):

        session = requests.Session()

        port = 60077

        # self.sess.headers.update({'skey': "ANGARA"})
        session.headers.update({'skey': "ANGARA"})
        # resp = session.post(f"{TARGET_URL}:{port}/back/update_settings")
        resp = session.post(f"https://10.130.5.16:60077/back/update_settings")

        print(f"status_code: {resp.status_code}")
        print(f"resp_text: {resp.text}")
