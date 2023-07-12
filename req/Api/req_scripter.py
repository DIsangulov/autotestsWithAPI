import requests

from req.Helpers.base_req import BaseReq


class Scripter(BaseReq):

    def scripter_category_get(self):
        """process GET tot get script categories (analytics/parsers/services)"""
        return self.sess.get(f"{self.host}/back/dp.scripter/category")

    def scripter_libs_get(self):
        """process GET to get script libs list"""
        # исп: front>при создании скрипта>возвращает список "Разрешенные пакеты и библиотеки python"
        return self.sess.get(f"{self.host}/back/dp.scripter/libs")

    def scripter_script_get(self):
        """process GET to get list of all scripts"""
        return self.sess.get(f"{self.host}/back/dp.scripter/script")

    def scripter_script_put(self, data):
        """process PUT to edit existing script"""
        return self.sess.put(f"{self.host}/back/dp.scripter/script", json=data)

    def scripter_script_post(self, data):
        """process POST to create new script"""
        return self.sess.post(f"{self.host}/back/dp.scripter/script", json=data)

    def scripter_script_exec_list_get(self):
        """process GET to get list of all scripts with access level exec"""
        return self.sess.get(f"{self.host}/back/dp.scripter/script/exec_list")

    def scripter_script_start_post(self, data):
        """process POST req to start script (if not started and user have rights for that)"""
        return self.sess.post(f"{self.host}/back/dp.scripter/script/start", json=data)

    def scripter_script_stop_id_get(self, _script_id):
        """process GET req to stop script (if script started and user have rights for that)"""
        return self.sess.get(f"{self.host}/back/dp.scripter/script/stop/{_script_id}")

    def scripter_script_id_get(self, _script_id):
        """process GET to get script by id"""
        return self.sess.get(f"{self.host}/back/dp.scripter/script/{_script_id}")

    def scripter_script_id_delete(self, _script_id):
        """process DELETE to delete script by id (set flag deleted)"""
        return self.sess.delete(f"{self.host}/back/dp.scripter/script/{_script_id}")

    def scripter_script_id_files_get(self, _script_id):
        """process GET to get script files by id"""
        return self.sess.get(f"{self.host}/back/dp.scripter/script/{_script_id}/files")

    def scripter_script_id_files_put(self, _script_id, data):
        """process GET to update script files by id"""
        return self.sess.put(f"{self.host}/back/dp.scripter/script/{_script_id}/files", json=data)

    def scripter_script_id_log_get(self, _script_id: int) -> requests.Response:
        """process GET to get script's history states (list of logs)"""
        return self.sess.get(f"{self.host}/back/dp.scripter/script/{_script_id}/log")

    def scripter_script_id_log_delete(self, _script_id):
        """process DELETE to delete all script logs from now"""
        return self.sess.delete(f"{self.host}/back/dp.scripter/script/{_script_id}/log")

    def scripter_script_id_log_last_get(self, _script_id):
        """process GET to get script's history last log"""
        return self.sess.get(f"{self.host}/back/dp.scripter/script/{_script_id}/log/last")

    def scripter_script_script_id_log_log_id_get(self, _script_id, _log_id):
        """process GET to get script log text by log history ID"""
        return self.sess.get(f"{self.host}/back/dp.scripter/script/{_script_id}/log/{_log_id}")

    def scripter_script_script_id_log_log_id_delete(self, _script_id, _log_id):
        """process DELETE to delete script log by history id"""
        return self.sess.delete(f"{self.host}/back/dp.scripter/script/{_script_id}/log/{_log_id}")

    def scripter_script_script_type_get(self, script_type):
        """process GET to get list of scripts on main script page depending on it's type (admin/user)"""
        return self.sess.get(f"{self.host}/back/dp.scripter/script/{script_type}")

    def scripter_sequence_get(self):
        """process GET req to get full list of sequences"""
        return self.sess.get(f"{self.host}/back/dp.scripter/sequence")

    def scripter_sequence_put(self, data):
        """process PUT to edit existing sequence"""
        return self.sess.put(f"{self.host}/back/dp.scripter/sequence", json=data)

    def scripter_sequence_post(self, data):
        """process POST to create new sequence"""
        return self.sess.post(f"{self.host}/back/dp.scripter/sequence", json=data)

    def scripter_sequence_log_id_get(self, _seq_id):
        """process GET to get sequence states (logs list) by ID"""
        # исп: получить логи >> front: проваливаешься в скрипт;
        return self.sess.get(f"{self.host}/back/dp.scripter/sequence/log/{_seq_id}")

    def scripter_sequence_start_post(self, data):
        """process POST req to start sequence (if it was not started and user have rights for that)"""
        return self.sess.post(f"{self.host}/back/dp.scripter/sequence/start", json=data)

    def scripter_sequence_stop_id_get(self, _seq_id):
        """process GET to stop sequence (if it started and user have rights for that)"""
        return self.sess.get(f"{self.host}/back/dp.scripter/sequence/stop/{_seq_id}")

    def scripter_sequence_id_get(self, _seq_id):
        """process GET tot get sequence by id"""
        return self.sess.get(f"{self.host}/back/dp.scripter/sequence/{_seq_id}")

    def scripter_sequence_id_delete(self, seq_id):
        """process DELETE to Delete sequence by ID"""
        return self.sess.delete(f"{self.host}/back/dp.scripter/sequence/{seq_id}")

    def scripter_sequence_id_log_delete(self, seq_id):
        """process DELETE to delete all sequence logs from now"""
        return self.sess.delete(f"{self.host}/back/dp.scripter/sequence/{seq_id}/log")

    def scripter_sequence_sequence_id_log_last_get(self, _seq_id):
        """process GET to get sequence last log"""
        return self.sess.get(f"{self.host}/back/dp.scripter/sequence/{_seq_id}/log/last")

    def scripter_sequence_sequence_id_log_log_id_get(self, sequence_id, log_id):
        """process GET to get sequence log text by log ID"""
        return self.sess.get(f"{self.host}/back/dp.scripter/sequence/{sequence_id}/log/{log_id}")

    def scripter_sequence_sequence_id_log_log_id_delete(self, sequence_id, log_id):
        """process DELETE to delete sequence log by history id"""
        return self.sess.delete(f"{self.host}/back/dp.scripter/sequence/{sequence_id}/log/{log_id}")

    def scripter_sequence_sequence_type_get(self, sequence_type):
        """process GET req to get list of admin/user sequences"""
        return self.sess.get(f"{self.host}/back/dp.scripter/sequence/{sequence_type}")
