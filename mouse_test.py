import time
from pynput.mouse import Controller

def move_mouse_smoothly(controller):
    ...

mouse_controller = Controller()

time.sleep(5)

start_time = time.time()

for x in range(0, 400):
    print(x)
    mouse_controller.move(5, 0)

end_time = time.time()

duration = end_time - start_time

print(f"Duration: {duration} seconds")
