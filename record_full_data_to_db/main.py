from record_full_data_to_db import data_to_record

from create_database.fill_the_table import fill_the_table

db_name = 'gazprom'
table_name = 'gazprom_vacancies'
# data_for_record = [('Роснефть-Pоснефть', 'Директор Сечина', 77777, 'rosneft-путуин.ru')]


fill_the_table(db_name, table_name, data_to_record)

