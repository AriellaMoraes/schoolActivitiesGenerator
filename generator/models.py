from argparse import MetavarTypeHelpFormatter
from multiprocessing.connection import answer_challenge
from lib import write, read

class Question:
    #pergunta, alternativas, resposta correta, materia, tema, ativo
    def __init__(self):
        self.pk = None
        self.question = ''
        self.alternatives = []
        self.right_answer = ''
        self.matter = ''
        self.theme = '' 
        self.active = True
        print('Questão iniciada')

    def save (self):
        '''Função que escreve em arquivo json'''
        dados = self.__dict__
        write(dados)

    def load (self):
        dados  = read()
        self.pk = dados['pk']
        self.question = dados['question']
        self.alternatives = dados['alternatives']
        self.right_answer = dados['right_answer']
        self.matter = dados['matter']
        self.theme = dados['theme']
        self.active = dados['active']
