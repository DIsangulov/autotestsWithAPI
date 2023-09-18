QA_SPAM_EMAIL = "s.yezhov@ngrsoftlab.ru"

API_AUTO_TEST_ = "API_AUTO_TEST_"
UI_AUTO_TEST_ = "UI_AUTO_TEST_"


class DB_picker_tables:
    name = "picker_tables"


# TODO: добавить в предусловия проверку на наличие БД и таблицы
# Предполагается, что хранилище удаляться не будет
# Предполагается, что таблица 'boulder_general' наполнена данными
class DB_Shallow:
    name = "Shallow"

    tab_boulder_general = "boulder_general"
    col_timestamp = "timestamp"     # DateTime
    col_name = "name"               # String
    col_item_group = "item_group"   # Nullable(String)
    col_price = "price"             # Int32
