import pygame
import os

def loadImage(name, useColorKey = False):
    """Take name and optional argument useColorKey.
    Load image and if useColorkey is True takes color
    from left top corner of the image and make this color
    transparent in pygame"""
    path = os.path.dirname(os.path.abspath(__file__))
    image = pygame.image.load(path+"\\sprites\\" + name)
    image = image.convert()
    if useColorKey:
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image

class paddle(pygame.sprite.Sprite):
    """Class of paddle. Take pygame
    Sprite class"""
    def __init__(self, win_size):
        """Take size of the window and
        initialize image and rect in the middle
        of the display. Init vel and len"""
        pygame.sprite.Sprite.__init__(self)
        self.image = loadImage("paddle.png", True)
        self.rect = self.image.get_rect()
        self.rect.center = (round(win_size[0]/2), round(win_size[1]*0.8))
        self.vel = 0
        self.len = 0

    def update(self, win_size):
        """Move paddle horizontaly and check for borders"""
        self.rect.move_ip((self.vel, 0))
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > win_size[0]:
            self.rect.right = win_size[0]

    def change_paddle(self):
        """Update paddle image and rect
        based on len variable of the paddle"""
        if self.len == 1:
            self.center = self.rect.center
            self.image = loadImage("long_paddle.png", True)
            self.rect = self.image.get_rect()
            self.rect.center = self.center

        if self.len == 0:
            self.center = self.rect.center
            self.image = loadImage("paddle.png", True)
            self.rect = self.image.get_rect()
            self.rect.center = self.center

        if self.len == -1:
            self.center = self.rect.center
            self.image = loadImage("short_paddle.png", True)
            self.rect = self.image.get_rect()
            self.rect.center = self.center





