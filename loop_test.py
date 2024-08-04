import time
import pygame
from pynput.mouse import Controller

mouse_controller = Controller()

pygame.init()

iterator = 1

while True:
    start_time = time.time()
    last_print_time = start_time

    for i in range(0, 10):
        pygame.time.delay(4)
        mouse_controller.move(5, 0)
        iterator += 1

        current_time = time.time()
        elapsed_time = current_time - last_print_time

        if elapsed_time >= 1.0:
            print(f"Przesunięto mysz {iterator} razy w ciągu ostatniej sekundy.")
            last_print_time = current_time
            iterator = 0

        print(elapsed_time)