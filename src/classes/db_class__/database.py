import psycopg2

from src.classes.db_class__.config import config

class DataBase:
    def __init__(self, db_name):
        self.db_name = db_name

    def __str__(self):
        return self.db_name

    def get_companies_and_vacancies_count(self):
        params = config()
        conn = psycopg2.connect(database=self.db_name, **params)
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """SELECT company_name, COUNT (*) FROM vacancies
                                GROUP BY company_name
                                ORDER BY COUNT (*) DESC"""
                    )

                    rows = cur.fetchall()
                    for row in rows:
                        print(f'Название компании: {row[0]}\n'
                              f'Количество вакансий: {row[1]}\n ')


        finally:
            conn.close()



    def get_all_vacancies(self):
        params = config()
        conn = psycopg2.connect(database=self.db_name, **params)
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """SELECT * FROM vacancies"""
                    )

                    rows = cur.fetchall()
                    for row in rows:
                        print(f'Название компании: {row[0]}\n'
                              f'Название вакансии: {row[1]}\n'
                              f'Заработная плата: {row[2]}\n'
                              f'Ссылка на вакансию: {row[3]}\n')


        finally:
            conn.close()


db = DataBase('lukoil')
db.get_all_vacancies()