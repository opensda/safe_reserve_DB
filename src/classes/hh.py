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

        self.data_store = []
        for page in range(0, 3):
            self.content = get_data(page)
            self.data_store.extend(self.content['items'])
            print(f'Количество объектов равно {len(self.data_store)}')
        return self.data_store

