import pygame
from paddle import loadImage
class set_pics(pygame.sprite.Sprite):
    """Class of instances with images of
    settings icons. Takes pygame Sprite class."""
    def __init__(self, center, option, typ):
        """Take arguments center, option and typ.
        Init Sprite class, option, type and based on
        postion and type init image and rect"""
        pygame.sprite.Sprite.__init__(self)
        self.option = option
        self.typ = typ
        if self.option == 0:
            if self.typ == "music":
                self.image = loadImage("music.png", True)
            elif self.typ == "sound":
                self.image = loadImage("sound.png", True)
            elif self.typ == "infty":
                self.image = loadImage("infty.png", True)

        elif self.option == 1:
            if self.typ == "music":
                self.image = loadImage("no_music.png", True)
            elif self.typ == "sound":
                self.image = loadImage("no_sound.png", True)
            elif self.typ == "infty":
                self.image = loadImage("no_infty.png", True)

        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self):
        """Update images"""
        if self.option == 1:
            if self.typ == "music":
                self.image = loadImage("music.png", True)
            elif self.typ == "sound":
                self.image = loadImage("sound.png", True)
            elif self.typ == "infty":
                self.image = loadImage("infty.png", True)

        elif self.option == 0:
            if self.typ == "music":
                self.image = loadImage("no_music.png", True)
            elif self.typ == "sound":
                self.image = loadImage("no_sound.png", True)
            elif self.typ == "infty":
                self.image = loadImage("no_infty.png", True)