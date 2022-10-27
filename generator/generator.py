# !/usr/bin/env python
# coding: utf-8
from json import load
from models_question import Question
from models_user import User
from models_evaluation import Evaluation

instancia_evaluation = Evaluation(6)
print(instancia_evaluation.questions)
# instancia_evaluation.name = 'Prova1'
# instancia_evaluation.user = 3
# instancia_evaluation.questions = [1,2,3]
# instancia_evaluation.save()
# instancia_question = Question(2)
# print(instancia_question.question)
# instancia_question.question = "Qual o resultado de 7x7?"
# instancia_question.user = 1
# instancia_question.save()
# # instancia_question.update()
# # instancia_question.delete()

# instancia_user = User()
# instancia_user.username = ''
# instancia_user.save()
