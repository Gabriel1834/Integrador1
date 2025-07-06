import pygame
import data
import cv2
import sys
import menu
import dialogo
import serial
import threading
import re
import msvcrt

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

hospital_img = pygame.image.load(data.hospital).convert()
hospital_img = pygame.transform.scale(hospital_img, (data.width, data.height))

aquario_img = pygame.image.load(data.aquario).convert()
aquario_img = pygame.transform.scale(aquario_img, (data.width, data.height))

background = miku_open_img
background2 = miku_close_img

fase = 0

video = cv2.VideoCapture(data.video_path)
success, img = video.read()
fps = video.get(cv2.CAP_PROP_FPS)

sensor_result = None
sensor_thread_done = False
waiting_input = False

def get_average_sensor_value_from_serial(ser, prefix='VAL:', num_values=1):
    global waiting_input, background, fase
    running2 = True
    while running2:
        line = ser.readline().decode(errors='ignore').strip()
        print(line)
        if line.startswith("Pino") and waiting_input == True:
            parte_pino_str, parte_valor_str = line.split(':')

            pino_match = re.search(r'\d+', parte_pino_str)
            if pino_match:
                pino = int(pino_match.group())
            else:
                pino = None
            valor = int(parte_valor_str)
            if fase == 0:
                if(pino == data.hospital_valor[0]):
                    if((valor > data.hospital_valor[1] - 100) and (valor < data.hospital_valor[1] + 100)):
                        running2 = False
                        return line
            elif fase == 1:
                if(pino == data.aquario_valor[0]):
                    if ((valor > data.aquario_valor[1] - 100) and (valor < data.aquario_valor[1]+ 100)):
                        running2 = False
                        return line



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
    global background, background2, fase
    success, img = video.read()
    if success:
        # Converte a imagem do OpenCV (BGR) para uma superfície do Pygame (RGB)
        img_red = cv2.resize(img, (data.width, data.height))
        screen.blit(pygame.image.frombuffer(img_red.tobytes(), (data.width, data.height), "BGR"), (0, 0))
    else:
        data.frase_atual = ""
        data.index_frase += 2
        data.letra = len(data.frase_objetivo[data.index_frase])
        if background == miku_open_img:
            background = hospital_img
            background2 = hospital_img
            fase += 1
        elif background == hospital_img:
            background = aquario_img
            background2 = aquario_img
            fase += 1
        data.estado = "dialogo"
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)

    pygame.display.flip()
    clock.tick(fps)

def start_game():
    dialogo.frase_acabou['frase_acabou'] = False
    running = True
    clock = pygame.time.Clock()
    delta_time = 0.1
    global sensor_result, sensor_thread_done, waiting_input

    # Abrir porta serial uma vez só
    try:
        ser = serial.Serial('COM9', 115200, timeout=1)
        ser.setDTR(False)
        ser.setRTS(False)
    except Exception as e:
        print("Erro ao abrir porta serial:", e)
        return
    sensor_result = None
    sensor_thread_done = False
    thread = threading.Thread(target=read_sensor_thread, args=(ser,))
    thread.start()

    while running:
        if(data.estado == 'menu'):
            menu.start()
        elif(data.estado == 'dialogo'):
            if dialogo.frase_acabou['frase_acabou']:
                print("entrou no if da frase")
                data.estado = 'sensor'
            else:
                dialogo.gato(data.index_frase, background, background2)
        elif(data.estado == 'sensor'):
            print("entrou no if do sensor")
            waiting_input = True
            while waiting_input:
                if sensor_thread_done:
                    if sensor_result is not None:
                        data.estado = 'cutscene'
                        waiting_input = False
                        # resetando o valor do sensor
                        ser.setDTR(False)
                        ser.setRTS(False)
                        sensor_result = None
                        sensor_thread_done = False
                        thread = threading.Thread(target=read_sensor_thread, args=(ser,))
                        thread.start()
                    else:
                        waiting_input = False
            while msvcrt.kbhit():
                msvcrt.getch()
            dialogo.frase_acabou['frase_acabou'] = False
        elif(data.estado == 'cutscene'):
            cutscene(clock)
        elif(data.estado == 'fade'):
            fade_out()
        if(data.estado == 'dialogo' or data.estado == 'menu'):
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
                            if(len(data.frase_atual) == len(data.frase_objetivo[data.index_frase]) and dialogo.frase_acabou['frase_acabou'] == False):
                                data.frase_atual = ""
                                data.index_frase += 1
                                data.letra = len(data.frase_objetivo[data.index_frase])
                            else:
                                data.frase_atual = data.frase_objetivo[data.index_frase]
                                dialogo.show_message(data.frase_atual, data.BLACK)
                        elif(data.estado == 'cutscene'):
                            screen.fill(data.BLACK)
                            data.estado = 'dialogo'
                            # cv2.destroyAllWindows()

        pygame.display.flip()
        delta_time = clock.tick(60) / 1000
        delta_time = max(0.001, min(0.1, delta_time))

    pygame.quit()
start_game()