import json


def get_vacancy_by_pay(vacancies: list, payment: int, currency='RUR'):
    """
    Сортирует вакансии по ЗП
    :param vacancies: список словарей с вакансиями
    :param payment: ЗП gross "от"
    :param currency: валюта
    :return: список отсортированных по ЗП вакансий
    """

    # Будем сохранять вакансии, где указана ЗП
    vac_with_pay = []

    # Будем сохранять отсортированные по ЗП вакансии
    vac_srt_by_pay = []

    # Если указана ЗП и есть нижняя "вилка", сохраняем вакансию

    for vacancy in vacancies:
        if vacancy.get('salary') == None:
            continue
        elif vacancy['salary'].get('from') == None:
            continue
        else:
            vac_with_pay.append(vacancy)

    # Сохраняем вакансии, в зависимости от выбранной валюты
    # и уровня нижней "вилки" ЗП

    for pay in vac_with_pay:
        if pay['salary']["currency"] == currency:
            if pay['salary']['gross'] == True:
                if pay['salary']['from'] >= payment:
                    vac_srt_by_pay.append(pay)

            # Если ЗП указана "net", то приводим его к значению "gross"
            elif pay['salary']['gross'] == False:
                if pay['salary']['from'] >= payment / 0.87:
                    vac_srt_by_pay.append(pay)

    # Сортируем по значению ЗП
    def get_pay(item):
        return item["salary"]['from']

    vac_srt_by_pay = sorted(vac_srt_by_pay, key=get_pay)

    return vac_srt_by_pay


def get_vac_by_exp(vacancies, experience):
    """
    Сортирует вакансии по опыту работы
    :param vacancies: список словарей с вакансиями
    :param experience: опыт работы
    Список допустимых значений для experience:
    # "noExperience" - нет опыта
    # "between1And3" - от 1 до 3 лет опыта
    # "between3And6" - от 3 до 6 лет опыта
    # "moreThan6" - более 6 лет опыта
    :return: список отсортированных по опыту вакансий
    """
    vac_srt_by_exp = []
    for vacancy in vacancies:
        if vacancy['experience']["id"] == experience:
            vac_srt_by_exp.append(vacancy)

    return vac_srt_by_exp


