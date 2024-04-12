# Lista inicial de lugares vagos nas salas
lugares_vagos = [10, 2, 1, 3, 0]

def exibir_lugares_vagos(lugares):
    print("Utilização das salas:")
    for num_sala, lugares_disponiveis in enumerate(lugares, start=1):
        print(f"Sala {num_sala}: {lugares_disponiveis} lugar(es) vazio(s)")

while True:
    exibir_lugares_vagos(lugares_vagos)
    sala = int(input("Digite o número da sala (ou 0 para sair): "))

    if sala == 0:
        print("Programa encerrado. Até mais!")
        break

    if sala > len(lugares_vagos) or sala < 1:
        print("Sala inválida")
    elif lugares_vagos[sala - 1] == 0:
        print("Desculpe, sala lotada!")
    else:
        lugares_solicitados = int(input(f"Quantos lugares você deseja ({lugares_vagos[sala - 1]} vagos): "))
        if lugares_solicitados > lugares_vagos[sala - 1]:
            print("Esse número de lugares não está disponível.")
        elif lugares_solicitados < 0:
            print("Número inválido")
        else:
            lugares_vagos[sala - 1] -= lugares_solicitados
            print(f"{lugares_solicitados} lugares vendidos")

# Exibe lugares vagos após as vendas
exibir_lugares_vagos(lugares_vagos)
