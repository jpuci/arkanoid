import pygame
import random
from paddle import loadImage

class special_opt(pygame.sprite.Sprite):
    """Class of special options.
    Take pygame Sprite class"""
    def __init__(self, center):
        """Take argument center.
        Init Sprite class, option to
        random value form list and image
        based on option. Init rect."""
        pygame.sprite.Sprite.__init__(self)
        self.option = random.choice([0, 1, 2, 3])

        if self.option == 0:
            self.image = loadImage("slow.png", True)
        elif self.option == 1:
            self.image = loadImage("fast.png", True)
        elif self.option == 2:
            self.image = loadImage("wide.png", True)
        elif self.option == 3:
            self.image = loadImage("narrow.png", True)

        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self):
        """Move special down"""
        self.rect.move_ip((0, 2))