import analisa_ficheiro
import json

def main():
    frase = input('nome do fixeiro: ')
    analisa_ficheiro.acessorio.verificar(frase)
    analisa_ficheiro.acessorio.por_json(frase)
    analisa_ficheiro.calculos.calcular_lines(frase)
    analisa_ficheiro.calculos.calcular_carateres(frase)
    analisa_ficheiro.calculos.calcular_palavra_cumprida(frase)
    analisa_ficheiro.calculos.calcular_ocurrencia_de_letras(frase)

if __name__ == '__main__':
    main()