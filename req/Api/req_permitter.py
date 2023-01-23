from req.Helpers.base_req import BaseReq


class Permitter(BaseReq):

    def permitter_check_ui_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/check_ui", headers=header, verify=False)
        return resp

    def permitter_db_watcher_all_db(self, token):
        header = {'token': token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/all_db", headers=header, verify=False)
        return resp

    def permitter_db_watcher_all_tables(self, token):
        header = {'token': token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/all_tables", headers=header, verify=False)
        return resp

    def permitter_db_watcher_db_tables(self, token):
        header = {'token': token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/db_tables/1", headers=header, verify=False)
        return resp

    def permitter_db_watcher_empty_role_dbs(self, token):
        header = {'token': token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/empty_role_dbs", headers=header, verify=False)
        return resp

    def permitter_db_watcher_empty_role_tables(self, token):
        header = {'token': token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/empty_role_tables", headers=header,
                             verify=False)
        return resp

    def permitter_db_watcher_empty_role_tables_id(self, token):
        header = {'token': token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/empty_role_tables/1", headers=header,
                             verify=False)
        return resp

    def permitter_db_watcher_get_tab_name_id(self, token):
        header = {'token': token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/get_tab_name/3573040", headers=header,
                             verify=False)
        return resp
