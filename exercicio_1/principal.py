import analisa_ficheiro
import json

def main():
    ola = analisa_ficheiro.acessorio.verificar()
    frase = input('nome do fixeiro: ')
    analisa_ficheiro.acessorio.por_json(frase)
    analisa_ficheiro.calculos.calcular_lines(frase)


if __name__ == '__main__':
    main()