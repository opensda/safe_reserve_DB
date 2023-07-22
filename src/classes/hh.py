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

    def get_data(self, vacancy):
        def get_data(page=0):
            self.params = {
            'text': vacancy,
            'area': 1,
            'pages': 20,
            'page': page,
            'per_page': 100}
            self.response = requests.get('https://api.hh.ru/vacancies', self.params)
            self.response_json = self.response.json()
            return self.response_json

        self.data_store = []
        for page in range(0, 2):
            self.content = get_data(page)
            self.data_store.extend(self.content['items'])
            print(f'Количество объектов равно {len(self.data_store)}')
        return self.data_store

    def get_clear_vacancies(self, vacancies, key_word):
        clear_vacancies = []
        for vac in vacancies:
            if key_word in vac['name'] or key_word.lower() in vac['name']:
                clear_vacancies.append(vac)
            elif vac['snippet']['requirement'] == None:
                continue
            elif key_word in vac['snippet']['requirement'] or key_word.lower() in vac['snippet']['requirement']:
                clear_vacancies.append(vac)
            elif vac['employer']['name'] == None:
                continue
            elif key_word in vac['employer']['name'] or key_word.lower() in vac['employer']['name']:
                clear_vacancies.append(vac)

        return clear_vacancies



