# Lista inicial de valores
V = [9, 8, 7, 12, 0, 13, 21]

# Inicializa valores
valores_pares = []
valores_impares = []

# Percorre a lista V e separa os valores
for valor in V:
    if valor % 2 == 0:
        valores_pares.append(valor)
    else:
        valores_impares.append(valor)


print(f"Valores pares: {valores_pares}")
print(f"Valores ímpares: {valores_impares}")
