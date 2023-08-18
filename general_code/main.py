import json

from src.classes.JSON_saver import JSON_Saver
from src.classes.hh import HH
from src.utils import load_data_hh_obj
from general_code.config import config
from general_code.create_db_script import create_database
from general_code.fill_the_table import fill_the_table



COMPANIES_VC = ['Лукойл', 'Роснефть', 'Сбербанк']
COMPANIES_DB = ['lukoil', 'rosneft', 'sberbank']

def main():
    for x in range(len(COMPANIES_VC)):
        hh = HH()
        parced_vacancies = hh.get_vacancies(COMPANIES_VC[x], 113)
        data_to_record = load_data_hh_obj(parced_vacancies)
        js_obj = JSON_Saver(f'Вакансии {COMPANIES_VC[x]}')
        js_obj.save_to_JSON(data_to_record)

        params = config()
        create_database(COMPANIES_DB[x], params)


        with open(f'../parced_vacancies/Вакансии {COMPANIES_VC[x]} в РФ.json', encoding='utf-8') as file:
            content = json.load(file)

        data_to_record = []
        for data in content:
            vac_name = data['name']
            url = data['url']
            pay = data['pay']
            employer = data['employer']
            data_to_record.append((employer, vac_name, pay, url))

        fill_the_table(COMPANIES_DB[x], data_to_record)


if __name__ == '__main__':
    main()




