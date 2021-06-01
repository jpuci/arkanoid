import pygame
from paddle import loadImage

class block(pygame.sprite.Sprite):
    """Class of blocks. Take pygame Sprite class"""
    def __init__(self, dur, x, y, special=False):
        """Take dur, x, y cooridinates and variavle special
        (False by default).Init Sprite class and dur, x, y
        variables. Init image based on dur. Init rectagle
        and special."""
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.dur = dur

        if self.dur == 1:
            self.image = loadImage("crack2.png", True)
        elif self.dur == 2:
            self.image = loadImage("crack1.png", True)
        elif self.dur == 3:
            self.image = loadImage("crack0.png", True)

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.special = special
    def update(self):
        """Update images based on durability"""
        if self.dur == 1:
            self.image = loadImage("crack2.png", True)
        elif self.dur == 2:
            self.image = loadImage("crack1.png", True)
        elif self.dur == 3:
            self.image = loadImage("crack0.png", True)
    def move_down(self):
        """Move block row down"""
        self.rect.move_ip((0, 55))