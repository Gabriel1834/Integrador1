import main
import pygame
import data

menu_options = ["Iniciar Jogo", "Opções", "Sair"]
selected = 0

def start():
    if(data.music == 0):
        pygame.mixer.music.play()
        data.music = 'miku'
    main.screen.blit(main.menu_background_img, (1, 1))
    # title_surface = title_font.render("Vrum! A Jornada", True, data.WHITE)

    # for i, option in enumerate(menu_options):
    #     color = data.HIGHLIGHT if i == selected else data.GRAY
        # text_surface = font.render(option, True, color)

def game_selected():
    data.estado = 'dialogo'
    pygame.time.delay(200)
    main.screen.blit(main.menu_jogar_img, (1, 1))
    pygame.display.update()
    pygame.time.delay(1000)
    pygame.mixer.music.stop()

# def handle_selection(index):
#     if menu_options[index] == "Iniciar Jogo":
#         fade_out()
#         main.start_game()
#     elif menu_options[index] == "Opções":
#         print("Abrindo opções...")
#     elif menu_options[index] == "Sair":
#         pygame.quit()
#         sys.exit()

