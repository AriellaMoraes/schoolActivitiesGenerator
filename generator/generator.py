# !/usr/bin/env python
# coding: utf-8
from json import load
from models import Question

questao2 = Question()
questao2.load()
questao2.save()

questao = Question()
questao.question = 'Quanto é 2+2?'
questao.pk = 1
questao.alternatives = {'a': 5, 'b': 3, 'c': 4, 'd': 2 }
questao.right_answer = 'c'
questao.matter = 'portuguese'
questao.theme = 'nouns'

questao.save()