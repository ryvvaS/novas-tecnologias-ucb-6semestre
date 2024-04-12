lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

# Imprimindo o maior elemento
maior_elemento = max(lista)
print(f"O maior elemento da lista é: {maior_elemento}")

# Imprimindo o menor elemento
menor_elemento = min(lista)
print(f"O menor elemento da lista é: {menor_elemento}")

# Imprimindo os números pares
numeros_pares = [num for num in lista if num % 2 == 0]
print(f"Números pares na lista: {numeros_pares}")

# Imprimindo número de ocorrências do primeiro elemento da lista
primeiro_elemento = lista[0]
ocorrencias_primeiro_elemento = lista.count(primeiro_elemento)
print(f"O primeiro elemento ({primeiro_elemento}) aparece {ocorrencias_primeiro_elemento} vezes na lista")

# Imprimindo a média dos elementos
media_elementos = sum(lista) / len(lista)
print(f"A média dos elementos da lista é: {media_elementos:.2f}")

# Imprimindo soma dos elementos de valor negativo
elementos_negativos = [num for num in lista if num < 0]
soma_elementos_negativos = sum(elementos_negativos)
print(f"A soma dos elementos negativos é: {soma_elementos_negativos}")
