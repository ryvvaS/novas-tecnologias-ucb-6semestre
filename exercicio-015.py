def calcular_quadrado_soma_impares(n):
    soma = 0
    numero_impar = 1
    for _ in range(n):
        soma += numero_impar
        numero_impar += 2
    return soma

def main():
    while True:
        entrada = input("Digite um número natural ou 'fim' para encerrar: ")

        if entrada.lower() == 'fim':
            print("Encerrando o programa...")
            break
        
        try:
            numero = int(entrada)
            if numero <= 0:
                print("Por favor, digite um número natural positivo.")
            else:
                quadrado = calcular_quadrado_soma_impares(numero)
                print(f"O quadrado de {numero} é {quadrado}.")
        except ValueError:
            print("Por favor, digite um número natural válido ou 'fim' para encerrar.")

if __name__ == "__main__":
    main()
