def verificar_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    while True:
        entrada = input("Digite um número ou 'fim' para encerrar: ")

        if entrada.lower() == 'fim':
            print("Encerrando o programa...")
            break
        
        try:
            numero = int(entrada)
            if verificar_primo(numero):
                print(f"{numero} é um número primo.")
            else:
                print(f"{numero} não é um número primo.")
        except ValueError:
            print("Por favor, digite um número inteiro válido ou 'fim' para encerrar.")

if __name__ == "__main__":
    main()
