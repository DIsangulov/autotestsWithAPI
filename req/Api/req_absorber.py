import json

import pytest
import random

from req.Helpers.base_req import BaseReq

rand = None
con_id = None
logo_id = None
rand_logo_id = None
at_uid = None
pt_id = None
source_id = None


class Absorber(BaseReq):

    def peopler_users_at_uid_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.peopler/users", headers=header, verify=False)
        name = 'dataplan_qaa@ngrsoftlab.ru'
        users = json.loads(resp.text)['res']
        uid = next((user for user in users if user['name'] == name), None)
        global at_uid
        at_uid = uid['id']
        return resp

    def id_picker_table_get(self, token):  # забираем id таблицы picker_table
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/db",
                             headers=header, verify=False)
        json_data = json.loads(resp.text)
        global pt_id
        for item in json_data['res']:
            if item['name'] == 'picker_tables':
                pt_id = item['id']
        print(pt_id)
        return resp

    def absorber_library_columns_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.absorber/library/columns", headers=header, verify=False)
        return resp

    def absorber_library_conn_type_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.absorber/library/conn_type", headers=header, verify=False)
        return resp

    def absorber_library_conn_type_id_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.absorber/library/conn_type/1", headers=header, verify=False)
        return resp

    def absorber_library_connector_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.absorber/library/connector", headers=header, verify=False)
        dct = json.loads(resp.text)
        global con_id
        con_id = dct['res'][1]['id']  # получили id коннекта
        print(con_id)
        return resp

    def absorber_library_connector_post(self, token):
        global rand
        rand = random.randint(1200, 12500)
        header = {'token': token}
        data = {
            "name": str(rand),
            "description": "",
            "published": True,
            "opened": True,
            "params": None,
            "conn_type_id": 2,
            "data": "test",
            "order_column": "src",
            "is_system": False,
            "logo_id": None,
            "mapping": [
                {
                    "storage_name": "src",
                    "event_name": "src",
                    "type": "String"
                },
                {
                    "storage_name": "spt",
                    "event_name": "spt",
                    "type": "String"
                },
                {
                    "storage_name": "dst",
                    "event_name": "dst",
                    "type": "String"
                },
                {
                    "storage_name": "dpt",
                    "event_name": "dpt",
                    "type": "String"
                }
            ],
            "author_id": at_uid,
            "editor_id": at_uid,
            "created": "2022-01-13T12:13:46.668Z",
            "modified": "2022-01-13T12:13:46.668Z"
        }
        resp = self.sess.post(f"{self.host}/back/dp.absorber/library/connector", headers=header, json=data,
                              verify=False)
        return resp

    def absorber_library_connector_put(self, token):
        header = {'token': token}
        data = {
            "id": str(con_id),
            "name": str(rand) + str(2),
            "description": "",
            "published": False,
            "opened": False,
            "author_id": None,
            "author_name": "",
            "editor_id": at_uid,
            "editor_name": "Датаплан Тестов",
            "created": "0001-01-01T00:00:00Z",
            "edited": "2022-02-07T15:17:11.612497Z",
            "params": None,
            "conn_type_id": 2,
            "data": "test",
            "order_column": "src",
            "is_system": False,
            "logo_id": None,
            "mapping": [
                {
                    "storage_name": "src",
                    "event_name": "src",
                    "type": "String"
                },
                {
                    "storage_name": "spt",
                    "event_name": "spt",
                    "type": "String"
                },
                {
                    "storage_name": "dst",
                    "event_name": "dst",
                    "type": "String"
                },
                {
                    "storage_name": "dpt",
                    "event_name": "dpt",
                    "type": "String"
                }
            ],
            "modified": "2022-02-08T16:36:29.335Z"
        }
        resp = self.sess.put(f"{self.host}/back/dp.absorber/library/connector", headers=header, json=data, verify=False)
        return resp

    def absorber_library_connector_id_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.absorber/library/connector/" + str(con_id), headers=header,
                             verify=False)
        return resp

    def absorber_library_connector_delete(self, token):
        header = {'token': token}
        resp = self.sess.delete(f"{self.host}/back/dp.absorber/library/connector/" + str(con_id), headers=header,
                                verify=False)
        return resp

    def absorber_library_logo_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.absorber/library/logo", headers=header, verify=False)
        dct = json.loads(resp.text)
        global logo_id
        logo_id = dct['res'][1]['id']  # получили id лого
        print(logo_id)
        return resp

    def absorber_library_logo_post(self, token):  # тут начались косячки проверить на сваггере, возможен баг
        global rand_logo_id
        rand_logo_id = random.randint(120000, 1250000)
        header = {'token': token}
        data = {
            "name": str(rand_logo_id),
            "editor_id": at_uid,
            "id": rand_logo_id,
            "is_system": False,
            "data": None
        }
        resp = self.sess.post(f"{self.host}/back/dp.absorber/library/logo", headers=header, json=data, verify=False)
        print(rand_logo_id)
        return resp

    def absorber_library_logo_put(self, token):  # тут начались косячки проверить на сваггере, возможен баг
        header = {'token': token}
        data = {"data": None,
                "edited": "2022-12-07T14:30:46.313631Z",
                "editor_id": at_uid,
                "editor_name": "Тестов Датаплан",
                "id": 1110,
                "is_system": False,
                "name": "630244"
                }
        resp = self.sess.put(f"{self.host}/back/dp.absorber/library/logo", headers=header, json=data, verify=False)
        print(rand_logo_id)
        return resp

    def absorber_library_logo_delete(self, token):
        header = {'token': token}
        resp = self.sess.delete(f"{self.host}/back/dp.absorber/library/logo/" + str(logo_id), headers=header,
                                verify=False)
        return resp

    def absorber_source_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.absorber/source", headers=header, verify=False)
        dct = json.loads(resp.text)
        global source_id
        source_id = dct['res'][0]['id']  # получили id лого
        print(source_id)
        return resp

    def absorber_source_post(self, token):
        header = {'token': token}
        data = {
            "now": True,
            "name": "API_test" + str(rand),
            "description": "",
            "editor_id": at_uid,
            "author_id": at_uid,
            "node": 0,
            "conn_type_id": 7,
            "workers_count": 2,
            "is_on": True,
            "debug_is_on": True,
            "monitoring_interval": 10,
            "monitoring_metric": "hour",
            "logo": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAgEASABIAAD/2wBDAAEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/2wBDAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/wAARCAArAG8DAREAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD+/igAoAKACgAoAKACgAoAKACgAoAKACgAoAYXwcY/X/61ACeZ7fr/APWoAPM9v1/+tQB4VqP7U37M2keIrjwhq37RPwK0vxbaTta3fhfUfi78P7LxFa3Kv5bW9xolz4gi1KGdZP3bQyWyyB/lK7uKAPbrW+tr62t7yyngvLO7hjuLW7tZ47i2ubeZBJDPbzxF4poZY2V45Y2ZHRgysQQaAJ/M9v1/+tQAeZ7fr/8AWoA+dv2hP2vv2Wv2TdM0PWP2nP2hvgz8AtO8UTX9v4Yn+LfxH8K+Az4luNLjgl1KDw9B4i1Kwudbl0+O6tXvY9LhuntRdW3nKhuIQ4B6b8L/AIqfDz41fD7wn8VvhN4v0H4gfDfx3pEGv+DfGvhi/i1Pw94l0S6Z1ttV0jUIcxXljcGN/JnjJSQDKkjBoA7zzPb9f/rUAHme36//AFqADzPb9f8A61AC7x6GgA3j0NADGGWOPb+QoAbQB+Yv/BZbT/2otV/4Jk/te6f+xs3i3/hoC6+F13F4Uj+H0l9D8QrjR21PTl8cW3gKbSpItXj8YT+CTr8ehNojjXjesi6DnWWsQQD+H/8AYr/a2/4IDfF79hTTv+CcH7cf7MOlfsa/tYz+BvEXw58Sftk+OvgVpnjLxFo/x9vRcaRp/wAX9a+K+mR23xk8Nata+Kb+21/UvCPjdNG+HuhWOlXvhfxF4l0zwvbx3DAH7wf8FS/2/v8AgoJ/wRY/Y+/Yd8a/si/8Mf8A7Tf7GNp8L/hF8Bde+L/jv4afFnxH4u/4TfTfCV2+g/Ea2b4d/tEeGfCo+G3xJ8J6LBceGbOCXV7nS/EOn31hf+LNQj8ReHljAPs79rT9u3/gov4X+KH/AAS8+Cv7HXiT9gT4neNv27PA2sa54x1rxx8Lf2g9V8NaRp/g/wAG6V468X/G/wAG2vhX45eHtQ0X4OjRtWsrXQ/Dvii71zxdeateW9p/bc3lX7WYB8w+Of8Agtz+0R8ef+Chn7S/7B/7KHxG/YN/ZKl/ZUmufC+peOf2928fahqX7QvxB03Vn0fX7L4VaJ4S8ffDjTvCug+HbyF1mg1jUfFviLV7G703Wba3soprrT7MAz/+CmPj/wDan+O3/Btv+1b47/b5+DngH4Y/tOaMfE2heIfDng3wrr+j+DoYPBn7Slj4V8HeOPAlr4313xb4gh0jxn4Q03SPEula2Nclj1iy1SPU7BLKxvIbKAA0/gp/wU7+HX/BJ7/g3B/YH/aW8beFrj4heItV+C3w0+G/wp+Glpq6+H5PHXxE17T/ABNrFpp97rzadq/9h6FpWheHtd1/XNWGmXrxWemfYrS3m1K/sYJQDjP2iv8Agr3/AMFX/wDgmn8MP2RP2xv2/PhX+x58Tf2Tf2lde8L+GviF4I/Zr8LfF3wV8bfgTrPj7wPffEHwxp6698QfiZ4u8JeLdQsPD2j+Inv7KTR7Oz1bU/D11oseuaAb6y1UgH19/wAFBP8Agr/8WPAP7ZP/AAT/AP2Af2HdG+EOofE39u/wv4W+LOm/tC/G/SPF/i34U+DPg74rufFMGi6hovgHwh4n+Hmt+L/E+t2vhPV9YtUn8caLaadbRaXY3On3c3iFLzRgD5u/Yf8A+CoP/BWD9oD/AIKv/tF/8E2fiLd/8E+W079kG+g8T/FPxr4a+C37RegeI/iX8KbTxL4O0XWrv4f3cv7Q/i3wz4P8cfZfHnhy4stL8U6RrGnRXEuowPLfLpcsk4B/VbQAUAOb7x/D+lADaAPzh/4Ktah+2xof7G3irxN/wT50HWfF37TfhD4g/B3xh4a8G6JfeF7C58aeFPC/xN8M618RfCF1L4uu7LTJtK8S+CLLXNH1azt7hdZvNPu7i20RZNUktUIB/Oj/AMFW9f8AiB/wV0/ZZHwe8P8A/BBn9sDQ/wBvLX4vDXhzwV8Z/jV8Mfgx4J8LfAuGz19NV1s6T+0re/EGy8Q6l4Pnt31GBPDetaN4Y8M6jc6rPqOqWltfWGnvdgH7RRf8EmV8X/8ABETw/wD8Epfir4z0rX/Fmm/sz6Z8N4viKY77UdB0D4v6AD4o8H+J9Mju7aHVLnwv4K+IEOlrpsJtbPUbjwvpUdtHDZXEqpEAflB/wa3/AAU/aH8V6R4/+P8A+1tLDrfiL9kDwrrP/BMf9mq7Ew1Gz0rwD8NPiXrvj74w32matFd3el+IZpPFWpeDfhvaeLtIEEEvhj4Z6foCGSez1ie9APnr9uf9mvwJ+1z8U/21of2+f+CGn7V+s/tDp8QPiDo37MX7Wf8AwT78BLp1l8Wvh3pmhJoXwb8TfFnWNT+M9/4d1v4i2YtbNtX8S674V8TaJd6Cmj6Vd+EtLl8Lx6PcgFC3/Y9/4KQfs+f8G2Wv/sCfFz4EftHftG/tJftH+I/EL/Cr4Z/DDStK+JMH7KnwpsNf+GWvaF8Pviv4kl8U20Hh+wkuNE8U+I9C0nwufFY0y98Vv4XitbKPQ7/7AAX/AI2f8E0P2p/+CiH/AAby/s0fsoaJ+zl8b/gX+13/AME/9U8FX9h8MPjxoXhzwBb/AByutA8HeLfDviXTvhtrc3im/wBLudL1TSfGEd/4f1rxLP4ZnHiHw5J4f1GwsLfVI9ToA3f+ChGh/wDBQD/gs9+xv+xD/wAE6vCP7AH7Tv7N3jzQ/iJ8J/F37V3xx/aN8HeHPBHwQ8AQ/DL4c+I/Aes3Xg3XIPGGq6z44tNU1bxXdeKdP0+x0Wx16a00iw0e1sLqbUL+fTQDnf8Agsbp2u/Cv/got/wS1/Zv+DX7P8v7bifsk/sk21t8O/hH+zz8XJvhJ+234P8AiJ4Ds7jT9I8feJ/HXgW11D4i+Hvhla+BPDPhTxFoGhRtY+G9Z8RnxHda08iT6JbasAe5f8EmP24Pgh+z9/wUQvP2UvjP/wAEtP2iP2FP2vv28Y9b+IEnxr+OXxW8T/Hnxx8XbnSoPEHiCGDxl4z+Ikdl4usvD+p33hvxRa6Y3h19U0eDxPDp9tqWl2VvcvqulgH9kNABQBIyEknigBNh9v1/woANh9v1/wAKADyz7f5/CgD8e/8Ago3/AMEofFX7fHxW+FHxU8I/t6/tXfsc3vw48I6p4I1bSf2cfFM/hm28b6Hq+uJrlxJq09tqemsmqwSoILK7vIdYtLZFR104yKWYA/QT9lj9mP4Vfsc/s/fC/wDZp+CWk3Oj/DT4T+Hv7B0CLUbr7frOpXF3f3ut+IPEviHURDbjU/E3izxLqmr+J/EmpC3t1v8AXNXv7tLeBJVhQA+gNh9v1/woANh9v1/woAPLPt/n8KADYfb9f8KAPxd/an/4Iw+CPjR+2/4a/wCCkP7Pv7R/xd/Y6/bK0bwza+D9f+IXw90fwP8AELwd8Q9BstFj8MW8Pjn4bfEnRdW0jUrgeE7ey8LzfYr7TtOuNL0zSrifTJNa0611dAD1b4H/APBLfwv4T/apsf25/wBpz46fEf8AbM/a18M+C2+Hfwv+IXxK8P8Aw/8AAfgv4JeDbn+1v7V034SfCn4YeG/D3hvQdR10a5qseseJvEFz4r8SzQX11DaarZLeagbwA/UzYfb9f8KADYfb9f8ACgCWgAoAKACgAoAKACgAoAKACgAoAKACgAoA/9k=",
            "data": "",
            "params": [],
            "sys_info": {
                "ip": "127.0.0.1",
                "version": "1"
            },
            "mapping_list": [
                {
                    "mapping": [
                        {
                            "event_name": "name",
                            "storage_name": "TimeStamp",
                            "type": "DateTime"
                        }
                    ],
                    "order_column": "TimeStamp",
                    "db_id": pt_id,
                    "table_name": "ad_users_ngr",
                    "table_create_flag": 1,
                    "tag": "tag1"
                }
            ]
        }
        resp = self.sess.post(f"{self.host}/back/dp.absorber/source", headers=header, json=data, verify=False)
        return resp

    def absorber_source_put(self, token):
        header = {'token': token}
        data = {
            "now": True,
            # "name": "API_test" + str(rand),
            "description": "new description",
            "editor_id": at_uid,
            "author_id": at_uid,
            "node": 0,
            "conn_type_id": 7,
            "workers_count": 2,
            "is_on": True,
            "debug_is_on": True,
            "monitoring_interval": 10,
            "monitoring_metric": "hour",
            "logo": "data:image/jpeg;base64,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",
            "data": "",
            "params": None,
            "sys_info": {
                "ip": "127.0.0.1",
                "version": "1",
                "last_data_state": 0,
                "last_data_time": None,
                "log_last_executed": ""
            },
            "mapping_list": [
                {
                    "tag": "tag1",
                    "order_column": "TimeStamp",
                    "mapping": [
                        {
                            "storage_name": "TimeStamp",
                            "event_name": "name",
                            "type": "DateTime"
                        }
                    ],
                    "db_id": pt_id,
                    "table_name": "ad_users_ngr",
                    "table_create_flag": 3
                }
            ],
            "id": source_id
        }
        resp = self.sess.put(f"{self.host}/back/dp.absorber/source", headers=header, json=data, verify=False)
        return resp

    def absorber_source_id_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.absorber/source/" + str(source_id), headers=header, verify=False)
        return resp

    def absorber_source_id_debug_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.absorber/source/" + str(source_id) + "/debug", headers=header,
                             verify=False)
        return resp

    def absorber_source_id_delete(self, token):
        header = {'token': token}
        resp = self.sess.delete(f"{self.host}/back/dp.absorber/source/" + str(source_id), headers=header, verify=False)
        return resp
