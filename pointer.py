import pygame
from paddle import loadImage
class pointer(pygame.sprite.Sprite):
    """Class of pointer, takes class
    Sprite from module pygame"""
    def __init__(self, center):
        """Take argument center and init Sprite
        class, image and rect"""
        pygame.sprite.Sprite.__init__(self)
        self.image = loadImage("pointer.png", True)
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self, y):
        """Take argument y and move pointer down"""
        self.rect.move_ip((0, y))
