import json

from req.Helpers.user_session import UserSession
from req.Api.req_monitor import Monitor


def _get_sample_data() -> dict:
    s_data = {
            "end": "2023-02-14T00:00:00Z",
            "start": "2023-02-13T00:00:00Z",
            "timeFlag": "",
            "timezone": "Europe/Moscow"
        }
    return s_data


class MonitorCase(UserSession):

    def case_monitor_dump_server_post(self):
        req = Monitor(self.sess, self.host)

        what = "server"
        data = _get_sample_data()
        resp = req.monitor_dump_what_post(what, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_monitor_dump_nodes_post(self):
        req = Monitor(self.sess, self.host)

        what = "nodes"
        data = _get_sample_data()
        resp = req.monitor_dump_what_post(what, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_monitor_fast_graph_post(self):
        req = Monitor(self.sess, self.host)

        _time_flags = [
            "0",    # Сегодня
            "1",    # Вчера
            "2",    # Неделя
            "3",    # Месяц
            "4",    # Год
        ]

        resp = None
        for t_flag in _time_flags:
            # ? отсутствие ключа 'timeFlag' возвращает 3549 значений
            data = {
                "timeFlag": t_flag,
                "timezone": "UTC"
            }

            resp = req.monitor_fast_graph_post(data)
            assert resp.status_code == 200, f"Ошибка, код: {resp.status_code}, post_data:{data}, resp.text: {resp.text}"

    def case_monitor_fast_info_get(self):
        req = Monitor(self.sess, self.host)

        resp = req.monitor_fast_info_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        resp_res = json.loads(resp.text)['res']
        keys = [
            "cpu",
            "event_count",
            "koef",
            "ram",
            "session_count",
            "source_count",
            "state",
            "table_count",
            "user_count",
        ]
        assert len(resp_res) == len(keys), \
            f"Число ключей в ответе 'res':{{...}}: {len(resp_res)}, Ожидаемое число: {len(keys)}"
        for _key in keys:
            assert _key in resp_res, f"Нет ключа: {_key} в ответе 'res':{resp_res}"

    def case_monitor_nodes_graphs_ml_metrics_post(self):
        req = Monitor(self.sess, self.host)
        what = "ml"
        metrics = "ram", "cpu", "iops", "network", "picked"
        data = _get_sample_data()

        for one_metric in metrics:
            resp = req.monitor_nodes_graphs_what_metric_post(what, one_metric, data)
            assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, metric: {one_metric},\nresp.text: {resp.text}"
            # print(resp.text)

    def case_monitor_nodes_graphs_picker_metrics_post(self):
        req = Monitor(self.sess, self.host)
        what = "picker"
        metrics = "ram", "cpu", "iops", "network", "picked"
        data = _get_sample_data()
        for one_metric in metrics:
            resp = req.monitor_nodes_graphs_what_metric_post(what, one_metric, data)
            assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, metric: {one_metric},\nresp.text: {resp.text}"
            # print(resp.text)

    def case_monitor_nodes_graphs_servicedb_metrics_post(self):
        req = Monitor(self.sess, self.host)
        what = "servicedb"
        metrics = "ram", "cpu", "iops", "network", "picked"
        data = _get_sample_data()
        for one_metric in metrics:
            resp = req.monitor_nodes_graphs_what_metric_post(what, one_metric, data)
            assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, metric: {one_metric},\nresp.text: {resp.text}"
            # print(resp.text)

    def case_monitor_nodes_graphs_datastore_metrics_post(self):
        req = Monitor(self.sess, self.host)
        what = "datastore"
        metrics = "ram", "cpu", "iops", "network", "picked"
        data = _get_sample_data()
        for one_metric in metrics:
            resp = req.monitor_nodes_graphs_what_metric_post(what, one_metric, data)
            assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, metric: {one_metric},\nresp.text: {resp.text}"
            # print(resp.text)

    def case_monitor_nodes_stats_ml_get(self):
        req = Monitor(self.sess, self.host)
        what = "ml"
        resp = req.monitor_nodes_stats_what_get(what)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_monitor_nodes_stats_picker_get(self):
        req = Monitor(self.sess, self.host)
        what = "picker"
        resp = req.monitor_nodes_stats_what_get(what)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_monitor_nodes_stats_servicedb_get(self):
        req = Monitor(self.sess, self.host)
        what = "servicedb"
        resp = req.monitor_nodes_stats_what_get(what)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_monitor_nodes_stats_datastore_get(self):
        req = Monitor(self.sess, self.host)
        what = "datastore"
        resp = req.monitor_nodes_stats_what_get(what)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_monitor_webserver_graphs_ram_post(self):
        req = Monitor(self.sess, self.host)
        metric = "ram"
        data = _get_sample_data()
        resp = req.monitor_webserver_graphs_metric_post(metric, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_monitor_webserver_graphs_cpu_post(self):
        req = Monitor(self.sess, self.host)
        metric = "cpu"
        data = _get_sample_data()
        resp = req.monitor_webserver_graphs_metric_post(metric, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_monitor_webserver_graphs_iops_post(self):
        req = Monitor(self.sess, self.host)
        metric = "iops"
        data = _get_sample_data()
        resp = req.monitor_webserver_graphs_metric_post(metric, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_monitor_webserver_graphs_network_post(self):
        req = Monitor(self.sess, self.host)
        metric = "network"
        data = _get_sample_data()
        resp = req.monitor_webserver_graphs_metric_post(metric, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_monitor_webserver_groups_get(self):
        req = Monitor(self.sess, self.host)
        resp = req.monitor_webserver_groups_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_monitor_webserver_stats_sys_get(self):
        req = Monitor(self.sess, self.host)
        what = "sys"
        resp = req.monitor_webserver_stats_what_get(what)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_monitor_webserver_stats_visual_get(self):
        req = Monitor(self.sess, self.host)
        what = "visual"
        resp = req.monitor_webserver_stats_what_get(what)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_monitor_webserver_stats_analytics_get(self):
        req = Monitor(self.sess, self.host)
        what = "analytics"
        resp = req.monitor_webserver_stats_what_get(what)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_monitor_webserver_stats_datastore_get(self):
        req = Monitor(self.sess, self.host)
        what = "datastore"
        resp = req.monitor_webserver_stats_what_get(what)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_monitor_webserver_stats_dataproc_get(self):
        req = Monitor(self.sess, self.host)
        what = "dataproc"
        resp = req.monitor_webserver_stats_what_get(what)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)
