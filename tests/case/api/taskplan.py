from req.Helpers.user_session import UserSession
from req.Api.req_taskplan import Taskplan


class TaskplanCase(UserSession):

    def case_taskplan_add_task_post(self, sched_type, object_id):
        req = Taskplan(self.sess, self.host)

        data = {
            "sched_type": sched_type,
            "object_id": object_id,
            "schedule": {
                # "sched_id": 0,
                "flag": 0,
                "timezone": "Europe/Moscow",
                "interval": {
                    "val": "5",
                    "str": "hour"
                },
                # "day": {
                #     "val": "",
                #     "hhmm": "00:00"
                # },
                # "week": {
                #     "days": None,
                #     "hhmm": "00:00"
                # },
                # "month": {
                #     "var": 0,
                #     "day": "",
                #     "val": "",
                #     "val2": "",
                #     "wday": "",
                #     "wnum": "",
                #     "hhmm": "00:00"
                # }
            },
            "timezone": "Europe/Moscow"
        }
        resp = req.taskplan_add_task_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # \u003c (<)    # \u003e (>)
        # {"error":{"code":400,"description":"can not identify type of object: \u003cnil\u003e","msg":"Неверные параметры"}}

    def case_taskplan_delete_task(self):
        req = Taskplan(self.sess, self.host)
        data = None
        resp = req.taskplan_delete_task(data)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_taskplan_get_shedule_post(self, sched_type, object_id):
        req = Taskplan(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        data = {
            "sched_type": sched_type,
            "timezone": "Europe/Moscow",
            "data": {
                "object_id": object_id
            }
        }
        resp = req.taskplan_get_shedule_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # {"error":{"code":426,"msg":"Пожалуйста, установите расписание"}}
