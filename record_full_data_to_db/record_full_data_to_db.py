import json

with open('Вакансии Газпром в РФ.json', encoding='utf-8') as file:
    content = json.load(file)

data_to_record = []
for data in content:
    vac_name = data['name']
    url = data['url']
    pay = data['pay']
    employer = data['employer']
    data_to_record.append((employer, vac_name, pay, url))




