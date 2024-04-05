def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

def main():
    while True:
        entrada = input("Digite um número inteiro não negativo: ")

        try:
            numero = int(entrada)
            if numero < 0:
                print("Por favor, digite um número inteiro não negativo.")
            else:
                resultado = calcular_fatorial(numero)
                print(f"O fatorial de {numero} é {resultado}.")
                break  
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()
