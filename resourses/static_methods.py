import random
import string
import datetime


def get_random_string(
        length: int = 8,
        *,
        add_symbols: str = "",
        uppercase: bool = True,
        lowercase: bool = True
) -> str:
    output_set = add_symbols
    if uppercase:
        output_set += string.ascii_uppercase
    if lowercase:
        output_set += string.ascii_lowercase

    return ''.join(random.choice(output_set) for _ in range(length))


def get_str_random_num(length: int = 4) -> str:
    """Возвращает приведенное к str число длины:length"""
    return str(random.randint(int(10**(length-1)), int(10**length-1)))


def get_datetime_now_z(*, day_delta: int = 0, hour_delta: int = 0) -> str:
    """Пример возврата: 2023-09-26T16:52:42Z"""
    dt_now = datetime.datetime.today() + datetime.timedelta(days=day_delta, hours=hour_delta)
    return dt_now.strftime("%Y-%m-%dT%H:%M:%SZ")


# def get_day_z(day_delta: int = 0) -> tuple[str, str]:
#     # Получение даты с округлением до крайних значений
#     dt_w_delta = datetime.datetime.today() + datetime.timedelta(days=day_delta)
#     dt_start = dt_w_delta.strftime("%Y-%m-%dT00:00:00Z")
#     dt_end = dt_w_delta.strftime("%Y-%m-%dT23:59:59Z")
#     return dt_start, dt_end
