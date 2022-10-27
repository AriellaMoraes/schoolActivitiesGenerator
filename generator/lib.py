import json

    
database = 'generator/database/'

def write(saida, file_name):
    '''Escrever em um arquivo json'''
    with open(database + file_name, 'w', encoding='utf-8') as file:
        json.dump(saida, file, indent=4)

def read(file_name):
    '''Ler um arquivo json'''
    with open(database + file_name, 'r') as file:
        data = json.load(file)
        return data

def get(pk, file_name):
    '''Busca questoes no arquivo json por numero de pk'''
    try:
        lista_questoes = read(file_name)
    except FileNotFoundError:
        return None
    for questao in lista_questoes:
        if pk == questao["pk"]:
            return questao
    return None  
