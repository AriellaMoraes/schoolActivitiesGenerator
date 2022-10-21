from lib import write, read

class Question:
    def __init__(self):
        pk = None
        print('Questão iniciada')

    def save (self):
        '''Função que escreve em arquivo json'''
        write({'questao': 0})

    def load (self):
        print(read())
       