import queue
import pygame
import time
from pynput.mouse import Controller


def remove_from_queue(queue, amount):
    for _ in range(amount):
        if not queue.empty():
            queue.get()

##############################################
# PRZEROBIC TA PETLE - ZA DUZY BUSY WAITING - BEZ OPOZNIENIA NA POCZATKU PETLI
# CALY PROGRAM ZWALNIA PRZEZ TA FUNKCJE
# PLUS POPRAWIC SPOSOB W JAKI SA OBLICZANE SEGMENTY - UPROSCIC I DODAC DLA MINUSOWYCH WSPOLRZEDNYCH
##############################################

def pointer_movement_handler(positions_queue, exit_event):
    # dodac to pozniej do konfiguracji w menu
    frame_rate = 240

    segments_queue = queue.Queue()
    queue_limit = frame_rate * 2
    time_interval = int(1000/frame_rate)
    mouse_controller = Controller()
    pygame.init()
    roughness_ratio = 0
    iteration_ratio = 0

    while not exit_event.is_set():
        time.sleep(0.001)
        try:
            if segments_queue.qsize() > queue_limit:
                remove_from_queue(segments_queue, frame_rate)
                roughness_ratio += 2
                iteration_ratio += 1
            else:
                if roughness_ratio > 0:
                    roughness_ratio -= 2

                if iteration_ratio > 0:
                    iteration_ratio -= 1

            if positions_queue.qsize() > 0:
                # DOCELOWE X I Y

                x_dest, y_dest = positions_queue.get()

                # DODAC TUTAJ DZIELENIE NA SEGMENTY
                # PO CZYM DODANIE DO KOLEJKI SEGMENTS_QUEUE
                # PRZYPISAC DLA KAZDEGO FRAMERATE ILOSC SEGMENTOW
                # PLUS ZROBIC WARUNKI ZE JAK ROUGHNESS RATIO SIE ZWIEKSZA
                # TO MNIEJ SEGMENTOW PO WIEKSZE ODLEGLOSCI

                # ZMIENIC TU LICZENIE SEGMENTOW - DODAC ZEBY DOLICZALO JESLI
                # iteration_ratio wieksze od 0

                x_segment = x_dest // (10 - iteration_ratio) if x_dest >= (10 - iteration_ratio) else 1

                y_segment = y_dest // (10 - iteration_ratio) if y_dest >= (10 - iteration_ratio) else 1

                for _ in range(10 - iteration_ratio):
                    if x_dest >= x_segment and y_dest >= y_segment:
                        segments_queue.put((x_segment, y_segment))

                        x_dest -= x_segment
                        y_dest -= y_segment
                        continue

                    if x_dest >= x_segment and y_dest <= y_segment:
                        if y_dest > 0:
                            segments_queue.put((x_segment, y_dest))
                        else:
                            segments_queue.put((x_segment, 0))

                        x_dest -= x_segment
                        y_dest = 0
                        continue

                    if x_dest <= x_segment and y_dest >= y_segment:
                        if x_dest > 0:
                            segments_queue.put((x_dest, y_segment))
                        else:
                            segments_queue.put((0, y_segment))

                        y_dest -= y_segment
                        x_dest = 0
                        continue

            next_position = segments_queue.get(block=False)
            mouse_controller.move(next_position[0], next_position[1])
            pygame.time.delay(time_interval)

        except queue.Empty:
            pass

    pygame.quit()
