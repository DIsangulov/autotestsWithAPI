from req.Helpers.base_req import BaseReq


class XbaCook(BaseReq):

    def xba_cook_anomalies_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/anomalies", headers=header, verify=False)
        return resp

    def xba_cook_anomalies_picker_max_min_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.xba_cook/anomalies/picker/max_min", headers=header, verify=False)
        return resp
