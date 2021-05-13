import json
import os.path

def calcular_lines(nome):
    conter = 0
    if (os.path.isfile(nome)):
        f = open(nome, 'r')
        for line in f:
            conter = conter+1
        print(conter)
        f.close()
    else:
        print("nao existe")

def calcular_carateres(nome):
    conter = 0
    if (os.path.isfile(nome)):
        f = open(nome, 'r')
        for line in f:
            conter = conter + len(line)
        print(f"total de caracteres: {conter}")
        f.close()
    else:
        print("nao existe")


def calcular_palavra_cumprida(nome):
    conter = 0
    numero_letras = 0
    palavra = ""
    if (os.path.isfile(nome)):
        f = open(nome, 'r')
        for line in f:
            ola = line.split(" ")
            for palavras in ola:
                if numero_letras <= len(palavras):
                    numero_letras = len(palavras)
                    palavra = palavras
        print(f"Maior palavra: {palavra}")
        f.close()
    else:
        print("nao existe")

def calcular_ocurrencia_de_letras(nome):
    dicionario = {}
    contara = 0
    contarb = 0
    contarc = 0
    contard = 0
    contare = 0
    contarf = 0
    contarg = 0
    contarh = 0
    contari = 0
    contark = 0
    contarl = 0
    contarm = 0
    contarn = 0
    contaro = 0
    contarp = 0
    contarq = 0
    contarr = 0
    contars = 0
    contart = 0
    contaru = 0
    contarv = 0
    contarw = 0
    contary = 0
    contarx = 0
    contarz = 0
    if (os.path.isfile(nome)):
        f = open(nome, 'r')
        for linha in f:
            contara = linha.count("a") + linha.count("A") + contara
            contarb = linha.count("b") + linha.count("B") + contarb
            contarc = linha.count("c") + linha.count("C") + contarc
            contard = linha.count("d") + linha.count("D") + contard
            contare = linha.count("e") + linha.count("E") + contare
            contarf = linha.count("f") + linha.count("F") + contarf
            contarg = linha.count("g") + linha.count("G") + contarg
            contarh = linha.count("h") + linha.count("H") + contarh
            contari = linha.count("i") + linha.count("I") + contari
            contark = linha.count("k") + linha.count("K") + contark
            contarl = linha.count("l") + linha.count("L") + contarl
            contarm = linha.count("m") + linha.count("M") + contarm
            contarn = linha.count("n") + linha.count("N") + contarn
            contaro = linha.count("o") + linha.count("O") + contaro
            contarp = linha.count("p") + linha.count("P") + contarp
            contarq = linha.count("q") + linha.count("Q") + contarq
            contarr = linha.count("R") + linha.count("r") + contarr
            contars = linha.count("s") + linha.count("S") + contars
            contart = linha.count("t") + linha.count("T") + contart
            contaru = linha.count("u") + linha.count("u") + contaru
            contarv = linha.count("v") + linha.count("V") + contarv
            contarw = linha.count("w") + linha.count("W") + contarw
            contary = linha.count("y") + linha.count("Y") + contary
            contarx = linha.count("x") + linha.count("X") + contarx
            contarz = linha.count("z") + linha.count("Z") + contarz
        f.close()
    else:
        print("nao existe")
    dicionario["a"] = contara
    dicionario["b"] = contarb
    dicionario["c"] = contarc
    dicionario["d"] = contard
    dicionario["e"] = contare
    dicionario["f"] = contarf
    dicionario["g"] = contarg
    dicionario["h"] = contarh
    dicionario["i"] = contari
    dicionario["k"] = contark
    dicionario["l"] = contarl
    dicionario["m"] = contarm
    dicionario["n"] = contarn
    dicionario["o"] = contaro
    dicionario["p"] = contarp
    dicionario["q"] = contarq
    dicionario["r"] = contarr
    dicionario["s"] = contars
    dicionario["t"] = contart
    dicionario["u"] = contaru
    dicionario["v"] = contarv
    dicionario["w"] = contarw
    dicionario["y"] = contary
    dicionario["x"] = contarx
    dicionario["z"] = contarz
    print(dicionario)