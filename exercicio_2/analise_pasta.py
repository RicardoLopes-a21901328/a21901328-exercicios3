import csv
import os
from matplotlib import pyplot as plt

def pede_pasta():
    nome = input("Caminho para a pasta:")
    return nome

def faz_calculos():
    nome = pede_pasta()
    lista = os.listdir(nome)
    quantidade = 1
    quantidade2 = 0
    list1 = {}
    tamanhos={}
    quantidades={}
    for file in lista:
        tamanho = (os.path.getsize(os.path.join(file,nome))/1024)
        nomes = os.path.basename(file).split(".")
        tamanhos['Tamanho'] = tamanho
        quantidades['Quantidade']=quantidade2+1
        list1[nomes[1]]= [quantidades,tamanhos]
    print(f"lista:{list1}")
    return list1

def guarda_resultados():
    with open('guarda_resultados.csv', 'w', newline='') as ficheiro:
        lista = {}
        lista = faz_calculos()
        campos = ['Extensao', 'Quantidade','Tamanho[kByte]']
        writer = csv.DictWriter(ficheiro, fieldnames=campos)
        conter = 0
        listak=[]
        listak = lista.keys()
        for listar in listak:
            writer.writerow({'Extensao':listak,'Quantidade':1,'Tamanho[kByte]':1})

def faz_grafico_barras():
    def faz_grafico_queijos(titulo, lista_chaves, lista_valores):
        plt.pie(lista_valores, labels=lista_chaves, autopct='%1.0f%%')
        plt.title(titulo)
        plt.show()

    def faz_grafico_barras(titulo, lista_chaves, lista_valores):
        plt.bar(lista_chaves, lista_valores)
        plt.title(titulo)
        plt.show()

    ola = faz_calculos()
    lista_chaves = [2]
    lista_valores = [2]
    conter=0
    key = {}
    key = ola.keys()
    for lista in key:
        lista_chaves[conter] = lista
        conter=conter+1
    conter = 0
    for lista in ola:
        lista_valores[conter] = lista_chaves.count(lista)
        conter = conter + 1
    titulo = 'Quantidade'
    faz_grafico_queijos(titulo, lista_chaves, lista_valores)
    conter=0
    lista_soma=[2]
    for lista in ola:
        lista_soma[conter] = conter + conter
        conter = conter + 1
    titulo='Tamanho'
    faz_grafico_barras(titulo, lista_chaves, lista_valores)

