# !/usr/bin/env python
# coding: utf-8
from argparse import MetavarTypeHelpFormatter
from multiprocessing.connection import answer_challenge
from unicodedata import name
from lib import write, read, get

class Question:
    file_name = 'questoes2.json'
    #pergunta, alternativas, resposta correta, materia, tema, ativo
    def __init__(self, pk = None):
        self.pk = pk
        self.question = ''
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
        self.generate_pk()    
        dict_questao = {} 
        dict_questao['pk'] = self.pk
        dict_questao['question'] = self.question
        self.lista_questoes.append(dict_questao)   
        write(self.lista_questoes, self.file_name)
        print(f'Pk {self.pk} adicionado')

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

class User:
    file_name = 'user.json'
    def __init__(self, pk = None):
        self.pk = pk
        self.username = ''
        if pk:
            name = get(self.pk, self.file_name)
            if name:
                self.username = name['username']
        try:
            self.lista_users = read(self.file_name)
        except FileNotFoundError:
            self.lista_users = []

    def save(self):
        '''Salva nome do usuario'''
        self.generate_pk()    
        dict_user = {} 
        dict_user['pk'] = self.pk
        dict_user['username'] = self.username
        self.lista_users.append(dict_user)   
        write(self.lista_users, self.file_name)
        print(f'Pk {self.pk} adicionado')

    def generate_pk(self):
        '''Define o numero pk de cada usuario'''
        lista_pk = []
        if not self.lista_users:
            self.pk = 1
            return
        for user in self.lista_users:
            lista_pk.append(user["pk"])   
        self.pk = max(lista_pk) + 1
        
    def update(self):
        for user in self.lista_users:
            if self.pk == user["pk"]:
                user['username'] = self.username
        write(self.lista_users, self.file_name)
    
    def delete(self):
        new_users = []
        for user in self.lista_users:
            if self.pk != user["pk"]:
                new_users.append(user)
        write(new_users, self.file_name)






