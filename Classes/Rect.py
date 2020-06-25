import pygame

from General import Functions


class Rect:

    def __init__(self, **kwargs):

        self.width = kwargs.get("width")
        self.height = kwargs.get("height")
        self.x = kwargs.get("x")
        self.y = kwargs.get("y")
        self.color = kwargs.get("color")

        self.label = kwargs.get("label")

    def move(self, x, y):
        self.x = x
        self.y = y

    def draw(self, display, center=False):

        """
        pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        This creates a new object on which you can call the render method.

        textsurface = myfont.render('Some Text', False, (0, 0, 0))
        This creates a new surface with text already drawn onto it. At the end you can just blit the text surface onto your main screen.

        screen.blit(textsurface,(0,0))
        """

        center_x, center_y = int(self.x - self.width / 2), int(self.y - self.height / 2)

        if center:
            pygame.draw.rect(display, self.color, (center_x, center_y, self.width, self.height))
        else:
            pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.height))

        # Functions.draw_font(display, text=str(self.label) + "TEST", x=center_x, y=center_y, color=(255, 255, 255))
