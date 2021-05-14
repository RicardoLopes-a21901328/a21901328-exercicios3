import csv
import os
from matplotlib import pyplot as plt

def pede_pasta():
    nome = input("Caminho para a pasta:")
    return nome

def faz_calculos():
    nome = pede_pasta()
    list={}
    lista = os.listdir(nome)
    quantidade = 1
    quantidade2 = 0
    list1 = {}
    tamanhos={}
    quantidades={}
    for file in lista:
        if os.path.isfile(file):
            tamanho = os.path.getsize(file)
            nomes = os.path.basename(file).split(".")
            tamanhos['Tamanho'] = tamanho
            quantidades['Quantidade']=quantidade2+1
            list1[nomes[1]]= [quantidade,tamanhos]
    print(f"lista:{list1}")
    return list1

def guarda_resultados():
    with open('guarda_resultados.csv', 'w', newline='') as ficheiro:
        campos = ['Extensao', 'Quantidade','Tamanho[kByte]']
        writer = csv.DictWriter(ficheiro, fieldnames=campos)
        lista = faz_calculos()
        conter = 0
        for listar in lista:
            writer.writerow({'Extensao':lista.keys()[conter],'Quantidade':lista.values()[0].split(":")[1],'Tamanho[kByte]':lista.values()[1].split(":")[1]})

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
    lista_chaves = []
    conter=0
    key = {}
    key = ola.keys()
    for lista in key:
        lista_chaves[conter]=key[conter]
        conter=conter+1
    conter = 0
    for lista in ola:
        lista_valores = ola.values()[0].split(":")[1]
        conter = conter + 1
    titulo = 'Quantidade'
    faz_grafico_queijos(titulo, lista_chaves, lista_valores)
    conter=0
    for lista in ola:
        lista_valores = ola.values()[1].split(":")[1]
        conter = conter + 1
    titulo='Tamanho'
    faz_grafico_barras(titulo, lista_chaves, lista_valores)

