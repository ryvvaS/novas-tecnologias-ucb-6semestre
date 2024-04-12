def verifica_parenteses(expressao):
    pilha = []  

    for caractere in expressao:
        if caractere == '(':  
            pilha.append(caractere)
        elif caractere == ')':  
            if not pilha:  
                return False
            
            if pilha[-1] == '(':
                pilha.pop()  
            else:
                return False  

    
    return not pilha

while True:
    
    expressao_usuario = input("Digite a expressão com parênteses (ou 'sair' para encerrar): ")

    if expressao_usuario.lower() == 'sair':
        print("Programa encerrado. Até mais!")
        break

    
    if verifica_parenteses(expressao_usuario):
        print("Expressão válida! Os parênteses estão balanceados corretamente.")
    else:
        print("Expressão inválida! Verifique a ordem dos parênteses.")
