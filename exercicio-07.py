def converter_segundos_para_tempo(segundos):
    # Nesse bloco de codigo estão defindas os calculos para número de dias, horas, minutos e segundos
    dias = segundos // (24 * 3600)
    horas = (segundos % (24 * 3600)) // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    
    return dias, horas, minutos, segundos_restantes

def main():
    while True:
        entrada = input("Digite a quantidade de segundos ou 'fim' para encerrar: ")
        
        if entrada.lower() == 'fim':
            print("Encerrando o programa...")
            break
        
        try:
            segundos = int(entrada)
            if segundos < 0:
                print("Por favor, digite um valor positivo de segundos.")
            else:
                dias, horas, minutos, segundos_restantes = converter_segundos_para_tempo(segundos)
                print(f"Resultado: {dias} dias, {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")
        except ValueError:
            print("Por favor, digite um número inteiro válido ou 'fim' para encerrar.")

if __name__ == "__main__":
    main()