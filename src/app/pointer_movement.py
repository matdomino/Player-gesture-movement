import queue
import pygame
from pynput.mouse import Controller, Button
from .input_operations import single_mb_press, hold_mb, release_mb

action_buttons = {
    "r_hold": Button.right,
    "l_hold": Button.left
}

def pointer_movement_handler(segments_queue, frame_rate, exit_event):
    time_interval = int(1000/frame_rate)
    mouse_controller = Controller()
    pygame.init()

    last_mouse_action = None

    while not exit_event.is_set():
        try:
            next_action = segments_queue.get(timeout=1)
            mouse_controller.move(next_action[0], next_action[1])

            if next_action[3] is not None and (
                next_action[3] != last_mouse_action or next_action[3] not in ["l_hold", "r_hold"]
            ):
                if last_mouse_action in ('r_hold', 'l_hold'):
                    release_mb(action_buttons[last_mouse_action], mouse_controller)


                # TUTAJ JESZCZE LOGIKA PRZYCISKOW


            pygame.time.delay(time_interval)

        except queue.Empty:
            pass

    pygame.quit()
    release_mb(Button.left, mouse_controller)
    release_mb(Button.right, mouse_controller)
