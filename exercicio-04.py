def separar_digitos(numero):
    numero_str = str(numero)
    for d in str(numero):
        print(d, end="   ")
def main():
    while True:
        print()
        entrada = input("Digite um número de cinco dígitos ou 'fim' para encerrar: ")
        if entrada.lower() == 'fim':
            print("Encerrando o programa...")
            break
        try:
            numero = int(entrada)
            if len(entrada) != 5:
                print("Por favor, insira um número de cinco dígitos.")
            else: 
                separar_digitos(numero)
        except ValueError:
            print("Por favor, digite um número inteiro válido ou 'fim' para encerrar.")

if __name__ == "__main__":
    main()
