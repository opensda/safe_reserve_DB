from pprint import pprint

from src.classes.hh import HH
from src.classes.vacancy import Vacancy
from src.classes.JSON_saver import JSON_Saver



vacancy = "Java"
pay = 50000
requirement = 'Опыт работы от 3-х лет'

hh = HH()

vacancies = hh.get_vacancies(vacancy)

file = JSON_Saver('Вакансии')



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





