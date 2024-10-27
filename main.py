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

# Objetivo: Dada uma lista de emails, remover todos os duplicados.

#emails: list = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
#novos_emails: list = list(set(emails))
#print(novos_emails)

# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

#idades = [22, 15, 30, 17, 18]
#adultos = [idade for idade in idades if idade >= 18 ]
#print(adultos)

# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

#pessoas: dict = [
#    {"nome": "Alice", "idade": 30},
#    {"nome": "Carol", "idade": 20},
#    {"nome": "Bob", "idade": 25}
#]
#
#pessoas.sort(key=lambda pessoa: pessoa["nome"])
#
#print(pessoas)

# Objetivo: Dado um conjunto de números, calcular a média.

#numeros: list = [10, 20, 30, 40, 50]
#
#media = sum(numeros)/ len(numeros)
#print(media)

# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

#valores: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#pares:list = []
#impares:list = []
#
#for num in valores:
#    if num % 2 == 0:
#        pares.append(num)
#    else:
#        impares.append(num)
#print("Pares: ", pares, "\nÍmpares: ", impares)

#Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

#produtos: list = [
#    {"id": 1, "nome": "Teclado", "preço": 100},
#    {"id": 2, "nome": "Mouse", "preço": 80},
#    {"id": 3, "nome": "Monitor", "preço": 300}
#]
#
#novo_preco: int = 100
#
#for produto in produtos:
#    if produto["id"] == 2:
#        produto["preço"] = novo_preco
#        break
#print(produtos)

# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

#dicionario1: dict = {"a": 1, "b": 2}
#dicionario2: dict = {"c": 3, "d": 4}
#
#dicionario1.update(dicionario2)
#
#print(dicionario1)

# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

#estoque: dict = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
#
#com_estoque: dict = {i: j for i, j in estoque.items() if j > 0}
#print(com_estoque)

#Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

#dicionario: dict = {"a": 1, "b": 2, "c": 3}

# entendi errado:
# lista: list = []
#for key in dicionario:
#    lista.append([key, dicionario[key]])
#print(lista)

#keys: list = list(dicionario.keys())
#values: list = list(dicionario.values())
#
#print(keys)
#print(values)

#Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

#texto: str = "engenharia de dados"
#
#count: dict = {}
#for character in texto:
#    if character in count:
#        count[character] += 1
#    else:
#        count[character] = 1
#print(count)