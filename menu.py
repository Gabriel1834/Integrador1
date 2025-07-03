import main
import pygame
import data

def start():
    if(data.music == 0):
        pygame.mixer.music.play()
        data.music = 'miku'
    main.screen.blit(main.menu_background_img, (1, 1))

def game_selected():
    data.estado = 'dialogo'
    pygame.time.delay(200)
    main.screen.blit(main.menu_jogar_img, (1, 1))
    pygame.display.update()
    pygame.time.delay(1000)
    pygame.mixer.music.stop()


