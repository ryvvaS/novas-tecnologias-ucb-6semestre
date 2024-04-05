
def calculo_digito_verificador(numero_conta):
    soma_digitos = sum(int(digito) for digito in str(numero_conta))
    digito_verificador = soma_digitos % 10
    return digito_verificador

def inserir_digito_verificador(numero_conta):
    digito_verificador = calculo_digito_verificador(numero_conta)
    return f"{numero_conta:06d}-{digito_verificador}"

def main():
    while True:
        entrada = input("Digite o número da conta (até seis dígitos) ou 'fim' para encerrar: ")

        if entrada.lower() == 'fim':
            print("Encerrando o programa...")
            break
        
        try:
            numero_conta = int(entrada)
            if not (0 <= numero_conta <= 9999): # (9999 é para ter espaço de calculo para a questão)
                print("Por favor, digite um número de até seis dígitos.")
            else:
                numero_conta_completo = inserir_digito_verificador(numero_conta)
                print(f"Número de conta completo: {numero_conta_completo}")
        except ValueError:
            print("Por favor, digite um número inteiro válido ou 'fim' para encerrar.")

if __name__ == "__main__":
    main()
