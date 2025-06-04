import time

# Iniciano o Jogo:
print("Olá, jogador!")
print("--------------------")
time.sleep(1)

# Definindo o nome no jogo: 
nome = input("Para iniciarmos o jogo, informe o seu nome:\n")
print("--------------------")

# Boas vindas ao jogo:
print(f"Bem vindo ao COURT LABYRINTH, {nome}!")
print("--------------------")
time.sleep(2)

# Explicando o Jogo:
print("Para iniciarmos o jogo, você precisa apenas saber como funciona:")
print("--------------------")
time.sleep(1)
print('- Para andar para a DIREITA, use a tecla "D"')
time.sleep(1)
print('- Para andar para a ESQUERDA, use a tecla "A"')
time.sleep(1)
print('- Para andar para BAIXO, use a tecla "S"')
time.sleep(1)
print('- Para andar para a CIMA, use a tecla "W"')
time.sleep(1)
print('- Você precisa chegar no final do labirinto indicado pelo ícone: ♔')
time.sleep(0.5)
print("--------------------")
time.sleep(2)

# Loop para checar se o jogador entendeu as regras
entendeu = None

while entendeu != "s":
    entendeu = input("Você entendeu as regras? [S/N]: ").lower()
    
    if entendeu == "s":
        print("Ótimo! Vamos começar o jogo!")
        print("--------------------")
        time.sleep(1)
    else:
        print("Sem problemas! Vamos revisar as regras de novo.\n")
        time.sleep(1)
        print('- Para andar para a DIREITA, use a tecla "D"')
        time.sleep(1)
        print('- Para andar para a ESQUERDA, use a tecla "A"')
        time.sleep(1)
        print('- Para andar para BAIXO, use a tecla "S"')
        time.sleep(1)
        print('- Para andar para CIMA, use a tecla "W"')
        time.sleep(1)
        print('- Você precisa chegar no final do labirinto indicado pelo íconte: ♔')
        time.sleep(0.5)
        print("--------------------")


# Função para exibir o labirinto
def exibir_labirinto(jogador_pos, labirinto):
    labirinto_temp = [linha[:] for linha in labirinto]  # Cria uma cópia do labirinto
    x, y = jogador_pos  # Posição do jogador
    labirinto_temp[x][y] = '♙'  # Colocando o '♙' na posição do jogador
    
    # Exibindo o labirinto
    for linha in labirinto_temp:
        print(" ".join(linha))

# Função para mover o jogador
def mover_jogador(pos, movimento, labirinto):
    x, y = pos
    
    if movimento == 'w' and x > 0 and labirinto[x-1][y] != '#':  # Para cima
        x -= 1
    elif movimento == 's' and x < 4 and labirinto[x+1][y] != '#':  # Para baixo
        x += 1
    elif movimento == 'a' and y > 0 and labirinto[x][y-1] != '#':  # Para a esquerda
        y -= 1
    elif movimento == 'd' and y < 4 and labirinto[x][y+1] != '#':  # Para a direita
        y += 1
    else:
        print("Movimento inválido. Tente novamente.")  # Feedback de movimento inválido
    return (x, y)

# Função principal para rodar o jogo
def jogar():
    # Criando um labirinto 5x5 com obstáculos (#)
    labirinto = [
        ['.', '.', '.', '#', '.'],
        ['.', '#', '.', '#', '.'],
        ['.', '.', '.', '#', '.'],
        ['#', '#', '.', '.', '.'],
        ['.', '.', '.', '#', '♔']
    ]
    
    jogador_pos = (0, 0)  # Posição inicial do jogador (canto superior esquerdo)
    objetivo = (4, 4)  # Posição do objetivo (canto inferior direito)
    
    while jogador_pos != objetivo:
        exibir_labirinto(jogador_pos, labirinto)  # Exibe o labirinto
        movimento = input("Digite o movimento (W = CIMA, S = BAIXO, A = ESQUERDA, D = DIREITA): ")
        
        # Move o jogador
        jogador_pos = mover_jogador(jogador_pos, movimento, labirinto)
        
        # Verifica se o jogador chegou ao objetivo
        if jogador_pos == objetivo:
            exibir_labirinto(jogador_pos, labirinto)
            print("Parabéns! Você venceu!")
            break

# Inicia o jogo
jogar()

