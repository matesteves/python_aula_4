# Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

#lista: list = list(range(1, 11))
#for i in lista:
#    print(lista[i]**2)

# Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

#lista: list = ["Python", "Java", "C++", "JavaScript"]
#
#lista.remove("C++")
#lista.append("Ruby")
#
#print(lista)

# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

#livro: dict = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}
#for info in livro:
#    print(info, ":", livro[info])

# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um # dicionário.

#texto: str = "Escreva um programa que conta o número de ocorrências de cada caractere em uma string #usando um # dicionário."
#count: dict = {}
#
#for character in texto:
#    if character in count:
#        count[character] += 1
#    else:
#        count[character] = 1
#
#print(count)

# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, # calcule o preço total da lista de compras.

#lista: list = ["maçã", "banana", "cereja"]
#precos: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
#
#total: float = 0
#
#for compra in lista:
#    total += precos[compra]
#
#print(total)