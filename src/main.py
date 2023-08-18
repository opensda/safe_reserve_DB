from src.classes.hh import HH
from src.classes.superjob import SuperJob

from src.classes.JSON_saver import JSON_Saver

from src.utils import load_data_hh_obj, get_sorted_by_pay, load_data_sj_obj



# hh = HH()
#
# gazprom_vacancies = hh.get_vacancies('Лукойл', 113)
#
#
# data_to_record = load_data_hh_obj(gazprom_vacancies)
#
# js_obj = JSON_Saver('Вакансии Лукойл РФ_1')
#
# js_obj.save_to_JSON(data_to_record)

"""ТЕСТИРЕМ ЗАПИСЬ ВАКАНСИЙ СРАЗУ НЕСКОЛЬКИХ КОМПАНИЙ В JSON"""

companies = ['Лукойл', 'Роснефть', 'Сбербанк']

for x in range(len(companies)):
    hh = HH()
    parced_vacancies = hh.get_vacancies(companies[x], 113)
    data_to_record = load_data_hh_obj(parced_vacancies)
    js_obj = JSON_Saver(f'Вакансии {companies[x]} РФ')
    js_obj.save_to_JSON(data_to_record)

# if source_choice == 'hh':
#         hh = HH()
#
#         # получаем вакансии по ключевому слову и id города
#         vacancies = hh.get_vacancies(key_word,hh_city_id)
#
#         # Преобразуем данные для записи в json файл
#         data_to_record = load_data_hh_obj(vacancies)
#
#
#         js_obj = JSON_Saver(filename)
#
#         # Записываем данные в json файл
#         js_obj.save_to_JSON(data_to_record)
#
#         # Получаем список отсортированных по зарплате вакансий
#         sorted_vac = get_sorted_by_pay(f'{filename}.json', sorted_num)





































































































# if __name__ == '__main__':
#
#     # Счетчик вакансий, которые выводятся в консоль
#     VACANCIES_COUNTER = 0
#
#     user_platfom_choice = int(input('С какой платорфмы Вы хотите получить '
#                                     'вакансии ?\n'
#                                     'нажмите 1 - получите вакансии с hh.ru\n'
#                                     'нажмите 2 - получите вакансии с superjob.ru\n'
#                                     '-->  '))
#     if user_platfom_choice == 1:
#         source_choice = 'hh'
#     elif user_platfom_choice == 2:
#         source_choice = 'sj'
#
#     user_city_choice = int(input('В каком городе необходимо найти '
#                                     'вакансии ?\n'
#                                     'нажмите 1 - Москва\n'
#                                     'нажмите 2 - Санкт - Петербург\n'
#                                  '-->  '))
#     if user_city_choice == 1 and source_choice == 'hh':
#         hh_city_id = 1
#         chosen_city = 'Москва'
#     elif user_city_choice == 2 and source_choice == 'hh':
#         hh_city_id = 2
#         chosen_city = 'Санкт-Петербург'
#     elif user_city_choice == 1 and source_choice == 'sj':
#         chosen_city = 'Москва'
#     elif user_city_choice == 2 and source_choice == 'sj':
#         chosen_city = 'Санкт-Петербург'
#
#     key_word = input('Введите название вакансии для поиска: --> ')
#
#     sorted_num = int(input('Вам будут представлены вакансии, отсортированные по ЗП,'
#                            'сколько вакансий Вам показать?\n'
#                            '--> '))
#
#     filename = f"Вакансии {key_word} в г.{chosen_city} с {source_choice}"
#
#     if source_choice == 'hh':
#         hh = HH()
#
#         # получаем вакансии по ключевому слову и id города
#         vacancies = hh.get_vacancies(key_word,hh_city_id)
#
#         # Преобразуем данные для записи в json файл
#         data_to_record = load_data_hh_obj(vacancies)
#
#
#         js_obj = JSON_Saver(filename)
#
#         # Записываем данные в json файл
#         js_obj.save_to_JSON(data_to_record)
#
#         # Получаем список отсортированных по зарплате вакансий
#         sorted_vac = get_sorted_by_pay(f'{filename}.json', sorted_num)
#
#
#
#     elif source_choice == 'sj':
#         superjob = SuperJob()
#
#         # получаем вакансии по ключевому слову и названию города
#         vacancies = superjob.get_vacancies(key_word, chosen_city)
#
#         # Далее аналогично
#
#         data_to_record = load_data_sj_obj(vacancies)
#         js_obj = JSON_Saver(filename)
#         js_obj.save_to_JSON(data_to_record)
#         sorted_vac = get_sorted_by_pay(f'{filename}.json', sorted_num)
#
#
#     # Выводим пользователю информацию в соответствии с запросом
#
#     for vac in sorted_vac:
#         VACANCIES_COUNTER += 1
#         print(f'Позиция вакансии в поиске: {VACANCIES_COUNTER}')
#         print(f'Название вакансии: {vac["name"]}')
#         print(f'Ссылка на вакансию: {vac["url"]}')
#         print(f'Заработная плата: {vac["pay"]}')
#         print(f'Требования: {vac["requirement"]}\n\n')
#
#
#     # Если пользователь ввел некорректные данные - просим перепроверить корректность введенных данных
#
#     if len(sorted_vac) == 0:
#         print('Если тут не появились данные о вакансиях, то проверьте корректность введенного запроса')








