# import time
# import pygame
# from pynput.mouse import Controller

# mouse_controller = Controller()

# pygame.init()

# iterator = 1
# start_time = time.time()
# last_print_time = start_time

# while True:
#     pygame.time.delay(4)
#     mouse_controller.move(5, 0)
#     iterator += 1

#     current_time = time.time()
#     elapsed_time = current_time - last_print_time

#     if elapsed_time >= 1.0:  # Sprawdza, czy minęła jedna sekunda
#         print(f"Przesunięto mysz {iterator} razy w ciągu ostatniej sekundy.")
#         last_print_time = current_time
#         iterator = 0  # Resetuje licznik

import time
import pygame
from pynput.mouse import Controller

mouse_controller = Controller()

pygame.init()

start_time = time.time()
last_print_time = start_time

while True:
    pygame.time.delay(4)
    mouse_controller.move(5, 0)

    current_time = time.time()
    elapsed_time = current_time - last_print_time

    if elapsed_time >= 1.0:
        loop_duration = current_time - start_time
        print(f"Czas trwania pętli: {loop_duration:.2f} sekundy.")
        last_print_time = current_time

