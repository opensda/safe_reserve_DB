from abc import ABC, abstractmethod
from pprint import pprint

import requests


class JobPlatform(ABC):

    @abstractmethod
    def __init__(self):
        pass



class HH(JobPlatform):

    def __init__(self):
        pass

    def get_vacancies(self, vacancy):
        def get_data(page=0):
            self.params = {
            'text': vacancy,
            'area': 1,
            'pages': page,
            'per_page': 2}
            self.response = requests.get('https://api.hh.ru/vacancies', self.params)
            self.response_json = self.response.json()
            return self.response_json

        for page in range(0, 2):
            self.data_store = []
            self.content = get_data(page)
            self.data_store.append(self.content)
        return self.data_store

hh = HH()

# pprint(hh.get_vacancies('Python'))

data = hh.get_vacancies('Python')


# pprint(data)
# for x in data:
#     print(x)

# print(len(data[0]['items']))

# for x in data:
#     name = x['items'][1]['name']
#     print(name)
#
for x in range(len(data[0]['items'])):
    name = data[0]['items'][x]['name']
    url = data[0]['items'][x]['alternate_url']
    requirement = data[0]['items'][x]['snippet']['requirement']
    if data[0]['items'][x]['salary'] == None:
        total_salary = None
    else:
        salary_from = data[0]['items'][x]['salary']['from']
        salary_to = data[0]['items'][x]['salary']['to']
        total_salary = f'{salary_from} - {salary_to}'
    # print(name, url, total_salary)





