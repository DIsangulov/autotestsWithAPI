import json

from req.Helpers.user_session import UserSession
from req.Api.req_monitor import Monitor
from resourses.static_methods import get_datetime_now_z


def _get_sample_data() -> dict:
    s_data = {
        "start": get_datetime_now_z(day_delta=-7),
        "end": get_datetime_now_z(),
        "offset": 0,
        "timeFlag": 0,
    }
    return s_data.copy()


class MonitorCase(UserSession):

    def case_monitor_dump_server_post(self):
        req = Monitor(self.sess, self.host)

        what = "server"
        data = _get_sample_data()
        resp = req.monitor_dump_what_post(what, data)
        assert resp.status_code == 200, f"Ошибка, code: {resp.status_code}, post_data: {data}, resp: {resp.text}"

    def case_monitor_dump_nodes_post(self):
        req = Monitor(self.sess, self.host)

        what = "nodes"
        data = _get_sample_data()
        resp = req.monitor_dump_what_post(what, data)
        assert resp.status_code == 200, f"Ошибка, code: {resp.status_code}, post_data: {data}, resp: {resp.text}"

    def case_monitor_fast_graph_post(self):
        req = Monitor(self.sess, self.host)

        _time_flags = (
            0,    # Сегодня
            1,    # Вчера
            2,    # Неделя
            3,    # Месяц
            4,    # Год
        )

        data = {"offset": 180}
        for t_flag in _time_flags:
            # ? отсутствие ключа 'timeFlag' возвращает 3549 значений

            data.update({"timeFlag": t_flag})

            resp = req.monitor_fast_graph_post(data)
            assert resp.status_code == 200, f"Ошибка, код: {resp.status_code}, post_data:{data}, resp: {resp.text}"
            # DAT-5479
            assert resp.text != '{"res":null}\n', f"status_code: {resp.status_code}\npost_data: {data}\nresp: {resp.text}"
            assert len(json.loads(resp.text)["res"]) > 0, f"status_code: {resp.status_code}\npost_data: {data}\nresp: {resp.text}"

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

    def case_monitor_nodes_graphs_what_metric_post(self):
        what_keys = ("ml", "picker", "servicedb", "datastore")
        metric_keys = ("ram", "cpu", "iops", "network", "picked")

        req = Monitor(self.sess, self.host)

        data = _get_sample_data()
        for what in what_keys:
            for metric in metric_keys:
                resp = req.monitor_nodes_graphs_what_metric_post(what, metric, data)
                assert resp.status_code == 200, f"Ошибка, code: {resp.status_code}, \
                what: {what}, metric: {metric}, post_data: {data}\nresp: {resp.text}"

    def case_monitor_nodes_stats_what_get(self):
        what_keys = ("ml", "picker", "servicedb", "datastore")

        req = Monitor(self.sess, self.host)

        for what in what_keys:
            resp = req.monitor_nodes_stats_what_get(what)
            assert resp.status_code == 200, f"Ошибка, code: {resp.status_code}, \
            what: {what}, resp: {resp.text}"

    def case_monitor_webserver_graphs_metric_post(self):
        metric_keys = ("ram", "cpu", "iops", "network")

        req = Monitor(self.sess, self.host)
        data = _get_sample_data()

        for metric in metric_keys:
            resp = req.monitor_webserver_graphs_metric_post(metric, data)
            assert resp.status_code == 200, f"Ошибка, code: {resp.status_code}, \
            metric: {metric}, post_data: {data}\nresp: {resp.text}"

    def case_monitor_webserver_groups_get(self):
        req = Monitor(self.sess, self.host)
        resp = req.monitor_webserver_groups_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_monitor_webserver_stats_sys_get(self):
        req = Monitor(self.sess, self.host)
        what = "sys"
        resp = req.monitor_webserver_stats_what_get(what)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_monitor_webserver_stats_visual_get(self):
        req = Monitor(self.sess, self.host)
        what = "visual"
        resp = req.monitor_webserver_stats_what_get(what)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_monitor_webserver_stats_analytics_get(self):
        req = Monitor(self.sess, self.host)
        what = "analytics"
        resp = req.monitor_webserver_stats_what_get(what)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_monitor_webserver_stats_datastore_get(self):
        req = Monitor(self.sess, self.host)
        what = "datastore"
        resp = req.monitor_webserver_stats_what_get(what)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_monitor_webserver_stats_dataproc_get(self):
        req = Monitor(self.sess, self.host)
        what = "dataproc"
        resp = req.monitor_webserver_stats_what_get(what)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
