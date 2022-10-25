import json

    
database = 'generator/database/'

def write(saida):
    with open(database + 'questoes.json', 'a', encoding='utf-8') as file:
        json.dump(saida, file, indent=4)

def read():
    with open(database + 'questoes.json', 'r') as file:
        data = json.load(file)
        return data