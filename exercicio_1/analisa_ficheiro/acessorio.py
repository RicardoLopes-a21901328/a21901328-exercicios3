import json
import os.path

def verificar():
    veri = False
    while veri==False:
        site = input("Qual o nome do ficheiro pretendido ")
        if(os.path.isfile(site)):
            print(f"{site}")
            veri=True
        else:
            print("Não existe tente outra vez ")
    return veri
def por_json(nome):
    if(nome.find(".")==0):
        print(f"{nome}.json")
        with open(f'{nome}.txt', 'w') as json_file:
            json.dump("dados", json_file)
    else:
        nome_perar = nome.split('.')
        print(f"{nome_perar[0]}.json ")
        with open(f'{nome}', 'w') as json_file:
            json.dump("ola", json_file)