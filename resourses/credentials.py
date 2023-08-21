import os

# TARGET_URL = os.environ.get('TARGET_URL', "https://10.130.0.22")
TARGET_URL = os.environ.get('TARGET_URL', "https://10.130.5.16")


class TestUsers:
    # /login  #  auth_data

    DpQaa = {
        "username": os.environ.get('TARGET_API_USER', "dataplan_qaa@ngrsoftlab.ru"),
        "password": os.environ.get('TARGET_API_PASSWORD', "fHNHQBc7jEKfaO0kywZz!!"),
        "local": False
    }

    DpQaaLocal = {
        "username": os.environ.get('TARGET_LOCAL_USER', "dataplan_qaa_local"),
        "password": os.environ.get('TARGET_LOCAL_PASSWORD', "so@you_came_back_to@me_again@@DdwIf991"),
        "local": True
    }
    # user0 = {}
    # user1 = {}
