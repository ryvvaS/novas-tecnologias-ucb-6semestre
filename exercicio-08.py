
def converter_temperatura(temp_celsius):
    #Nesse bloco setei as mudanças de  temperatura para fahrenheit e kelvin conforme a formula de cada uma delas.
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    temp_kelvin = temp_celsius + 273.15
    return temp_fahrenheit, temp_kelvin

def main():
    while True:
        entrada = input("Digite a temperatura em Celsius ou 'fim' para encerrar: ")

        if entrada.lower() == 'fim':
            print("Encerrando o programa...")
            break
        
        try:
            temp_celsius = float(entrada)
            temp_fahrenheit, temp_kelvin = converter_temperatura(temp_celsius)
            print(f"Temperatura em Fahrenheit: {temp_fahrenheit:.2f} °F")
            print(f"Temperatura em Kelvin: {temp_kelvin:.2f} °K")
        except ValueError:
            print("Por favor, digite uma temperatura válida em Celsius ou 'fim' para encerrar.")

if __name__ == "__main__":
    main()
