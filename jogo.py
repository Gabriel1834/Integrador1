import pygame
import random
import serial
import threading
import main
import time

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

font = pygame.font.SysFont(None, 48)
commands = ["Vire à esquerda", "Vire à direita", "Vá para frente"]
clock = pygame.time.Clock()

# Variáveis globais para comunicação com a thread
sensor_result = None
sensor_thread_done = False

def show_message(message, color):
    text_surface = font.render(message, True, color)
    main.screen.blit(
        text_surface,
        (main.WIDTH // 2 - text_surface.get_width() // 2, main.HEIGHT // 2 + 100),
    )

def draw_challenge(command):
    main.screen.fill(BLACK)
    instruction = font.render(command, True, WHITE)
    main.screen.blit(
        instruction,
        (main.WIDTH // 2 - instruction.get_width() // 2, main.HEIGHT // 2 - 50),
    )
    pygame.display.flip()


def get_average_sensor_value_from_serial(ser, prefix='VAL:', num_values=1):
    # values = []

    # while len(values) < num_values:
    #     try:
    #         line = ser.readline().decode(errors='ignore').strip()
    #         if line.startswith(prefix):
    #             try:
    #                 val = int(line[len(prefix):])
    #                 values.append(val)
    #             except ValueError:
    #                 continue
    #     except Exception as e:
    #         print("Erro ao ler da serial:", e)
    #         break

    # if not values:
    #     return None
    # return sum(values) // len(values)
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


def start_game():
    global sensor_result, sensor_thread_done
    running = True

    # Abrir porta serial uma vez só
    try:
        ser = serial.Serial('COM9', 115200, timeout=1)
        ser.setDTR(False)
        ser.setRTS(False)
    except Exception as e:
        print("Erro ao abrir porta serial:", e)
        return

    while running:
        # command = random.choice(commands)
        # draw_challenge(command)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        waiting_input = True
        # Inicia leitura em thread
        sensor_result = None
        sensor_thread_done = False
        thread = threading.Thread(target=read_sensor_thread, args=(ser,))
        thread.start()
        #Primeiro Nivel

        #Esperando resultado do sensor
        while waiting_input:

            # if sensor_thread_done:
            #     if sensor_result is not None:
            #         print("Valor do sensor:", sensor_result)
            #         if command == "Vá para frente":
            #             if sensor_result > 4081:
            #                 show_message("Parabéns, você acertou!", GREEN)
            #             else:
            #                 show_message("Que pena, você errou!", RED)
            #         elif command == "Vire à direita":
            #             if sensor_result > 3850 and sensor_result < 4081:
            #                 show_message("Parabéns, você acertou!", GREEN)
            #             else:
            #                 show_message("Que pena, você errou!", RED)
            #         elif command == "Vire à esquerda":
            #             if sensor_result < 3850 and sensor_result > 3000:
            #                 show_message("Parabéns, você acertou!", GREEN)
            #             else:
            #                 show_message("Que pena, você errou!", RED)

            #         pygame.display.flip()
            #         pygame.time.delay(1500)
            #     else:
            #         print("Valor inválido recebido")
            if sensor_thread_done:
                if sensor_result is not None:
                    #logica de validacao do sensor
                    print(sensor_result)
                    # show_message(sensor_result, GREEN)

                waiting_input = False

                pygame.time.delay(500)
                ser.reset_input_buffer()

                clock.tick(60)

    ser.close()
    pygame.quit()
