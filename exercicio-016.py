def fibonacci(n):
    if n <= 0:
        return "Número inválido"
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

def main():
    while True:
        entrada = input("Digite um número inteiro maior ou igual a 3 ou 'fim' para encerrar: ")

        if entrada.lower() == 'fim':
            print("Encerrando o programa...")
            break
        
        try:
            numero = int(entrada)
            resultado = fibonacci(numero)
            if resultado == "Número inválido":
                print("Por favor, digite um número inteiro maior ou igual a 3.")
            else:
                print(f"O {numero}-ésimo termo da série de Fibonacci é {resultado}.")
        except ValueError:
            print("Por favor, digite um número inteiro válido ou 'fim' para encerrar.")

if __name__ == "__main__":
    main()
