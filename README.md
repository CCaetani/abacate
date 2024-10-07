import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jogo dos Botões")

# Cores
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Configurações do jogo
num_buttons = 6
eliminator_index = -1  # Índice do botão eliminador
buttons = []
game_over = False
click_count = 0  # Contador de cliques em botões seguros

# Posições fixas para os botões (cantos da tela)
button_positions = [
    (50, 50),  # Canto superior esquerdo
    (screen_width - 150, 50),  # Canto superior direito
    (50, screen_height - 150),  # Canto inferior esquerdo
    (screen_width - 150, screen_height - 150),  # Canto inferior direito
    (screen_width // 2 - 50, 50),  # Centro superior
    (screen_width // 2 - 50, screen_height - 150)  # Centro inferior
]

# Carregar a imagem do tigre
# Função para criar botões
def create_buttons():
    global buttons, eliminator_index
    buttons.clear()
    random_positions = random.sample(button_positions, num_buttons)  # Escolhe posições aleatórias
    for pos in random_positions:
        buttons.append(pygame.Rect(pos[0], pos[1], 100, 50))
    eliminator_index = random.randint(0, num_buttons - 1)  # Escolhe um botão eliminador aleatoriamente

# Função para desenhar botões
def draw_buttons():
    for i, button in enumerate(buttons):
        pygame.draw.rect(screen, GRAY, button)  # Botões são cinzas
        font = pygame.font.Font(None, 36)
        text_surface = font.render(str(i + 1), True, BLACK)  # Números nos botões
        text_rect = text_surface.get_rect(center=button.center)
        screen.blit(text_surface, text_rect)

# Função para desenhar a tela de eliminação
def draw_game_over():
    screen.fill(RED)

    font = pygame.font.Font(None, 74)
    text = font.render("Você foi eliminado!", True, BLACK)
    screen.blit(text, (screen_width // 2 - 250, screen_height // 2 + 50))  # Ajuste a posição do texto
    pygame.display.flip()
    pygame.time.delay(2000)  # Espera 2 segundos antes de voltar à tela inicial

# Função principal do jogo
def game_loop():
    global game_over, click_count
    click_count = 0  # Reinicia o contador
    create_buttons()
    game_over = False

    while not game_over:
        screen.fill(WHITE)
        draw_buttons()

        # Mostrar a contagem de cliques
        font = pygame.font.Font(None, 36)
        count_text = f"Cliques em botões seguros: {click_count}"
        text_surface = font.render(count_text, True, BLACK)
        screen.blit(text_surface, (50, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botão esquerdo do mouse
                    mouse_pos = event.pos
                    for i, button in enumerate(buttons):
                        if button.collidepoint(mouse_pos):
                            if i == eliminator_index:
                                # Jogador clicou no botão eliminador
                                game_over = True
                                break
                            else:
                                # Jogador clicou em um botão seguro
                                click_count += 1  # Incrementa o contador
                                create_buttons()  # Reinicia com novos botões
                                break

        # Desenhar botões e atualizar tela
        pygame.display.flip()

    draw_game_over()  # Mostra a tela de eliminação

# Função para desenhar a tela inicial
def draw_start_screen():
    screen.fill(WHITE)

    font = pygame.font.Font(None, 74)
    text = font.render("Clique para Começar", True, BLACK)
    screen.blit(text, (screen_width // 2 - 200, screen_height // 2 + 50))  # Ajuste a posição do texto

    pygame.display.flip()

# Loop principal do jogo
running = True
while running:
    draw_start_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Botão esquerdo do mouse
                game_loop()  # Começar o jogo

    pygame.display.flip()

pygame.quit()
