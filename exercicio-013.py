def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i
        return fatorial

def main():
    while True:
        entrada = input("Digite um número não negativo ou 'fim' para encerrar: ")

        if entrada.lower() == 'fim':
            print("Encerrando o programa...")
            break
        
        try:
            numero = int(entrada)
            if numero < 0:
                print("Por favor, digite um número não negativo.")
            else:
                resultado = calcular_fatorial(numero)
                print(f"O fatorial de {numero} é {resultado}.")
        except ValueError:
            print("Por favor, digite um número inteiro válido ou 'fim' para encerrar.")

if __name__ == "__main__":
    main()