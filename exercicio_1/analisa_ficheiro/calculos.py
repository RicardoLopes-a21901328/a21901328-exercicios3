import json
import os.path

def calcular_lines(nome):
    conter = 0
    if (os.path.isfile(nome)):
        f = open(nome, 'r')
        for line in f:
            conter = conter+1
        print(conter)
    else:
        print("nao existe")