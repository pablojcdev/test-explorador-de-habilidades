from modulo_1_question_answers import answers_area1_1
from modulo_1_question_answers import answers_area1_2
import sys 
from modulo_2 import *

def start(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer == "si":
            return Modulo_1()
        else:
            sys.exit("\n¡Nos vemos!\n")

score_area1_1 = ''

def area1_1(question):
    global score_area1_1
    score_area1_1 = 0
    for question in answers_area1_1:
        answer_area1_1 = input(question.prompt).strip().lower()
        if answer_area1_1 == question.answer:
            score_area1_1 += 1
    print("\nHas obtenido " + str(score_area1_1) + " puntos en el AREA I")

score_area1_2 = ''

def area1_2(question):
    global score_area1_2
    score_area1_2 = 0
    for question in answers_area1_2:
        answer_area1_2 = input(question.prompt).strip().lower()
        if answer_area1_2 == question.answer:
            score_area1_2 += 1
    print("\nHas obtenido " + str(score_area1_2) + " puntos en el AREA II")

best_area = ''

def best_area_final():
    global best_area
    best_area = max(score_area1_1, score_area1_2)
    if best_area == score_area1_1:
        print("Tu mejor aptitud se encuentra en el AREA I, con " + str(best_area) + " puntos")
    else:
        print("Tu mejor aptitud se encuentra en el AREA II, con " + str(best_area) + " puntos")

def recomendacion():
    global best_area
    if best_area == scoare_rea1_1:
        return print(recomendacion_area_1)
    else:
        return print(recomendacion_area_2)

def Modulo_1():
    print("\n\nMODULO 1\n\nMI ESTILO:\nIndica, en cada una de las Areas, cuál es tu \"Estilo de Hacer las Cosas en casa, en el trabajo o en el colegio\". Responde con un SI a aquellas afirmativas para tí.")
    print("\n\nAREA I:\nCuando hago las cosas en casa, en el trabajo o en el colegio SOY...")
    area1_1(answers_area1_1)
    print("\n\nAREA II:\nCuando hago las cosas en casa, en el trabajo o en el colegio SOY...")
    area1_2(answers_area1_2)
    print("\n")
    best_area_final()
    print("\nEsta es la recomendacion que mas se adecua a tus resultados:\n")
    recomendacion()

