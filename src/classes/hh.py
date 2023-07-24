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

    def get_vacancies(self, vacancy, area_id):
        def get_data(page=0):
            self.params = {
            'text': vacancy,
            'area': area_id,
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
            print(f'Количество объектов равно {len(self.data_store)} (hh.ru)')
        return self.data_store

    def get_clarified_vacancies(self, vacancies, key_word):
        clarified_vacancies = []
        for vac in vacancies:
            if key_word in vac['name'] or key_word.lower() in vac['name']:
                clarified_vacancies.append(vac)
            elif vac['snippet']['requirement'] == None:
                continue
            elif key_word in vac['snippet']['requirement'] or key_word.lower() in vac['snippet']['requirement']:
                clarified_vacancies.append(vac)
            elif vac['employer']['name'] == None:
                continue
            elif key_word in vac['employer']['name'] or key_word.lower() in vac['employer']['name']:
                clarified_vacancies.append(vac)

        return clarified_vacancies



