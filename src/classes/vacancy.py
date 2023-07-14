from hh import HH


class Vacancy:
    All_vacancies = []

    def __init__(self, name=None, url=None, pay=None, requirement=None):
        hh = HH()
        data = hh.get_vacancies('Python')
        for x in range(len(data[0]['items'])):
            self.name = data[0]['items'][x]['name']
            self.url = data[0]['items'][x]['alternate_url']
            self.requirement = data[0]['items'][x]['snippet']['requirement']
            if data[0]['items'][x]['salary'] == None:
                self.pay = None
            else:
                salary_from = data[0]['items'][x]['salary']['from']
                salary_to = data[0]['items'][x]['salary']['to']
                self.pay = f'{salary_from} - {salary_to}'
            Vacancy.All_vacancies.append(self)

    def __str__(self):
        return f'{Vacancy.All_vacancies}'
        # return f'{self.name}, {self.url}, {self.pay}, {self.requirement}'


vacancy = Vacancy()
print(str(Vacancy.All_vacancies[0].name))
print(str(Vacancy.All_vacancies[1].name))