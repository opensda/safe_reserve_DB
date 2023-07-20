from pprint import pprint

from src.classes.hh import HH
from src.classes.vacancy import Vacancy
from src.classes.JSON_saver import JSON_Saver

import json



vacancy = "Java"
payment = 500
currency = 'USD'
requirement = 'Опыт работы от 3-х лет'

# hh = HH()
#
# vacancies = hh.get_vacancies(vacancy)
#
# file = JSON_Saver('Вакансии по Java')
# file.save_to_JSON(vacancies)

with open('Вакансии по Java.json', encoding='utf-8') as file:
    data = json.load(file)






"""
Сортировка данных по ЗП. Оставляем только те вакансии, в которых есть ЗП
и указана ЗП "от"
"""

data_pay_must_have = []
for vacancy in data:
    if vacancy.get('salary') == None:
        continue
    elif vacancy['salary'].get('from') == None:
        continue
    else:
        data_pay_must_have.append(vacancy)


# print(len(data_pay_must_have))


"""
Сортируем данные по ЗП
"""
def get_pay(x):
    return x["salary"]['from']

srtd_by_pay = sorted(data_pay_must_have, key=get_pay)

# for x in srtd_by_pay:
#     print(x['salary'])


just_in_request = []
for pay in data_pay_must_have:
    if pay['salary']["currency"] == currency:
        if pay['salary']['gross'] == True:
            if pay['salary']['from'] >= payment:
                just_in_request.append(pay)
        elif pay['salary']['gross'] == False:
            if pay['salary']['from'] >= payment / 0.87:
                just_in_request.append(pay)

    elif pay['salary']["currency"] == currency:
        if pay['salary']['gross'] == True:
            if pay['salary']['from'] >= payment:
                just_in_request.append(pay)
        elif pay['salary']['gross'] == False:
            if pay['salary']['from'] >= payment / 0.87:
                just_in_request.append(pay)



print(len(just_in_request))

for x in just_in_request:
    print(x['salary'])

"""
 Сортировка данных в зависимости от опыта
"""
# vac_srt_by_exp = []
# for vacancy in data:
#     if vacancy["experience"]["name"] == 'От 3 до 6 лет'\
#             or vacancy["experience"]["name"] == "От 1 года до 3 лет":
#         vac_srt_by_exp.append(vacancy)
























"""
Ниже код для записи минимальных данных в экземпляры класса Vacancy, которые
потом будут сохранены в список All_vacancies
"""

# for x in range(len(vacancies)):
#     name = vacancies[x]['name']
#     url = vacancies[x]['alternate_url']
#     requirement = vacancies[x]['snippet']['requirement']
#     if vacancies[x]['salary'] == None:
#         pay = None
#     else:
#         salary_from = vacancies[x]['salary']['from']
#         salary_to = vacancies[x]['salary']['to']
#         pay = f'{salary_from} - {salary_to}'
#
#     vacancy = Vacancy(name, url, requirement, pay)
#
# pprint(Vacancy.All_vacancies)
# print()
# print()
#
# for vacancy1 in Vacancy.All_vacancies:
#     print(vacancy1)





