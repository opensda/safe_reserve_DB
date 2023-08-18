import psycopg2

from create_database.config import config

# Подключаемся к БД и вносим туда данные

# conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='12345')



# params = config()
# conn = psycopg2.connect(database='rosneft', **params)
# data_for_record = [('Роснефть', 'Директор', 50000, 'rosneft.ru')]
# try:
#     with conn:
#         with conn.cursor() as cur:
#             cur.executemany('INSERT INTO gazprom_vacancies VALUES (%s, %s, %s, %s)', data_for_record )
#             # cur.executemany('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', employees_for_record)
#             # cur.executemany('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', orders_for_record)
#
#
# finally:
#     conn.close()


def fill_the_table(db_name, data_to_record):
    params = config()
    conn = psycopg2.connect(database=db_name, **params)
    try:
        with conn:
            with conn.cursor() as cur:
                cur.executemany(f'INSERT INTO vacancies VALUES (%s, %s, %s, %s)', data_to_record)
                # cur.executemany('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', employees_for_record)
                # cur.executemany('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', orders_for_record)
    finally:
        conn.close()


# data_for_record = [('Роснефть-Pоснефть', 'Директор Сечина', 5000000, 'rosneft-путуин.ru')]
# db_name = 'rosneft'
# table_name = 'gazprom_vacancies'
#
# fill_the_table(db_name, table_name, data_for_record)