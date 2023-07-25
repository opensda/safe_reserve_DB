import requests

from src.classes.hh import JobPlatform


class SuperJob(JobPlatform):
    """
       Класс позволяет собирать информацию о вакансиях с платформы superjob.ru.ru
    """

    def __init__(self, name='superjob'):
        self.name = name

    def get_vacancies(self, key_word: str, town: str):
        """
        Получаем вакансии с superjob.ru с заданными параметрами
        :param key_word: ключевое слово для поискового запроса
        :param town: название города
        :return: список словарей с вакансиями
        """
        api_key = 'v3.r.137697608.f7e337a7ba658714046240826f8b669cf769b285.aa25b4c1fa18e394fa2aa5b8ee94fb1baef25811'

        def get_data(page=0):
            """
            Внутрення функция - парсим данные о вакансиях постранично
            :param page: номер страницы
            """

            # Делаем get запрос с необходимыми параметрами
            # и получаем данные в json формате


            # В заголовке передаем полученный при регистрации API-ключ
            headers = {
                'X-Api-App-Id': api_key}


            params = {'keyword': key_word,
                      'town': town,
                      'page': page,
                      'count': 100,
                      'archive': False,
                      }

            response = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers, params=params)
            response_json = response.json()
            return response_json

        data_store = []
        for page in range(0, 5):
            content = get_data(page)
            data_store.append(content)
            print(f'Загружаются данные с superjob.ru: 100 вакансий загружено')


        return data_store

