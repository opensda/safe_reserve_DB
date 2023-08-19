import psycopg2

from src.classes.db_class__.config import config


params = config()
conn = psycopg2.connect(database='lukoil', **params)
try:
    with conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM vacancies')
            rows = cur.fetchall()
            for row in rows:
                print(row)



finally:
    conn.close()