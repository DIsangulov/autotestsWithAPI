from req.Helpers.base_req import BaseReq


class Monitor(BaseReq):

    def monitor_anomals_flag_0_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/anomals/0", headers=header, json=data, verify=False)
        return resp

    def monitor_anomals_flag_1_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/anomals/1", headers=header, json=data, verify=False)
        return resp

    def monitor_anomals_flag_2_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/anomals/2", headers=header, json=data, verify=False)
        return resp

    def monitor_anomals_flag_3_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/anomals/3", headers=header, json=data, verify=False)
        return resp

    def monitor_anomals_flag_4_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/anomals/4", headers=header, json=data, verify=False)
        return resp

    def monitor_dump_server_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/dump/server", headers=header, json=data, verify=False)
        return resp

    def monitor_dump_nodes_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/dump/nodes", headers=header, json=data, verify=False)
        return resp

    # -----------------------------------------------------------
    def monitor_nodes_graphs_ml_ram_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/nodes/graphs/ml/ram", headers=header, json=data,
                              verify=False)
        return resp

    def monitor_nodes_graphs_ml_cpu_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/nodes/graphs/ml/cpu", headers=header, json=data,
                              verify=False)
        return resp

    def monitor_nodes_graphs_ml_iops_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/nodes/graphs/ml/iops", headers=header, json=data,
                              verify=False)
        return resp

    def monitor_nodes_graphs_ml_network_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/nodes/graphs/ml/network", headers=header, json=data,
                              verify=False)
        return resp

    def monitor_nodes_graphs_ml_picked_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/nodes/graphs/ml/picked", headers=header, json=data,
                              verify=False)
        return resp

    def monitor_nodes_graphs_picker_ram_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/nodes/graphs/picker/ram", headers=header, json=data,
                              verify=False)
        return resp

    def monitor_nodes_graphs_picker_cpu_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/nodes/graphs/picker/cpu", headers=header, json=data,
                              verify=False)
        return resp

    def monitor_nodes_graphs_picker_iops_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/nodes/graphs/picker/iops", headers=header, json=data,
                              verify=False)
        return resp

    def monitor_nodes_graphs_picker_network_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/nodes/graphs/picker/network", headers=header, json=data,
                              verify=False)
        return resp

    def monitor_nodes_graphs_picker_picked_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/nodes/graphs/picker/picked", headers=header, json=data,
                              verify=False)
        return resp

    def monitor_nodes_graphs_servicedb_ram_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/nodes/graphs/servicedb/ram", headers=header, json=data,
                              verify=False)
        return resp

    def monitor_nodes_graphs_servicedb_cpu_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/nodes/graphs/servicedb/cpu", headers=header, json=data,
                              verify=False)
        return resp

    def monitor_nodes_graphs_servicedb_iops_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/nodes/graphs/servicedb/iops", headers=header, json=data,
                              verify=False)
        return resp

    def monitor_nodes_graphs_servicedb_network_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/nodes/graphs/servicedb/network", headers=header, json=data,
                              verify=False)
        return resp

    def monitor_nodes_graphs_servicedb_picked_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/nodes/graphs/servicedb/picked", headers=header, json=data,
                              verify=False)
        return resp

    def monitor_nodes_graphs_datastore_ram_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/nodes/graphs/datastore/ram", headers=header, json=data,
                              verify=False)
        return resp

    def monitor_nodes_graphs_datastore_cpu_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/nodes/graphs/datastore/cpu", headers=header, json=data,
                              verify=False)
        return resp

    def monitor_nodes_graphs_datastore_iops_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/nodes/graphs/datastore/iops", headers=header, json=data,
                              verify=False)
        return resp

    def monitor_nodes_graphs_datastore_network_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/nodes/graphs/datastore/network", headers=header, json=data,
                              verify=False)
        return resp

    def monitor_nodes_graphs_datastore_picked_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/nodes/graphs/datastore/picked", headers=header, json=data,
                              verify=False)
        return resp

    def monitor_nodes_stats_ml_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.monitor/nodes/stats/ml", headers=header, verify=False)
        return resp

    def monitor_nodes_stats_picker_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.monitor/nodes/stats/picker", headers=header, verify=False)
        return resp

    def monitor_nodes_stats_servicedb_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.monitor/nodes/stats/servicedb", headers=header, verify=False)
        return resp

    def monitor_nodes_stats_datastore_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.monitor/nodes/stats/datastore", headers=header, verify=False)
        return resp

    def monitor_webserver_graphs_ram_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/webserver/graphs/ram", headers=header, json=data,
                              verify=False)
        return resp

    def monitor_webserver_graphs_cpu_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/webserver/graphs/cpu", headers=header, json=data,
                              verify=False)
        return resp

    def monitor_webserver_graphs_iops_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/webserver/graphs/iops", headers=header, json=data,
                              verify=False)
        return resp

    def monitor_webserver_graphs_network_post(self, token):
        data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.monitor/webserver/graphs/network", headers=header, json=data,
                              verify=False)
        return resp

    def monitor_webserver_groups_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.monitor/webserver/groups", headers=header, verify=False)
        return resp

    def monitor_webserver_stats_sys_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.monitor/webserver/stats/sys", headers=header, verify=False)
        return resp

    def monitor_webserver_stats_visual_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.monitor/webserver/stats/visual", headers=header, verify=False)
        return resp

    def monitor_webserver_stats_analytics_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.monitor/webserver/stats/analytics", headers=header, verify=False)
        return resp

    def monitor_webserver_stats_datastore_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.monitor/webserver/stats/datastore", headers=header, verify=False)
        return resp

    def monitor_webserver_stats_dataproc_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.monitor/webserver/stats/dataproc", headers=header, verify=False)
        return resp
