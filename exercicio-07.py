def exibe_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(map(str, linha)))

def verifica_vitoria(tabuleiro, jogador):
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador or tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

def jogo_da_velha():
    tabuleiro = [[0, 0, 0] for _ in range(3)]
    jogadores = ["X", "O"]
    jogador_atual = 0
    jogadas = 0

    while True:
        exibe_tabuleiro(tabuleiro)
        linha = int(input(f"Jogador {jogadores[jogador_atual]}, escolha a linha (1 a 3): ")) - 1
        coluna = int(input(f"Jogador {jogadores[jogador_atual]}, escolha a coluna (1 a 3): ")) - 1

        if tabuleiro[linha][coluna] == 0:
            tabuleiro[linha][coluna] = jogadores[jogador_atual]
            jogadas += 1
            if verifica_vitoria(tabuleiro, jogadores[jogador_atual]):
                exibe_tabuleiro(tabuleiro)
                print(f"Jogador {jogadores[jogador_atual]} venceu!")
                break
            elif jogadas == 9:
                exibe_tabuleiro(tabuleiro)
                print("Empate!")
                break
            jogador_atual = 1 - jogador_atual
        else:
            print("Posição ocupada. Escolha outra.")

if __name__ == "__main__":
    jogo_da_velha()
