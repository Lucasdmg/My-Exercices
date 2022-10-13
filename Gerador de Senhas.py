#BY Lucas Domingues "Osíris"
from random import choice
import string

print(5*"*","Gerador de Senhas Aleatório",5*"*")
key = int(input("Digite Quantas Chaves Gerar \n >> "))
caract = int(input("Digite o Numero de Caracteres\n >> "))

print(5*"*"," Selecione a Caracteristica da Senha ",5*"*")

print("1 = Letras ")
print("2 = Numeros ")
print("3 = Numeros + Letras ")
print("4 = Numeros + Letras + Especial ")

comp = int(input("Digite 1, 2, 3 ou 4 \n >> "))
print("Senha:")

for i in range(key):
    length = caract
    keys1 = (string.ascii_letters)
    keys2 = (string.octdigits)
    keys3 = (string.hexdigits)
    keys4 = (string.hexdigits + string.ascii_letters + string.punctuation)

    keygen1 = ''
    keygen2 = ''
    keygen3 = ''
    keygen4 = ''

    for i in range(length):
      keygen1 += choice(keys1)
      keygen2 += choice(keys2)
      keygen3 += choice(keys3)
      keygen4 += choice(keys4)
    if comp == 1:
        print(f"{keygen1}")
    elif comp == 2:
        print(f"{keygen2}")
    elif comp == 3:
        print(f"{keygen3}")
    elif comp == 4:
        print(f"{keygen4}")
    else:
        print("Erro !!! ")
