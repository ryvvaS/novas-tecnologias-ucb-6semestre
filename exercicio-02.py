import random
import string

def carregar_palavras(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            palavras = arquivo.readlines()
            return [palavra.strip() for palavra in palavras]
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return []

def salvar_palavras(nome_arquivo, palavras):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for palavra in palavras:
            arquivo.write(palavra + "\n")

def escolher_palavra_aleatoria(palavras):
    return random.choice(palavras)

def obter_palpite(letras_usadas):
    while True:
        palpite = input("Digite uma letra: ").lower()
        if palpite in string.ascii_lowercase and len(palpite) == 1 and palpite not in letras_usadas:
            return palpite
        else:
            print("Por favor, digite uma letra válida que ainda não foi usada.")
# Funções do jogo
def jogo_da_forca(palavra_secreta):
    # Converte a palavra em uma lista de letras
    letras_corretas = list(palavra_secreta.lower())
    # Cria uma lista de underscores para representar as letras não adivinhadas
    palavra_atual = ['_'] * len(letras_corretas)
    # Número máximo de tentativas
    max_tentativas = 6
    # Inicializa o contador de tentativas
    tentativas = 0
    # Lista para armazenar as letras erradas
    letras_erradas = []
    # Lista para armazenar as letras usadas
    letras_usadas = []

    print("Bem-vindo ao Jogo da Forca!")
    print("Voce tem 6 chances para descobrir, cada erro será representado por um '*' ")
    print("A palavra tem", len(palavra_secreta), "letras.")

    while tentativas < max_tentativas and '_' in palavra_atual:
        print(" ".join(palavra_atual))
        palpite = obter_palpite(letras_usadas)
        letras_usadas.append(palpite)

        if palpite in letras_corretas:
# Atualiza a palavra atual com a letra correta
            for i, l in enumerate(letras_corretas):
                if l == palpite:
                    palavra_atual[i] = palpite
            print("Letra correta!")
        else:
            print("Letra incorreta.")
            tentativas += 1
            letras_erradas.append(palpite)
            print("Chances restantes:", "* " * tentativas + " " * (max_tentativas - tentativas))
            print("Letras erradas:", ", ".join(letras_erradas))

    if '_' not in palavra_atual:
        print("A palavra era:", palavra_secreta)
        return True
    else:
        print("Game over! A palavra era:", palavra_secreta)
        return False

# Carrega as palavras do arquivo
nome_arquivo = "palavras.txt"
lista_palavras = carregar_palavras(nome_arquivo)

while True:
    if lista_palavras:
        # Escolhe uma palavra aleatória da lista de palavras
        palavra_secreta = escolher_palavra_aleatoria(lista_palavras)
        if jogo_da_forca(palavra_secreta):
            nova_palavra = input("Parabéns! Você venceu! Insira uma nova palavra para adicionar ao jogo: ").lower().strip()
            lista_palavras.append(nova_palavra)
            salvar_palavras(nome_arquivo, lista_palavras)
    else:
        print("Nenhuma palavra encontrada no arquivo.")
        break

    resposta = input("Deseja jogar novamente? (s/n): ").lower()
    if resposta != 's':
        break
