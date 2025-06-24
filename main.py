import pygame
import data
import cv2
import sys
import menu
import dialogo
import serial
import threading

pygame.init()

pygame.display.set_caption("Vrum! A Jornada")
pygame.mixer.music.load('music_menu.mp3',"mp3")
font = pygame.font.Font('freesansbold.ttf', 24)
screen = pygame.display.set_mode((data.width,data.height))
timer = pygame.time.Clock

menu_background_img = pygame.image.load(data.menu_background).convert()
menu_jogar_img = pygame.image.load(data.menu_jogar).convert()
menu_background_img = pygame.transform.scale(menu_background_img, (data.width, data.height))
menu_jogar_img = pygame.transform.scale(menu_jogar_img, (data.width, data.height))
miku_open_img = pygame.image.load(data.miku_talking_open).convert() 
miku_close_img = pygame.image.load(data.miku_talking_close).convert()
miku_open_img = pygame.transform.scale(miku_open_img, (data.width, data.height))
miku_close_img = pygame.transform.scale(miku_close_img, (data.width, data.height))

video = cv2.VideoCapture(data.video_path)
success, img = video.read()
fps = video.get(cv2.CAP_PROP_FPS)

sensor_result = None
sensor_thread_done = False

def get_average_sensor_value_from_serial(ser, prefix='VAL:', num_values=1):
    value = 0
    port = 0
    try:
        line = ser.readline().decode(errors='ignore').strip()
        if line:
            sensor = line.split(':')
            port = sensor[1].replace('VAL', '')
            value = sensor[2]
    except Exception as e:
        print("Erro ao ler da serial:", e)

    if value==0 or port==0:
        return None
    else:
        return port, value


# Thread que lê valor do sensor
def read_sensor_thread(ser, prefix='VAL:', num_values=1):
    global sensor_result, sensor_thread_done
    sensor_result = get_average_sensor_value_from_serial(ser, prefix, num_values)
    sensor_thread_done = True

def fade_out():
    fade = pygame.Surface((data.width, data.height))
    fade.fill(data.BLACK)
    for alpha in range(data.FADECOLOR):
        fade.set_alpha(alpha)
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(30)

def cutscene(clock):
    success, img = video.read()
    if success:
        # Converte a imagem do OpenCV (BGR) para uma superfície do Pygame (RGB)
        img_red = cv2.resize(img, (data.width, data.height))
        screen.blit(pygame.image.frombuffer(img_red.tobytes(), (data.width, data.height), "BGR"), (0, 0))
    pygame.display.flip()
    clock.tick(fps)

def start_game():
    running = True
    clock = pygame.time.Clock()
    delta_time = 0.1
    global sensor_result, sensor_thread_done

    # Abrir porta serial uma vez só
    try:
        ser = serial.Serial('COM9', 115200, timeout=1)
        ser.setDTR(False)
        ser.setRTS(False)
    except Exception as e:
        print("Erro ao abrir porta serial:", e)
        return

    while running:
        if(data.estado == 'menu'):
            menu.start()
        elif(data.estado == 'dialogo'):
            dialogo.gato()
        elif(data.estado == 'cutscene'):
            cutscene(clock)
        elif(data.estado == 'fade'):
            fade_out()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if(data.estado == 'menu'):
                        print("menu")
                        menu.game_selected()
                    elif(data.estado == 'dialogo'):
                        if(len(data.frase_atual) == len(data.frase_objetivo[data.index_frase])):
                            waiting_input = True
                            # Inicia leitura em thread
                            sensor_result = None
                            sensor_thread_done = False
                            thread = threading.Thread(target=read_sensor_thread, args=(ser,))
                            thread.start()
                            #Primeiro Nivel
                            while waiting_input:
                                data.estado = 'cutscene'
                                if sensor_thread_done:
                                    if sensor_result is not None:
                                        #logica de validacao do sensor
                                        print(sensor_result)
                                        # show_message(sensor_result, GREEN)

                                waiting_input = False
                                data.estado = 'dialogo'
                        else:
                            data.frase_atual = data.frase_objetivo[data.index_frase]
                            dialogo.show_message(data.frase_atual, data.BLACK)
                    elif(data.estado == 'cutscene'):
                        screen.fill(data.BLACK)
                        data.estado = 'hospital'
                        cv2.destroyAllWindows()

        pygame.display.flip()
        delta_time = clock.tick(60) / 1000
        delta_time = max(0.001, min(0.1, delta_time))

    pygame.quit()
start_game()