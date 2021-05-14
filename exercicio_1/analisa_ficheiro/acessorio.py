import json
import os.path

def verificar(nome):
    veri = False
    while veri==False:
        if(os.path.isfile(nome)):
            print(f"{nome}")
            veri=True
        else:
            nome = input("Qual o nome do ficheiro pretendido ")
    return veri
def por_json(nome):
    if(nome.find(".")==0):
        print(f"{nome}.json")
        with open(f'{nome}.txt', 'w') as json_file:
            json.dump("dados", json_file)
    else:
        nome_perar = nome.split('.')
        print(f"{nome_perar[0]}.json ")
        with open(f'{nome_perar[0]}.json', 'w') as json_file:
            json.dump("ola", json_file, indent= 4)