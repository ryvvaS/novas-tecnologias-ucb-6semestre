
    
def separar_digitos(numero):
    for d in str(numero):
        print(d, end="   ")

def main():
    while True:
        entrada = input("Digite um número ou 'fim' para encerrar: ")

        if entrada.lower() == 'fim':
            print("Encerrando o programa...")
            break
        
        try:
            numero = int(entrada)
            print("Dígitos separados por três espaços:")
            separar_digitos(numero)
            print()
        except ValueError:
            print("Por favor, digite um número inteiro válido ou 'fim' para encerrar.")

if __name__ == "__main__":
    main()
