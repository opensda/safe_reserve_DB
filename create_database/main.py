from config import config
from create_db_script import create_database
# def main():
#     params = config()
#     create_database('Роснефть', params)
#
# if __name__ == '__main__':
#     main()


COMPANIES_DB = ['lukoil', 'rosneft', 'sberbank']

for x in range(len(COMPANIES_DB)):

    params = config()
    create_database(COMPANIES_DB[x], params)


