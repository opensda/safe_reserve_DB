import json

class JSON_Saver:

    def __init__(self, filename):
        self.filename = filename


    def save_to_JSON(self, data):
        with open(f'{self.filename}.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


    # def save_to_txt(self, data):
    #     formatted_json = json.dumps(data, indent=4, ensure_ascii=False)



