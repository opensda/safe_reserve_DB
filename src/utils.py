import json

from src.classes.vacancy import Vacancy


def get_sorted_by_pay(filename: str, sorted_num: int):
    """
    Сортируем вакансии по ЗП
    :param filename: имя json файла с вакансиями
    :param sorted_num: количество отсортированных вакансий
    :return: список словарей, отсортированный по ЗП
    """
    with open(filename, encoding='utf-8') as file:
        content = json.load(file)
    vac_with_pay = []
    for vac in content:
        if vac.get('pay') == None:
            continue
        elif vac.get('pay') == 0:
            continue
        else:
            vac_with_pay.append(vac)
    def get_pay(vacancy):
        return vacancy["pay"]

    vac_srt_by_pay = sorted(vac_with_pay, key=get_pay)
    vac_srt_by_pay = vac_srt_by_pay[:sorted_num]

    return vac_srt_by_pay


def load_data_hh_obj(clear_data):
    """
    Заагружаем данные о вакансиях с hh.ru в объекты класса Vacanvy
    :param clear_data: список словарей с вакансиями
    :return: список словарей с атрибутами объекта класса Vacancy
    """
    data_js_obj = []
    for x in range(len(clear_data)):
        name = clear_data[x]['name']
        url = clear_data[x]['alternate_url']
        requirement = clear_data[x]['snippet']['requirement']
        employer = clear_data[x]['employer']['name']
        if clear_data[x]['salary'] == None:
            pay = None
        else:
            pay = clear_data[x]['salary']['from']

        vacancy = Vacancy(name, pay, requirement, employer, url)
        data_js_obj.append(vacancy.to_json())

    return data_js_obj


def load_data_sj_obj(data):
    """
    Заагружаем данные о вакансиях с superjob.ru.ru в объекты класса Vacanvy
    :param clear_data: список словарей с вакансиями
    :return: список словарей с атрибутами объекта класса Vacancy
    """
    data_js_obj = []
    for x in range(len(data)):
        for i in range(len(data[x]['objects'])):
            name = data[x]['objects'][i]['profession']
            url = data[x]['objects'][i]['link']
            pay = data[x]['objects'][i]['payment_from']
            requirement = data[x]['objects'][i]['candidat']

            vacancy = Vacancy(name, pay, requirement, url)
            data_js_obj.append(vacancy.to_json())

    return data_js_obj
