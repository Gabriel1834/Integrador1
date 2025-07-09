import data
import pygame
import main

def show_message(message, color):
    text_surface = main.font.render(message, True, color)
    main.screen.blit(
        text_surface,
        (data.width // 2 - text_surface.get_width() // 2, data.height // 2 + 240),
    )

frase_acabou = {
    "frase_acabou": False
}

def gato(index_frase, background, background2):
    if(len(data.frase_atual) == len(data.frase_objetivo[data.index_frase])):
        main.screen.blit(main.background2, (1, 1))
        show_message(data.frase_atual, data.BLACK)
        if(data.frase_objetivo[data.index_frase + 1] == "*"):
            frase_acabou['frase_acabou'] = True
    elif(len(data.frase_atual)%2 == 0):
        main.screen.blit(main.background, (1, 1))
        data.frase_atual = data.frase_atual + data.frase_objetivo[data.index_frase][len(data.frase_objetivo[data.index_frase]) - data.letra]
        show_message(data.frase_atual, data.BLACK)
        data.letra -= 1
        pygame.time.delay(75)
    elif(len(data.frase_atual)%2 == 1):
        main.screen.blit(main.background2, (1, 1))
        data.frase_atual = data.frase_atual + data.frase_objetivo[data.index_frase][len(data.frase_objetivo[data.index_frase]) - data.letra]
        show_message(data.frase_atual, data.BLACK)
        data.letra -= 1
        pygame.time.delay(75)

def caminho_errado():
    if(len(data.frase_atual) == len(data.frase_caminho_errado[0])):
        main.screen.blit(main.miku_close_img, (1, 1))
        show_message(data.frase_atual, data.BLACK)
        frase_acabou['frase_acabou'] = True
    elif(len(data.frase_atual)%2 == 0):
        main.screen.blit(main.miku_open_img, (1, 1))
        data.frase_atual = data.frase_atual + data.frase_caminho_errado[0][len(data.frase_caminho_errado[0]) - data.letra]
        show_message(data.frase_atual, data.BLACK)
        data.letra -= 1
        pygame.time.delay(75)
    elif(len(data.frase_atual)%2 == 1):
        main.screen.blit(main.miku_close_img, (1, 1))
        data.frase_atual = data.frase_atual + data.frase_caminho_errado[0][len(data.frase_caminho_errado[0]) - data.letra]
        show_message(data.frase_atual, data.BLACK)
        data.letra -= 1
        pygame.time.delay(75)