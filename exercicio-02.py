def exibir_caixa(largura, altura):
    for i in range(altura):
        if i == 0 or i == altura - 1:
            print('*' * largura)
        else:
            print('*' + ' ' * (largura - 2) + '*')

def exibir_oval(largura, altura):

    a = largura // 2
    b = altura // 2
    for y in range(altura):
        for x in range(largura):
            if ((x - a) / a) ** 2 + ((y - b) / b) ** 2 <= 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

def exibir_seta(largura):
    for i in range(largura):
        print(' ' * (largura - i - 1) + '*' * (i * 2 + 1))

def exibir_losango(largura):
    for i in range(largura):
        print(' ' * (largura - i - 1) + '*' * (i * 2 + 1))
    for i in range(largura - 2, -1, -1):
        print(' ' * (largura - i - 1) + '*' * (i * 2 + 1))

def main():
    largura = 10
    altura = 5
    
    print("Caixa:")
    exibir_caixa(largura, altura)
    print("\nOval:")
    exibir_oval(largura, altura)
    print("\nSeta:")
    exibir_seta(largura)
    print("\nLosango:")
    exibir_losango(largura)

if __name__ == "__main__":
    main()
