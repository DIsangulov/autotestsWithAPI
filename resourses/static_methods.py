import random
import datetime


def get_str_random_num(length: int = 4) -> str:
    """Возвращает приведенное к str число длины:length"""
    return str(random.randint(int(10**(length-1)), int(10**length-1)))


def get_datetime_now_z() -> str:
    # пример возврата: 2023-09-25T14:52:42Z
    return datetime.datetime.today().strftime("%Y-%m-%dT%H:%M:%SZ")

# TODO:

# get_datetime_now_z(minus='hour') # |hour|day|week|month|

# !не использовать минусы от timestamp; можно напороться на разницу по смене летнее-зимнее время
# get_datetime . hour_back
# get_datetime . day_back
# get_datetime . week_back

# TODO:
# def get_datetime_day_z() -> (str, str) # (2023-09-25T00:00:00Z, 2023-09-25T23:59:59Z)
# def get_datetime_day_z(hours=false) -> (str, str) # (2023-09-25, 2023-09-25)
