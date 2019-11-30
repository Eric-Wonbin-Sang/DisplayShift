import pygame
import random
import win32api


def draw_font(display, text, x, y, size=50, color=(0, 0, 0)):
    font = pygame.font.Font(None, size)
    text = font.render(text, True, color)
    display.blit(text, (x, y))


def get_rand_color():
    return random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)


def get_mouse_position(ratio=1.0, x_delta=0, y_delta=0):
    x, y = win32api.GetCursorPos()
    return x * ratio + x_delta, y * ratio + y_delta


def set_mouse_position(x, y):
    win32api.SetCursorPos((int(x), int(y)))
