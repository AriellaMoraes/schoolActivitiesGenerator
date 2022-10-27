from lib import write, read, get
from models_question import Question

class Evaluation:
    file_name = 'evaluation.json'
    def __init__(self, pk = None):
        self.pk = pk
        self.name = ''
        self.user = None
        self.questions = []
        if pk:
            evaluation = get(self.pk, self.file_name)
            if evaluation:
                self.name = evaluation['name']
                self.questions = evaluation['questions']
                self.user = evaluation['user']
        try:
            self.lista_evaluation = read(self.file_name)
        except FileNotFoundError:
            self.lista_evaluation = []

    def save(self):
        '''Salva nome do usuario'''
        if not self.user:
            raise Exception('self.user is not defined!')
        self.generate_pk()    
        dict_evaluation = {} 
        dict_evaluation['pk'] = self.pk
        dict_evaluation['name'] = self.name
        dict_evaluation['user'] = self.user
        dict_evaluation['questions'] = self.questions
        self.lista_evaluation.append(dict_evaluation)   
        write(self.lista_evaluation, self.file_name)
        print(f'Evaluation pk {self.pk} adicionado')

    def generate_pk(self):
        '''Define o numero pk de cada avaliação'''
        lista_pk = []
        if not self.lista_evaluation:
            self.pk = 1
            return
        for evaluation in self.lista_evaluation:
            lista_pk.append(evaluation["pk"])   
        self.pk = max(lista_pk) + 1
                
    def update(self):
        for evaluation in self.lista_evaluations:
            if self.pk == evaluation["pk"]:
                evaluation['name'] = self.name
        write(self.lista_evaluation, self.file_name)
            
    def delete(self):
        new_evaluation = []
        for evaluation in self.lista_evaluation:
            if self.pk != evaluation["pk"]:
                new_evaluation.append(evaluation)
        write(new_evaluation, self.file_name)
