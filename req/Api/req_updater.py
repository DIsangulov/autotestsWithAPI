from req.Helpers.base_req import BaseReq


class Updater(BaseReq):

    def updater_additions_get(self):
        """process GET req to get list of available additions"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.updater/additions", headers=header, verify=False)
        return resp

    def updater_additions_addition_post(self):
        """process POST req to install addition"""
        addition = "geo_ip"     # FIXME: какие ещё есть? << updater_additions_get
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.updater/additions/{addition}", headers=header, verify=False)
        return resp

    def updater_additions_addition_delete(self):
        """process DELETE req to delete addition data (if user has access to addition database)"""
        addition = "geo_ip"
        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.updater/additions/{addition}", headers=header, verify=False)
        return resp

    def updater_check_updates_get(self):
        """process GET req to get info 'product can be updated'"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.updater/check_updates", headers=header, verify=False)
        return resp

    # TODO: def [POST] /back/dp.updater/update

    # TODO: def [POST] /back/dp.updater/update_from_archive

    # TODO new: /back/dp.updater/versions   # https://tasks.ngrsoftlab.ru/browse/DAT-5287
