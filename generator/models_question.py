# !/usr/bin/env python
# coding: utf-8
from lib import write, read, get

class Question:
    file_name = 'questoes.json'
    def __init__(self, pk = None):
        # Declarando variaveis da instancia ===========
        self.pk = pk
        self.question = ''
        self.user = None
        
        if pk:
            questao = get(self.pk, self.file_name)
            if questao:
                self.question = questao['question']
        try:
            self.lista_questoes = read(self.file_name)
        except FileNotFoundError:
            self.lista_questoes = []

    def generate_pk(self):
        '''Define o numero pk de cada questao'''
        lista_pk = []
        if not self.lista_questoes:
            self.pk = 1
            return
        for questao in self.lista_questoes:
            lista_pk.append(questao["pk"])   
        self.pk = max(lista_pk) + 1


    def save(self):
        '''Salva objeto questao'''
        if not self.user:
            raise Exception('self.user is not defined!')
        self.generate_pk()    
        dict_questao = {} 
        dict_questao['pk'] = self.pk
        dict_questao['question'] = self.question
        dict_questao['user'] = self.user
        self.lista_questoes.append(dict_questao)   
        write(self.lista_questoes, self.file_name)
        print(f'Question pk {self.pk} adicionado')

    def update(self):
        for questao in self.lista_questoes:
            if self.pk == questao["pk"]:
                questao['question'] = self.question
        write(self.lista_questoes, self.file_name)
    
    def delete(self):
        new_questions = []
        for questao in self.lista_questoes:
            if self.pk != questao["pk"]:
                new_questions.append(questao)
        write(new_questions, self.file_name)

