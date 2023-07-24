from pprint import pprint

from src.classes.hh import HH


class Vacancy:
    All_vacancies = []
    # hh = HH()
    # data = hh.get_vacancies('Python')

    def __init__(self, name, pay, requirement, url=None):
        self.name = name
        self.url = url
        self.pay = pay
        self.requirement = requirement

        Vacancy.All_vacancies.append(self)
    def __str__(self):
        return f'{self.name}'
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.url}, {self.pay})"

    def to_json(self):
        return {
            "name": self.name,
            "url": self.url,
            "pay": self.pay,
            "requirement": self.requirement}

    def __gt__(self, other):
        return self.pay > other.pay








# for x in range(len(Vacancy.data)):
#     name = Vacancy.data[x]['name']
#     url = Vacancy.data[x]['alternate_url']
#     requirement = Vacancy.data[x]['snippet']['requirement']
#     if Vacancy.data[x]['salary'] == None:
#         pay = None
#     else:
#         salary_from = Vacancy.data[x]['salary']['from']
#         salary_to = Vacancy.data[x]['salary']['to']
#         pay = f'{salary_from} - {salary_to}'
#
#     vacancy = Vacancy(name, url, pay, requirement)


