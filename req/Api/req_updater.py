from req.Helpers.base_req import BaseReq


class Updater(BaseReq):

    def updater_additions_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.updater/additions", headers=header, verify=False)
        return resp

    def updater_additions_addition_delete(self):
        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.updater/additions/geo_ip", headers=header, verify=False)
        return resp

    def updater_additions_addition_post(self):
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.updater/additions/geo_ip", headers=header, verify=False)
        return resp

    def updater_check_updates_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.updater/check_updates", headers=header, verify=False)
        return resp
