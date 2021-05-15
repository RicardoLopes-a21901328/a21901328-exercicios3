import  os

def pede_pasta():
    nome = input("Caminho para a pasta:")
    return nome

def calcula_tamanho_pasta(pasta):
    soma = 0
    pastas = os.listdir(pasta)
    for ficheiro in pastas:
        ficheiros = os.path.join(pasta,ficheiro)
        if os.path.isfile(ficheiros):
            soma = ((soma + os.path.getsize(ficheiros))/1024)
        if os.path.isdir(ficheiros):
            calcula_tamanho_pasta(ficheiros)

    return soma
def main():
    name = pede_pasta()
    soma = calcula_tamanho_pasta(name)
    print(soma)
if __name__ == "__main__":
  main()