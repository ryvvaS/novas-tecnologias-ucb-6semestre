def verificar_numero(numero):
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

def main():
    while True:
        entrada = input("Digite um número inteiro ou 'fim' para encerrar: ")
        if entrada.lower() == 'fim':
            print("Encerrando o programa...")
            break
        try:
            numero = int(entrada)
            verificar_numero(numero)
        except ValueError:
            print("Por favor, digite um número inteiro válido ou 'fim' para encerrar.")

if __name__ == "__main__":
    main()
