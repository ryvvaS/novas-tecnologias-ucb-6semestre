import math

def calcular_raizes(a, b, c):
   
    discriminante = b**2 - 4*a*c
    
    if discriminante < 0:
        return None, None  
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return x1, x2

def main():
    while True:
        entrada = input("Digite os coeficientes da equação quadrática (a, b, c), separados por espaços, ou 'fim' para encerrar: ")
        
        if entrada.lower() == 'fim':
            print("Encerrando o programa...")
            break
        
        try:
            coeficientes = [float(x) for x in entrada.split()]
            if len(coeficientes) != 3:
                print("Por favor, insira exatamente três coeficientes.")
            else:
                a, b, c = coeficientes
                x1, x2 = calcular_raizes(a, b, c)
                if x1 is None:
                    print("Não há raízes reais para os coeficientes fornecidos.")
                else:
                    print("Raízes da equação quadrática:")
                    print(f"x' = {x1}")
                    print(f"x'' = {x2}")
        except ValueError:
            print("Por favor, insira coeficientes válidos ou 'fim' para encerrar.")

if __name__ == "__main__":
    main()