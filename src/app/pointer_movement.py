import queue
import pygame
import time
from pynput.mouse import Controller


def pointer_movement_handler(segments_queue, exit_event):
    # dodac to pozniej do konfiguracji w menu
    frame_rate = 240

    time_interval = int(1000/frame_rate)
    mouse_controller = Controller()
    pygame.init()

    while not exit_event.is_set():
        try:
            next_position = segments_queue.get(timeout=1)
            mouse_controller.move(next_position[0], next_position[1])
            pygame.time.delay(time_interval)

        except queue.Empty:
            pass

    pygame.quit()
