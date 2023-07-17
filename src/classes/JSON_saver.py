import json

class JSON_Saver:

    def __init__(self, filename):
        self.filename = filename


    def save_to_JSON(self, data):
        with open(f'{self.filename}.json', 'w') as file:
            sep_data = data[0]
            json.dump(sep_data, file, indent=2, ensure_ascii=False)



