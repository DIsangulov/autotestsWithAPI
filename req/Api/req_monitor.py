import requests

from req.Helpers.base_req import BaseReq


class Monitor(BaseReq):

    def monitor_dump_what_post(self, what, data) -> requests.Response:
        """process POST req for getting detailed dump with usage data"""
        return self.sess.post(f"{self.host}/back/dp.monitor/dump/{what}", json=data)

    def monitor_fast_graph_post(self, data):
        """get fast common system state graph (for main dashboard)"""
        return self.sess.post(f"{self.host}/back/dp.monitor/fast_graph", json=data)

    def monitor_fast_info_get(self):
        """get fast common system state (for main dashboard)"""
        return self.sess.get(f"{self.host}/back/dp.monitor/fast_info")

    def monitor_nodes_graphs_what_metric_post(self, what, metric, data) -> requests.Response:
        """process POST req for getting nodes current usage graph data"""
        return self.sess.post(f"{self.host}/back/dp.monitor/nodes/graphs/{what}/{metric}", json=data)

    def monitor_nodes_stats_what_get(self, what) -> requests.Response:
        """process GET req for getting nodes current usage data"""
        return self.sess.get(f"{self.host}/back/dp.monitor/nodes/stats/{what}")

    def monitor_webserver_graphs_metric_post(self, metric, data) -> requests.Response:
        """process POST req for getting webserver usage graphs data"""
        return self.sess.post(f"{self.host}/back/dp.monitor/webserver/graphs/{metric}", json=data)

    def monitor_webserver_groups_get(self) -> requests.Response:
        """process GET req for getting all webserver components stats"""
        return self.sess.get(f"{self.host}/back/dp.monitor/webserver/groups")

    def monitor_webserver_stats_what_get(self, what) -> requests.Response:
        """process GET req for getting webserver component what stats"""
        return self.sess.get(f"{self.host}/back/dp.monitor/webserver/stats/{what}")
