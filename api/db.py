import logging
import psycopg2

DB_ARGS = "dbname=test user=postgres password=test host=localhost port=5432"


# функция подключение к БД
def conDB():
    try:
        conn = psycopg2.connect(DB_ARGS)
    except:
        logging.error("Unable to connect to the database.")
        return None
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    return cur


# функция добавления пользователя
def insertUser(cur, name, age, mail, password):
    cur.execute("INSERT INTO person(name, age, mail, password) VALUES(%s, %s, %s, %s)", (name, age, mail, password))
