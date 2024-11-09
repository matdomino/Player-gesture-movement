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
            action = next_action[2]

            if action != last_mouse_action:
                if last_mouse_action in ('r_hold', 'l_hold'):
                    release_mb(action_buttons[last_mouse_action], mouse_controller)

                if action == "l_hold":
                    hold_mb(Button.left, mouse_controller)

                if action == "r_hold":
                    hold_mb(Button.right, mouse_controller)

                if action == "l_single":
                    single_mb_press(Button.left, mouse_controller, last_mouse_action==action)

                if action == "r_single":
                    single_mb_press(Button.right, mouse_controller, last_mouse_action==action)

                last_mouse_action = action
                pygame.time.delay(time_interval)
                continue

            if next_action[0] is not None:
                mouse_controller.move(next_action[0], next_action[1])

            last_mouse_action = action
            pygame.time.delay(time_interval)

        except queue.Empty:
            pass

    pygame.quit()
    release_mb(Button.left, mouse_controller)
    release_mb(Button.right, mouse_controller)
