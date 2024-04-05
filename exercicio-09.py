def adicao():
    print("Tabuada de Adição:")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} + {j} = {i + j}")
        print()

def subtracao():
    print("Tabuada de Subtração:")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} - {j} = {i - j}")
        print()

def multiplicacao():
    print("Tabuada de Multiplicação:")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} * {j} = {i * j}")
        print()

def divisao():
    print("Tabuada de Divisão:")
    for i in range(1, 11):
        for j in range(1, 11):
            if j != 0:
                print(f"{i} / {j} = {i / j}")
        print()

def main():
    while True:
        print("\nMenu:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicao()
        elif opcao == '2':
            subtracao()
        elif opcao == '3':
            multiplicacao()
        elif opcao == '4':
            divisao()
        elif opcao.lower() == '5':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
