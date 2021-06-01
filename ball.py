import pygame

class ball(object):
    """Class of the ball"""
    def __init__(self):
        """Initialize x, y, free, vel_x, vel_y
        lives_count variables"""
        self.x = 400
        self.y = 460
        self.free = False
        self.vel_x = 0
        self.vel_y = 0
        self.lives_count = 3


    def draw(self, win):
        """Take win and draw circle and border of the circle"""
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), 8,2)
        pygame.draw.circle(win, (255, 0, 0), (self.x, self.y), 6)


    def move(self, lost_life_sound, is_sound, ping_sound):
        """Takes sounds. Check the borders and change velocities
        if hit. If ball crosses the bottom border lives_count is updated
        Update x, y and hitbox"""
        if self.x < 8:
            self.vel_x *= -1
            if is_sound:
                ping_sound.play()
        elif self.x > 792:
            self.vel_x *= -1
            if is_sound:
                ping_sound.play()
        elif self.y < 10 and self.vel_y < 0:
            self.vel_y *= -1
            if is_sound:
                ping_sound.play()
        elif self.y > 592:
            self.free = False
            self.lives_count -= 1
            #play sound
            if is_sound and self.lives_count >= 0:
                lost_life_sound.play()


        self.x += self.vel_x
        self.y += self.vel_y
        self.x = round(self.x)
        self.y = round(self.y)
        self.hitbox = pygame.Rect(self.x - 8, self.y - 8, 16, 16)

    def lives(self, win):
        """Draw lives on the bottom of the screen"""
        x = 75
        for i in range(self.lives_count):
            pygame.draw.circle(win, (0, 0, 0), (x, 550), 8, 2)
            pygame.draw.circle(win, (255, 0, 0), (x, 550), 6)
            x += 25

