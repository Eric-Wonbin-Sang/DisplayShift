import screeninfo
import pygame
import os

from Classes import Rect
from General import Functions


def main():

    monitor_list = screeninfo.get_monitors()

    pygame.init()
    clock = pygame.time.Clock()

    ratio = .2
    x_delta = int(-1 * min([monitor.x * ratio for monitor in monitor_list]))
    y_delta = 0

    display_width = int((max([monitor.x + monitor.width for monitor in monitor_list]) - min([monitor.x for monitor in monitor_list])) * ratio)
    display_height = int((max([monitor.y + monitor.height for monitor in monitor_list]) - min([monitor.y for monitor in monitor_list])) * ratio)

    display = pygame.display.set_mode((display_width, display_height), 0, 32)
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (-10, 0)
    os.environ['SDL_VIDEO_CENTERED'] = '0'

    rect_list = [Rect.Rect(width=monitor.width * ratio, height=monitor.height * ratio,
                           x=monitor.x * ratio + x_delta, y=monitor.y * ratio + y_delta,
                           color=Functions.get_rand_color(), label=m_i)
                 for m_i, monitor in enumerate(monitor_list)]
    mouse_rect = Rect.Rect(width=10, height=10, x=0, y=0, color=(255, 255, 255))

    curr_monitor = monitor_list[0]
    prev_monitor = curr_monitor
    while True:

        mouse_position = Functions.get_mouse_position(ratio=ratio, x_delta=x_delta, y_delta=y_delta)

        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                quit()

        mouse_rect.move(*mouse_position)

        for monitor in monitor_list:
            if monitor.x * ratio + x_delta <= mouse_rect.x <= (monitor.x + monitor.width) * ratio + x_delta:
                curr_monitor = monitor

        if curr_monitor != prev_monitor:
            mouse_rect.y = (curr_monitor.height/prev_monitor.height) * mouse_rect.y
            # Functions.set_mouse_position(mouse_rect.x / ratio + x_delta, mouse_rect.y)

        print(mouse_rect.x, mouse_rect.y)

        display.fill((0, 0, 0))
        for rect in rect_list:
            rect.draw(display)
        mouse_rect.draw(display, center=True)

        pygame.display.flip()
        clock.tick(60)

        prev_monitor = curr_monitor


main()
