import main
import pygame
import random

pygame.init()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Fonte
font = pygame.font.SysFont(None, 48)

# Comandos possíveis
commands = ["Vire à esquerda", "Vire à direita", "Vá para frente"]
keys_map = {
    "Vire à esquerda": pygame.K_LEFT,
    "Vire à direita": pygame.K_RIGHT,
    "Vá para frente": pygame.K_UP,
}

clock = pygame.time.Clock()
running = True


def show_message(message, color):
    text_surface = font.render(message, True, color)
    main.screen.blit(
        text_surface,
        (main.WIDTH // 2 - text_surface.get_width() // 2, main.HEIGHT // 2 + 100),
    )


def draw_challenge(command, score):
    main.screen.fill(BLACK)
    instruction = font.render(command, True, WHITE)
    main.screen.blit(
        instruction,
        (main.WIDTH // 2 - instruction.get_width() // 2, main.HEIGHT // 2 - 50),
    )
    score_text = font.render(f"Pontuação: {score}", True, WHITE)
    main.screen.blit(score_text, (20, 20))
    pygame.display.flip()


def show_game_over():
    main.screen.fill(BLACK)
    over_text = font.render("Game Over!", True, RED)
    main.screen.blit(
        over_text,
        (main.WIDTH // 2 - over_text.get_width() // 2, main.HEIGHT // 2 - 20),
    )
    pygame.display.flip()
    pygame.time.delay(3000)


def start_game():
    global running
    running = True
    score = 0
    while running:
        command = random.choice(commands)
        draw_challenge(command, score)
        waiting_input = True

        while waiting_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                elif event.type == pygame.KEYDOWN:
                    if event.key == keys_map[command]:
                        score += 10
                        draw_challenge(command, score)
                        show_message("Parabéns, você acertou!", GREEN)
                    else:
                        score -= 10
                        draw_challenge(command, score)
                        show_message("Que pena, você errou!", RED)

                    pygame.display.flip()
                    pygame.time.delay(1500)
                    waiting_input = False

                    if score < 0:
                        show_game_over()
                        running = False

        clock.tick(60)

    pygame.quit()
