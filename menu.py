import main
import jogo
import pygame
import sys

pygame.init()

# Configurações da janela
pygame.display.set_caption("Vrum! A Jornada")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
HIGHLIGHT = (0, 200, 200)

# Fonte
font = pygame.font.SysFont(None, 48)
title_font = pygame.font.SysFont(None, 64)

# Opções de menu
menu_options = ["Iniciar Jogo", "Opções", "Sair"]
selected = 0
clock = pygame.time.Clock()

def draw_menu():
    main.screen.fill(BLACK)

    title_surface = title_font.render("Vrum! A Jornada", True, WHITE)
    main.screen.blit(title_surface, (main.WIDTH // 2 - title_surface.get_width() // 2, 50))

    for i, option in enumerate(menu_options):
        color = HIGHLIGHT if i == selected else GRAY
        text_surface = font.render(option, True, color)
        main.screen.blit(text_surface, (main.WIDTH // 2 - text_surface.get_width() // 2, 150 + i * 60))

    pygame.display.flip()

def fade_out():
    fade = pygame.Surface((main.WIDTH, main.HEIGHT))
    fade.fill(BLACK)
    for alpha in range(0, 300, 10):
        fade.set_alpha(alpha)
        draw_menu()
        main.screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(30)

def handle_selection(index):
    if menu_options[index] == "Iniciar Jogo":
        fade_out()
        jogo.start_game()
    elif menu_options[index] == "Opções":
        print("Abrindo opções...")
    elif menu_options[index] == "Sair":
        pygame.quit()
        sys.exit()

def menu_loop():
    global selected
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    handle_selection(selected)

        draw_menu()
        clock.tick(60)