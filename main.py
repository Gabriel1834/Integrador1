import pygame
import data
import cv2
import sys
import menu
import dialogo
import serial
import threading
import re
import verificacao

pygame.init()

stop_thread_event = threading.Event()

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

bombeiro_img = pygame.image.load(data.bombeiro).convert()
bombeiro_img = pygame.transform.scale(bombeiro_img, (data.width, data.height))

delegacia_img = pygame.image.load(data.delegacia).convert()
delegacia_img = pygame.transform.scale(delegacia_img, (data.width, data.height))

fazenda_img = pygame.image.load(data.fazenda).convert()
fazenda_img = pygame.transform.scale(fazenda_img, (data.width, data.height))

escola_img = pygame.image.load(data.escola).convert()
escola_img = pygame.transform.scale(escola_img, (data.width, data.height))

prefeitura_img = pygame.image.load(data.prefeitura).convert()
prefeitura_img = pygame.transform.scale(prefeitura_img, (data.width, data.height))

papel_img = pygame.image.load(data.papel).convert()
papel_img = pygame.transform.scale(papel_img, (data.width, data.height))

final_img = pygame.image.load(data.final).convert()
final_img = pygame.transform.scale(final_img, (data.width, data.height))

caminho_img = pygame.image.load(data.caminho).convert()
caminho_img = pygame.transform.scale(caminho_img, (data.width, data.height))

background = miku_open_img
background2 = miku_close_img

fase = 0
contador_virada = 0
N_viradas_shared = {
    "N_viradas": 0
}
Max_viradas_shared = {
    "Max_viradas": 0
}

video = cv2.VideoCapture(data.video_path)
success, img = video.read()
fps = video.get(cv2.CAP_PROP_FPS)

sensor_result = None
sensor_thread_done = False
waiting_input = False

def get_average_sensor_value_from_serial(ser, prefix='VAL:', num_values=1):
    global waiting_input, background, background2, fase, contador_virada, N_viradas, acertou
    while not stop_thread_event.is_set():
        try:
            line = ser.readline().decode(errors='ignore').strip()
            if not line:
                continue
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
                    # da praça para o hospital
                    if(pino == data.hospital_valor[0]):
                        if((valor > data.hospital_valor[1] - 100) and (valor < data.hospital_valor[1] + 100)):
                            data.estado = 'cutscene'
                            return line
                elif fase == 1:
                    # do hospital para o aquario
                    if(pino == data.aquario_valor[0]):
                        if ((valor > data.aquario_valor[1] - 100) and (valor < data.aquario_valor[1]+ 100)):
                            data.estado = 'cutscene'
                            return line
                elif fase == 2:
                    Max_viradas_shared['Max_viradas'] = 3
                    # do aquario para o bombeiro
                    print("numero de viradas: ",N_viradas_shared['N_viradas'])
                    #fase direita e esquerda
                    background = caminho_img
                    background2 = caminho_img
                    if (N_viradas_shared['N_viradas'] == 0):
                        valor_anterior = data.valor_31
                        valor_proximo = data.valor_62
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor, line, pino)
                        return line
                    elif (N_viradas_shared['N_viradas'] == 1):
                        valor_anterior = data.valor_62
                        valor_proximo = data.valor_22
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor, line, pino)
                        return line
                    elif (N_viradas_shared['N_viradas'] == 2):
                        valor_anterior = data.valor_22
                        valor_proximo = data.valor_71
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor, line, pino)
                        return line
                    elif (N_viradas_shared['N_viradas'] == 3):
                        valor_anterior = data.valor_71
                        valor_proximo = data.valor_13
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor, line, pino)
                        return line
                elif(fase == 3):
                    Max_viradas_shared['Max_viradas'] = 3
                    #do bombeiro para a delegacia
                    if(N_viradas_shared['N_viradas'] == 0):
                        background = caminho_img
                        background2 = caminho_img
                        valor_anterior = data.valor_13
                        valor_proximo = data.valor_81
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor,line, pino)
                        return line
                    elif(N_viradas_shared['N_viradas'] == 1):
                        background = caminho_img
                        background2 = caminho_img
                        valor_anterior = data.valor_81
                        valor_proximo = data.valor_23
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor, line, pino)
                        return line
                    elif(N_viradas_shared['N_viradas'] == 2):
                        background = caminho_img
                        background2 = caminho_img
                        valor_anterior = data.valor_23
                        valor_proximo = data.valor_22
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor, line, pino)
                        return line
                    elif (N_viradas_shared['N_viradas'] == 3):
                        valor_anterior = data.valor_22
                        valor_proximo = data.valor_21
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor, line, pino)
                        return line
                elif(fase == 4):
                    #da delegacia pra fazenda
                    Max_viradas_shared['Max_viradas'] = 4
                    if(N_viradas_shared['N_viradas'] == 0):
                        background = caminho_img
                        background2 = caminho_img
                        valor_anterior = data.valor_21
                        valor_proximo = data.valor_52
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor,line, pino)
                        return line
                    elif(N_viradas_shared['N_viradas'] == 1):
                        background = caminho_img
                        background2 = caminho_img
                        valor_anterior = data.valor_52
                        valor_proximo = data.valor_31
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor, line, pino)
                        return line
                    elif(N_viradas_shared['N_viradas'] == 2):
                        background = caminho_img
                        background2 = caminho_img
                        valor_anterior = data.valor_31
                        valor_proximo = data.valor_32
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor, line, pino)
                        return line
                    elif(N_viradas_shared['N_viradas'] == 3):
                        background = caminho_img
                        background2 = caminho_img
                        valor_anterior = data.valor_32
                        valor_proximo = data.valor_33
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor, line, pino)
                        return line
                    elif(N_viradas_shared['N_viradas'] == 4):
                        background = caminho_img
                        background2 = caminho_img
                        valor_anterior = data.valor_33
                        valor_proximo = data.valor_82
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor, line, pino)
                        return line
                elif(fase == 5):
                    # da fazenda para escola
                    Max_viradas_shared['Max_viradas'] = 2
                    if(N_viradas_shared['N_viradas'] == 0):
                        background = caminho_img
                        background2 = caminho_img
                        valor_anterior = data.valor_82
                        valor_proximo = data.valor_24
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor, line, pino)
                        return line
                    elif(N_viradas_shared['N_viradas'] == 1):
                        background = caminho_img
                        background2 = caminho_img
                        valor_anterior = data.valor_24
                        valor_proximo = data.valor_91
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor, line, pino)
                        return line
                    elif(N_viradas_shared['N_viradas'] == 2):
                        background = caminho_img
                        background2 = caminho_img
                        valor_anterior = data.valor_91
                        valor_proximo = data.valor_14
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor, line, pino)
                        return line
                elif(fase == 6):
                    # da escola para a prefeitura
                    print("Numero de viradas: ",N_viradas_shared['N_viradas'] )
                    Max_viradas_shared['Max_viradas'] = 1
                    if(N_viradas_shared['N_viradas'] == 0):
                        background = caminho_img
                        background2 = caminho_img
                        valor_anterior = data.valor_14
                        valor_proximo = data.valor_13
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor, line, pino)
                        return line
                    elif(N_viradas_shared['N_viradas'] == 1):
                        background = caminho_img
                        background2 = caminho_img
                        valor_anterior = data.valor_13
                        valor_proximo = data.valor_12
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor, line, pino)
                        return line
                elif(fase == 7):
                    Max_viradas_shared['Max_viradas'] = 3
                    # da prefeitura ao papel
                    if(N_viradas_shared['N_viradas'] == 0):
                        background = caminho_img
                        background2 = caminho_img
                        valor_anterior = data.valor_12
                        valor_proximo = data.valor_11
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor,line, pino)
                        return line
                    elif(N_viradas_shared['N_viradas'] == 1):
                        background = caminho_img
                        background2 = caminho_img
                        valor_anterior = data.valor_11
                        valor_proximo = data.valor_51
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor, line, pino)
                        return line
                    elif(N_viradas_shared['N_viradas'] == 2):
                        background = caminho_img
                        background2 = caminho_img
                        valor_anterior = data.valor_51
                        valor_proximo = data.valor_20
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor, line, pino)
                        return line
                    elif(N_viradas_shared['N_viradas'] == 3):
                        background = caminho_img
                        background2 = caminho_img
                        valor_anterior = data.valor_20
                        valor_proximo = data.valor_42
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor, line, pino)
                        return line
                elif(fase == 8):
                    # do papel para o final
                    Max_viradas_shared['Max_viradas'] = 3
                    if(N_viradas_shared['N_viradas'] == 0):
                        background = caminho_img
                        background2 = caminho_img
                        valor_anterior = data.valor_42
                        valor_proximo = data.valor_30
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor,line, pino)
                        return line
                    elif(N_viradas_shared['N_viradas'] == 1):
                        background = caminho_img
                        background2 = caminho_img
                        valor_proximo = data.valor_33
                        if(pino == valor_proximo[0]):
                            if((valor > valor_proximo[1] - 100) and (valor < valor_proximo[1] + 100)):
                                data.estado = 'dialogo'
                                data.frase_atual = ""
                                data.index_frase += 4
                                data.letra = len(data.frase_objetivo[data.index_frase])
                                N_viradas_shared['N_viradas'] += 1
                        return line
                    elif(N_viradas_shared['N_viradas'] == 2):
                        background = caminho_img
                        background2 = caminho_img
                        valor_anterior = data.valor_33
                        valor_proximo = data.valor_82
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor, line, pino)
                        return line
                    elif(N_viradas_shared['N_viradas'] == 3):
                        background = caminho_img
                        background2 = caminho_img
                        valor_anterior = data.valor_82
                        valor_proximo = data.valor_81
                        verificacao.verificacao_direita_esquerda(valor_proximo, valor_anterior, valor, line, pino)
                        return line
                   
        except serial.SerialException:
            print("porta serial fechada")
            break



# Thread que lê valor do sensor
def read_sensor_thread(ser, prefix='VAL:', num_values=1):
    global sensor_result, sensor_thread_done
    sensor_result = get_average_sensor_value_from_serial(ser, prefix, num_values)
    print(sensor_result)
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
    global background, background2, fase, contador_virada
    success, img = video.read()
    if success:
        # Converte a imagem do OpenCV (BGR) para uma superfície do Pygame (RGB)
        img_red = cv2.resize(img, (data.width, data.height))
        screen.blit(pygame.image.frombuffer(img_red.tobytes(), (data.width, data.height), "BGR"), (0, 0))
    else:
        data.frase_atual = ""
        data.index_frase += 2
        data.letra = len(data.frase_objetivo[data.index_frase])
        contador_virada = 0
        if background == miku_open_img:
            background = hospital_img
            background2 = hospital_img
            fase += 1
        elif background == hospital_img:
            background = aquario_img
            background2 = aquario_img
            fase += 1
        elif fase == 2:
            background = bombeiro_img
            background2 = bombeiro_img
            fase += 1
            N_viradas_shared['N_viradas'] = 0
        elif fase == 3:
            background = delegacia_img
            background2 = delegacia_img
            fase += 1
        elif fase == 4:
            background = fazenda_img
            background2 = fazenda_img
            fase += 1
        elif fase == 5:
            background = escola_img
            background2 = escola_img
            fase += 1
            N_viradas_shared['N_viradas']
        elif fase == 6:
            background = prefeitura_img
            background2 = prefeitura_img
            fase += 1
        elif fase == 7:
            background = papel_img
            background2 = papel_img
            fase += 1
        elif fase == 8:
            background = final_img
            background2 = final_img
        data.estado = "dialogo"
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        pygame.event.clear()

    pygame.display.flip()
    clock.tick(fps)

def start_game():
    dialogo.frase_acabou['frase_acabou'] = False
    running = True
    clock = pygame.time.Clock()
    delta_time = 0.1
    global sensor_result, sensor_thread_done, waiting_input
    ser = None
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
    stop_thread_event.clear()
    thread = threading.Thread(target=read_sensor_thread, args=(ser,))
    thread.start()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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
            dialogo.frase_acabou['frase_acabou'] = False
        elif(data.estado == 'cutscene'):
            cutscene(clock)
        elif(data.estado == 'fade'):
            fade_out()


        pygame.display.flip()
        delta_time = clock.tick(60) / 1000
        delta_time = max(0.001, min(0.1, delta_time))

    
    stop_thread_event.set()
    if ser:
        ser.close()
    thread.join()
    pygame.quit()
    sys.exit()



start_game()