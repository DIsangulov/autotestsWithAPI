from req.Helpers.base_req import BaseReq


class StorageWorker(BaseReq):

    def storage_worker_ask_one_sql_post(self, data):
        """process POST req with raw sql ask for executing it"""
        return self.sess.post(f"{self.host}/back/dp.storage_worker/ask_one_sql", json=data)

    def storage_worker_ask_plain_sql_post(self, data):
        """process POST req with "plain-constructed" sql ask params for executing it"""
        return self.sess.post(f"{self.host}/back/dp.storage_worker/ask_plain_sql", json=data)

    # TODO: [GET] /back/dp.storage_worker/backups

    # TODO: [POST] /back/dp.storage_worker/backups/table/{db_name}/{table_name}

    # TODO: [GET] /back/dp.storage_worker/backups/{id}

    # TODO: [DELETE] /back/dp.storage_worker/backups/{id}

    # TODO: [GET] /back/dp.storage_worker/backups/{id}/download

    # TODO: [POST] /back/dp.storage_worker/backups/{id}/restore

    # TODO: [POST] /back/dp.storage_worker/backups/{type}/upload

    def storage_worker_import_rules_get(self):
        """process GET to return db and tables import restrictions info"""
        return self.sess.get(f"{self.host}/back/dp.storage_worker/import_rules")

    def storage_worker_psevdo_namer_regs_get(self):
        """process GET req for getting list of regexps"""
        return self.sess.get(f"{self.host}/back/dp.storage_worker/psevdo_namer/regs")

    def storage_worker_psevdo_namer_regs_post(self, data):
        """process POST req for creating new regexp"""
        return self.sess.post(f"{self.host}/back/dp.storage_worker/psevdo_namer/regs", json=data)

    def storage_worker_psevdo_namer_regs_pid_get(self, _reg_pid):
        """process GET req for getting regexp with id=pid"""
        return self.sess.get(f"{self.host}/back/dp.storage_worker/psevdo_namer/regs/{_reg_pid}")

    # TODO: [PUT] /back/dp.storage_worker/psevdo_namer/regs/{pid}

    def storage_worker_psevdo_namer_regs_pid_delete(self, _reg_pid):
        """process DELETE req for deleting pid regexp"""
        return self.sess.delete(f"{self.host}/back/dp.storage_worker/psevdo_namer/regs/{_reg_pid}")

    def storage_worker_show_base_db_name_get(self, db_name):
        """process GET req for getting the DB structure"""
        return self.sess.get(f"{self.host}/back/dp.storage_worker/show_base/{db_name}")

    def storage_worker_statistics_db_event_stats_db_name_flag_post(self, db_name, flag, data):
        """process POST req for getting one db inserts dynamic"""
        return self.sess.post(f"{self.host}/back/dp.storage_worker/statistics/db_event_stats/{db_name}/{flag}", json=data)

    def storage_worker_statistics_db_one_tab_stats_db_name_tab_name_get(self, db_name, tab_name):
        """process GET req for getting one tables statistics info"""
        return self.sess.get(f"{self.host}/back/dp.storage_worker/statistics/db_one_tab_stats/{db_name}/{tab_name}")

    def storage_worker_statistics_db_search_post(self, data):
        """process POST req for getting columns matching search criteria"""
        return self.sess.post(f"{self.host}/back/dp.storage_worker/statistics/db_search", json=data)

    def storage_worker_statistics_db_stats_dbname_get(self, dbname):
        """process GET req for getting one db statistics info"""
        return self.sess.get(f"{self.host}/back/dp.storage_worker/statistics/db_stats/{dbname}")

    def storage_worker_statistics_db_tabs_event_stats_db_name_tab_name_flag_post(self, db_name, tab_name, flag, data):
        """process POST req for getting one table inserts dynamic"""
        return self.sess.post(f"{self.host}/back/dp.storage_worker/statistics/db_tabs_event_stats/{db_name}/{tab_name}/{flag}", json=data)

    def storage_worker_statistics_db_tabs_stats_dbname_get(self, dbname):
        """process GET req for getting all tables statistics info"""
        return self.sess.get(f"{self.host}/back/dp.storage_worker/statistics/db_tabs_stats/{dbname}")

    def storage_worker_statistics_storage_search_post(self, data):
        """process POST req for getting content search result"""
        return self.sess.post(f"{self.host}/back/dp.storage_worker/statistics/storage_search", json=data)

    def storage_worker_statistics_test_selection_post(self, data):
        """process POST req for getting column test selection"""
        return self.sess.post(f"{self.host}/back/dp.storage_worker/statistics/test_selection", json=data)

    def storage_worker_storage_db_get(self):
        """process GET to return all storage databases"""
        return self.sess.get(f"{self.host}/back/dp.storage_worker/storage/db")

    def storage_worker_storage_db_put(self, data):
        """process POST to edit storage db properties (description currently)"""
        return self.sess.put(f"{self.host}/back/dp.storage_worker/storage/db", json=data)

    def storage_worker_storage_db_post(self, data):
        """process POST to create new storage DB"""
        return self.sess.post(f"{self.host}/back/dp.storage_worker/storage/db", json=data)

    def storage_worker_storage_db_delete(self, db_name):
        """process DELETE to delete storage DB (if already exists)"""
        return self.sess.delete(f"{self.host}/back/dp.storage_worker/storage/db/{db_name}")

    def storage_worker_storage_import_csv_db_name_table_name_post(self, db_name, table_name, data):
        """process POST to insert fetched from csv data into DB table"""
        return self.sess.post(f"{self.host}/back/dp.storage_worker/storage/import_csv/{db_name}/{table_name}", json=data)

    def storage_worker_storage_import_json_db_name_table_name_post(self, db_name, table_name, data):
        """process POST to insert fetched from json data into DB table"""
        return self.sess.post(f"{self.host}/back/dp.storage_worker/storage/import_json/{db_name}/{table_name}", json=data)

    def storage_worker_storage_supported_engines_get(self):
        """process GET req to get available storage table engine list"""
        return self.sess.get(f"{self.host}/back/dp.storage_worker/storage/supported_engines")

    def storage_worker_storage_supported_types_get(self):
        """process GET req to get storage data types list"""
        return self.sess.get(f"{self.host}/back/dp.storage_worker/storage/supported_types")

    def storage_worker_storage_table_columns_db_name_tab_name_get(self, db_name, tab_name):
        """process GET req for getting table columns"""
        return self.sess.get(f"{self.host}/back/dp.storage_worker/storage/table/columns/{db_name}/{tab_name}")

    def storage_worker_storage_table_columns_db_name_table_name_post(self, db_name, table_name, data):
        """process POST to set aliases for columns"""
        return self.sess.post(f"{self.host}/back/dp.storage_worker/storage/table/columns/{db_name}/{table_name}", json=data)

    # TODO: [POST] /back/dp.storage_worker/storage/table/{db_name}

    # TODO: [POST] /back/dp.storage_worker/storage/table/{db_name}/{table_name}

    # TODO: [DELETE] /back/dp.storage_worker/storage/table/{db_name}/{table_name}

    def storage_worker_storage_table_db_name_table_name_ttl_get(self, db_name, table_name):
        """returns TTL settings for a table"""
        return self.sess.get(f"{self.host}/back/dp.storage_worker/storage/table/{db_name}/{table_name}/ttl")

    # TODO: [PUT] /back/dp.storage_worker/storage/table/{db_name}/{table_name}/ttl

    # TODO: [DELETE] /back/dp.storage_worker/storage/table/{db_name}/{table_name}/{column_name}

    def storage_worker_storage_table_db_name_table_name_count_get(self, db_name, table_name, count):
        """process GET to return to client a part of data from table"""
        return self.sess.get(f"{self.host}/back/dp.storage_worker/storage/table/{db_name}/{table_name}/{count}")

    # TODO: [POST] /back/dp.storage_worker/storage/view/{db_name}
