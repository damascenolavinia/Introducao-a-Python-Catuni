import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nomes = ["Alice", "Joao", "Ana", "Jose", "Carlos", "Janaina", "Caio", "Cristiane"]
nomes_com_j = []
nomes_com_c = []
nomes_com_a = []
for nome in nomes:
    if nome.startswith("A"):
        nomes_com_a.append(nome)
    elif nome.startswith("J"):
        nomes_com_j.append(nome)
    elif nome.startswith("C"):
        nomes_com_c.append(nome)
#print (nomes_com_a)
#print (nomes_com_j)
#print (nomes_com_c)

idades = [17, 18, 25, 43, 15, 29, 36, 50]
maior_de_idade = []
menor_de_idade = []
for idade in idades:
    if idade > 18:
        maior_de_idade.append(idade)
    elif idade <= 18:
        menor_de_idade.append(idade)
#print (maior_de_idade)
#print (menor_de_idade)

salarios = [2000, 5000, 1500, 2100, 5000, 1500, 2000, 2000]
contagem ={}
for salario in salarios:
    if salario in contagem:
        contagem[salario]=contagem[salario]+1
    else:
        contagem[salario]=1
#print(contagem)

letras = ["A","B","C","C","A","C","B","B","A"]
contagem_categorias ={}
for letra in letras:
    if letra in contagem_categorias:
        contagem_categorias[letra]=contagem_categorias[letra]+1
    else:
        contagem_categorias[letra]=1
print (contagem_categorias)

numero=1
while numero <= 10:
    if numero % 5 == 0:
        print (f"Numero {numero} e divisivel por 5")
    numero +=1

numero = 1
while numero <= 20:
    if numero % 2 == 0:
        print (f"Numero {numero} par")
    else:
        print (f"Numero {numero} impar")
    numero += 1