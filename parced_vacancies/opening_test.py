import json

# with open ('Вакансии Лукойл в РФ в РФ.json', encoding='utf-8') as file:
#     content = json.load(file)

COMPANIES_VC = ['Лукойл', 'Роснефть', 'Сбербанк']

for x in range(len(COMPANIES_VC)):
    with open(f'Вакансии {COMPANIES_VC[x]} в РФ.json', encoding='utf-8') as file:
        content = json.load(file)
        print(content)
